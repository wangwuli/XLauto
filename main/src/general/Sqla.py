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


#https://www.cnblogs.com/gongnanxiong/p/11743055.html