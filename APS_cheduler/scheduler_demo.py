from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from task_test import add, print_time

# 创建一个后台调度器
scheduler = BackgroundScheduler()

# 添加定时任务
# 每10秒执行一次 add 任务
scheduler.add_job(add, 'interval', seconds=10, args=[16, 16], id='add_job')

# 每分钟执行一次 print_time 任务
scheduler.add_job(print_time, 'cron', minute='*', id='print_time_job')

# 启动调度器
scheduler.start()

try:
    # 保持程序运行
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    # 优雅地关闭调度器
    scheduler.shutdown()
