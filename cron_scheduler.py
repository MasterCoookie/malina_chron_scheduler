def generate_cron_line(minute_freq: int, starting_hour: int, ending_hour: int, weekdays: int) -> str:
    if minute_freq < 1 or minute_freq > 59:
        raise Exception('Invalid minute frequency')
    if starting_hour < 0 or starting_hour > 23:
        raise Exception('Invalid starting hour')
    if ending_hour < 0 or ending_hour > 23:
        raise Exception('Invalid ending hour')
    if starting_hour > ending_hour:
        raise Exception('Starting hour cannot be greater than ending hour')
    if len(weekdays) != 7:
        raise Exception('Invalid weekdays list')
    
    if not any(weekdays):
        raise Exception('At least one day of the week must be selected')

    cron_line = f'*/{minute_freq} {starting_hour}-{ending_hour} * *'
    weekdays_cron_line = ','.join([str(i+1) for i, range in enumerate(weekdays[:-1]) if range])
    if weekdays[-1]:
        weekdays_cron_line = f'0,{weekdays_cron_line}'
    cron_line = f'{cron_line} {weekdays_cron_line}'
    return cron_line
