import json
import uuid
import datetime
import decimal


class JSONExtendEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, datetime.date):
            return o.strftime('%Y-%m-%d')
        elif isinstance(o, decimal.Decimal):
            return str(o)  # float(o)
        elif isinstance(o, bytes):
            return o.decode('utf-8')
        elif isinstance(o, uuid.UUID):
            return str(o)
        return super().default(o)


# json to dict
def from_json(data):
    """JSON 字符串转字典"""
    return json.loads(data)


# dict to json
def to_json(data):
    """字典转 JSON 字符串"""
    return json.dumps(
        data,
        cls=JSONExtendEncoder,
        ensure_ascii=False
    )
