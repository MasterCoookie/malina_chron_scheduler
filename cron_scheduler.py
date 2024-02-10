def generate_cron_line(minute_freq, starting_hour, ending_hour, weekdays):
    cron_line = f'*/{minute_freq} {starting_hour}-{ending_hour} * * '
    cron_line += ' '.join([str(i) for i, range in enumerate(weekdays) if range])
    return cron_line