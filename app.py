from crontab import CronTab


if __name__ == '__main__':
    print('Specify weekdays active, 0 - SUN, 1 - MON ..., 6 - SAT:')
    weekdays = input('0 for SUN only, 1-3 for MON-WED, * for everyday:\n')
    print('Specify hours active, 0-23:')
    hours = input('0 for midnight, 3-15 for 3AM to 3PM, * for every hour:\n')
    print('Specify minutes active, 0-59:')
    minutes = input('0 for the start of the hour, 15-30 for minutes from 15 to 30, * for every minute:\n')
    cron = CronTab(user='pi')
    job = cron.new(command='python3 ~/malina_cron_scheduler/crontab_call_test.py')
    
    try:
        job.setall(f'{minutes} {hours} * * {weekdays}')
        cron.write()
    except KeyError as e:
        print(f'Error: {e}')
        print('Check your input and try again')
        exit(1)
    print("Crontab created successfully:")
    print(job)
