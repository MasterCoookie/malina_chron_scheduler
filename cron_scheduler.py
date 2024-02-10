def generate_cron_line(minute_freq: int, starting_hour: int, ending_hour: int, weekdays: int) -> str:
    cron_line = f'*/{minute_freq} {starting_hour}-{ending_hour} * *'
    weekdays_cron_line = ','.join([str(i+1) for i, range in enumerate(weekdays[:-1]) if range])
    if weekdays[-1]:
        weekdays_cron_line = f'0,{weekdays_cron_line}'
    cron_line = f'{cron_line} {weekdays_cron_line}'
    return cron_line
