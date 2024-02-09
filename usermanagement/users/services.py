from django.db import transaction 
from .models import BaseUser, Process
from django.http import HttpRequest
from usermanagement.core.exceptions import error_response, success_response


def create_user(*, email: str, password: str) -> BaseUser:
    return BaseUser.objects.create_user(email=email, password=password)


@transaction.atomic
def register(*, email: str, password: str) -> BaseUser:
    user = create_user(email=email, password=password)
    return user


async def create_process(reqeust: HttpRequest, **kwargs):
    try:
        process = Process.objects.create(name=kwargs.get("name"))
        return success_response(data=process)
    except Exception as ex:
        return error_response(message=str(ex))



