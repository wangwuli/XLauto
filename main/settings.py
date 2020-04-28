#数据库
#————————————————————————————————————#
#数据库配置
database_service_ip="127.0.0.1"
database_service_port=3306
database_name="xlauto"
database_user="root"
database_pwd="wangwuli"

database_url = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=database_user,password=database_pwd, host=database_service_ip,port=database_service_port, db=database_name)

#连接数据库
SQLALCHEMY_DATABASE_URI = database_url

#如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = False

#sql是否调试
SQLALCHEMY_ECHO = True

#数据库池的大小，默认值为5
SQLALCHEMY_POOL_SIZE = 5

#连接超时时间
SQLALCHEMY_POOL_TIMEOUT = 30

#自动回收连接的秒数
SQLALCHEMY_POOL_RECYCLE = 5

#控制在连接池达到最大值后可以创建的连接数，当这些额外的 连接回收到连接池后将会被断开和抛弃
SQLALCHEMY_MAX_OVERFLOW = 5

SQLALCHEMY_BINDS = {
    "xlauto_mysql" : SQLALCHEMY_DATABASE_URI
}
#————————————————————————————————————#

PASS_KEY = 'xlauto'