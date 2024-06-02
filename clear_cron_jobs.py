from crontab import CronTab

cron = CronTab(user='pi')
for job in cron:
    print("Removing:", job)
    cron.remove(job)

cron.write()
print("Crontab cleared successfully")
