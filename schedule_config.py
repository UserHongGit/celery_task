#schedule_config.py
from base_config import app
from celery.schedules import crontab



# 定时任务配置
app.conf.beat_schedule = {
    'add-every-10-seconds': {
        'task': 'tasks.test_task.add',
        'schedule': 10.0,  # 每10秒执行一次
        'args': (16, 16)
    },
    'print-time-every-minute': {
        'task': 'tasks.test_task.print_time',
        'schedule': crontab(minute='*'),  # 每分钟执行一次
    },
}
