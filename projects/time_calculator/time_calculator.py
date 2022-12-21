def add_time(current_time, added_time, day_of_week = None):
    added_time=added_time.split(':')
    added_time=int(added_time[0]) * 60 + int(added_time[1])

    [current_time, daytime]=current_time.split()
    current_time=current_time.split(':')
    current_time=int(current_time[0]) * 60 + int(current_time[1])
    if daytime == "PM": current_time += 12 * 60

    # total time 
    total_min = current_time + added_time
    tot_hours = (total_min // 60)
    tot_min = (total_min % 60)

    # number of days passed
    days_elapsed = tot_hours // 24
    tot_hours = tot_hours % 24
    res_daytime = "AM"
    if (tot_hours >= 12):
        res_daytime = "PM"
        tot_hours = tot_hours - 12

    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if (day_of_week != None):
        day_of_week = str(day_of_week).casefold()
        idx = week_days.index(day_of_week)
        end_idx = idx + days_elapsed % 7
        end_day = week_days[end_idx].capitalize()
    
    hours_str = '{0:02d}:{1:02d} {2}'.format(tot_hours, tot_min, res_daytime)
    days_str = f'({"next day" if days_elapsed == 1 else str(days_elapsed) + " days later"})' if days_elapsed > 0 else ''
    return f'{hours_str}{", " + end_day if "end_day" in locals() else ""} {days_str}'