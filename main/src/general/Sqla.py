from sqlalchemy import text

from main.models.models import db

class Sqla():
    def __init__(self, current_app = ''):
        self.current_app = current_app

    def fetch_to_dict(self, sql, params={}, fecth='all'):
        '''
        dict的方式返回数据
        :param sql: select * from xxx where name=:name
        :param params:{'name':'zhangsan'}
        :param fecth:默认返回全部数据，返回格式为[{},{}],如果fecth='one',返回单条数据，格式为dict
        :param bind:连接的数据，默认取配置的SQLALCHEMY_DATABASE_URL，
        :return:
        '''

        #IN 查询支持直接入参list
        for params_one in params:
            if isinstance(params[params_one], list):
                params[params_one] = tuple(params[params_one])

        resultProxy = db.session.execute(sql, params, bind=db.get_engine(self.current_app,bind='xlauto_mysql'))
        if fecth == 'one':
            result_tuple = resultProxy.fetchone()
            if result_tuple:
                result = dict(zip(resultProxy.keys(), list(result_tuple)))
            else:
                return None
        else:
            result_tuple_list = resultProxy.fetchall()
            if result_tuple_list:
                result = []
                keys = resultProxy.keys()
                for row in result_tuple_list:
                    result_row = dict(zip(keys, row))
                    result.append(result_row)
            else:
                return None
        db.session.remove()
        return result


    # 分页
    def fetch_to_dict_pagetion(self, sql, params={}, page=1, page_size=15):
        sql_count = """select count(*) as count from (%s) _count""" % sql
        total_count = self.get_count(sql_count, params, bind='xlauto_mysql')
        sql_page = '%s limit %s,%s' % (sql, (page - 1) * page_size, page_size)
        print('sql_page:', sql_page)
        result = self.fetch_to_dict(sql_page, params, 'all', bind='xlauto_mysql')
        result_dict = {'results': result, 'count': total_count}
        return result_dict


    # 执行单条语句（update,insert）
    def execute(self, sql, params={}):
        print('sql', sql)
        db.session.execute(sql, params, bind=db.get_engine(bind='xlauto_mysql'))
        db.session.commit()
        db.session.remove()

    def get_count(self, sql, params={}):
        return int(self.fetch_to_dict(sql, params, fecth='one', bind='xlauto_mysql').get('count'))

    # 执行多条语句，失败自动回滚
    def execute_many(self, sqls):
        print(sqls)
        if not isinstance(sqls, (list, tuple)):
            raise Exception('type of the parameters must be list or tuple')
        if len(sqls) == 0:
            raise Exception("parameters's length can't be 0")
        for statement in sqls:
            if not isinstance(statement, dict):
                raise Exception("parameters erro")
        try:
            for s in sqls:
                db.session.execute(s.get('sql'), s.get('params'), bind=db.get_engine(bind=s.get('bind', 'xlauto_mysql')))
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception("execute sql fail ,is rollback")
        db.session.remove()
    #https://www.cnblogs.com/gongnanxiong/p/11743055.html
    #加密
    def sql_encryption(self, str):
        sql = """
        select HEX(AES_ENCRYPT(:str, :iskey)) AS passwd;
        """
        # test= self.fetch_to_dict(sql,{'str':str, 'iskey': self.current_app.config['PASS_KEY']})
        return self.fetch_to_dict(sql,{'str':str, 'iskey': self.current_app.config['PASS_KEY']})[0]['passwd']
    # 解密
    def sql_decrypt(self, unhex_str):
        sql = """
        select AES_DECRYPT(UNHEX(:str), :iskey) AS passwd;
        """
        # test = self.fetch_to_dict(sql, {'str': unhex_str, 'iskey': self.current_app.config['PASS_KEY']})
        passwd = self.fetch_to_dict(sql,{'str':unhex_str, 'iskey': self.current_app.config['PASS_KEY']})[0]['passwd']
        return str(passwd, encoding="utf-8")


    def GetInsertOrUpdateObj(self, cls, strFilter, **kw):
        '''
        cls:            Model 类名
        strFilter:      filter的参数.eg:"name='name-14'"
        **kw:           【属性、值】字典,用于构建新实例，或修改存在的记录
        '''
        existing = db.session.query(cls).filter_by(text(strFilter)).first()
        if not existing:
            res = cls()
            for k, v in kw.items():
                if hasattr(res, k):
                    setattr(res, k, v)
        else:
            res = existing
            for k, v in kw.items():
                if hasattr(res, k):
                    setattr(res, k, v)

        db.session.commit()
        db.session.close()
        db.session.remove()
        return res
