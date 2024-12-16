# base_config.py
class DataSourceConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Hong@localhost:3306/test?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
class CeleryConfig:
    broker_url = 'redis://localhost:6379/6'  # 这里使用Redis作为示例
    result_backend = 'redis://localhost:6379/6'
    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    timezone = 'Asia/Shanghai'
    enable_utc = True
    worker_pool = 'solo'

celeryconfig = CeleryConfig()
