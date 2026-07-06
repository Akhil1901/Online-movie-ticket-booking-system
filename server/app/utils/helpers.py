from datetime import datetime


def current_time():
    """
    Returns current UTC time.
    """
    return datetime.utcnow()


def format_datetime(dt):
    """
    Format datetime object.
    """
    if dt is None:
        return None

    return dt.strftime("%Y-%m-%d %H:%M:%S")