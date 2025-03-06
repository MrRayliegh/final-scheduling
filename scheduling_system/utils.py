from datetime import datetime
from django.utils.timezone import get_current_timezone, is_aware

def safe_make_aware(value):
    """Ensure datetime values are timezone-aware."""
    if isinstance(value, str):
        try:
            value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError(f"Invalid datetime format: {value}")

    if not isinstance(value, datetime):
        raise TypeError(f"safe_make_aware expects a datetime object, got {type(value).__name__}")

    if is_aware(value):
        return value  # Already aware, return as is

    return value.astimezone(get_current_timezone())
