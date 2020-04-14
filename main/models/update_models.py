import os
import settings

cmd = "flask-sqlacodegen mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8 --outfile ./models.py  --flask".format(
        username=settings.database_user, password=settings.database_pwd, host=settings.database_service_ip,
        port=settings.database_service_port,
        db=settings.database_name)

os.system(cmd)

