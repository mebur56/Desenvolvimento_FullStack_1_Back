from datetime import datetime


def valid_schedule(schedule):
    print(schedule)
    if not schedule["title"]:
        return False, "Título não pode ser nulo"
    if not valid_date(schedule["date"]):
        return False, "Data inválida"    
    
    return True, ""


def valid_date(data_str):
    print(data_str)
    try:
        datetime.strptime(data_str, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False