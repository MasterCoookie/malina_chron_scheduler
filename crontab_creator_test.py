from crontab import CronTab
cron = CronTab(user='pi')

job = cron.new(command='python3 /home/pi/Projects/Python/crontab_call_test.py')

job.minute.every(1)

cron.write()

print("Crontab created successfully")
