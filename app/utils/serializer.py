from bson import ObjectId
from datetime import datetime


def serialize_data(data):
    """
    Recursively converts MongoDB ObjectId and datetime objects
    into JSON serializable values.
    """

    if isinstance(data, list):
        return [serialize_data(item) for item in data]

    if isinstance(data, dict):
        return {key: serialize_data(value) for key, value in data.items()}

    if isinstance(data, ObjectId):
        return str(data)

    if isinstance(data, datetime):
        return data.isoformat()

    return data