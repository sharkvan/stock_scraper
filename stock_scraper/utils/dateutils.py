from datetime import datetime

def friendly_date(obj):

    if isinstance(obj, datetime):
        serial = obj.date().isoformat()
        return serial

    return str(obj)
