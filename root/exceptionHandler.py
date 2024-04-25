from rest_framework.views import exception_handler
from rest_framework.response import Response

from root.models import RootException


def custom_exception_handler(exc, context):
    if isinstance(exc, RootException):
        response_data = {
            'code': exc.status_code,
            'detail': getattr(exc, 'detail', "default_detail")
        }
        return Response(response_data, status=getattr(exc, 'status_code', 500))
    response_data = {
            'code': 500,
            'detail': getattr(exc, 'message', repr(exc))
        }
    return Response(response_data, status=500)  