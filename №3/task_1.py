from datetime import datetime, timedelta

def datetime_info(date_str):
    date = datetime.strptime(date_str, '%Y-%m-%d')
    
    formatted_date = date.strftime('%d-%m-%Y')
    
    day_of_week = date.strftime('%A')
    
    next_year = date.replace(year=date.year + 1)
    days_until_next_year = (next_year - date).days
    
    return {
        'formatted_date': formatted_date,
        'day_of_week': day_of_week,
        'days_until_next_year': days_until_next_year
    }

print(datetime_info('2024-10-24'))
