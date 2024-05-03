
class HttpError(Exception):
    """Generic HttpError exception"""
class BadRequest(HttpError):
    """Raise for 400 bad request responses"""
