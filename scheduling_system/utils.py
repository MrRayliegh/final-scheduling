import datetime
from django.utils.timezone import get_current_timezone, is_naive

def safe_make_aware(value, tz=None):
    """
    Convert a naive datetime to an aware datetime.
    If value is already aware, return as-is.
    """
    if isinstance(value, str):  
        # Convert string to datetime
        try:
            value = datetime.datetime.fromisoformat(value)
        except ValueError:
            raise ValueError(f"String '{value}' is not in a valid datetime format.")

    if not isinstance(value, datetime.datetime):
        raise TypeError(f"safe_make_aware() expects a datetime object, got {type(value).__name__}")

    if tz is None:
        tz = get_current_timezone()  # Use Django's current timezone

    if is_naive(value):  
        return value.replace(tzinfo=tz)

    return value  # Already aware, return as-is
