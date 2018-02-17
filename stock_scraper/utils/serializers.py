
from datetime import datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.strftime("%Y-%m-%d")
        return serial

    return str(obj)
