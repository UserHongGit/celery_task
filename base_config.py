# base_config.py
# 配置Celery
from celery import Celery


app = Celery('my_celery_project'
             # ,broker=celeryconfig.broker_url
             # , backend=celeryconfig.result_backend
             )
app.config_from_object('worker_config:celeryconfig')

import tasks.test_task

import schedule_config

# app.conf.update(
#     CELERY_ACCEPT_CONTENT = ['json'],
#     CELERY_TASK_SERIALIZER = 'json',
#     CELERY_RESULT_SERIALIZER = 'json'
# )



# 如果使用Django，还可以自动发现任务
# app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
