import json
from datetime import datetime
from stock_scraper.items import Payment

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.strftime("%Y-%m-%d")
        return serial

    if isinstance(obj, dict):
        return obj
   
    if isinstance(obj, Payment):
        return dict(obj)

    return str(obj)
