from django.db import transaction 
from .models import BaseUser, Process
from django.http import HttpRequest
from usermanagement.core.exceptions import error_response, success_response
from django.contrib.auth.decorators import login_required, permission_required


def create_user(*, email: str, password: str) -> BaseUser:
    return BaseUser.objects.create_user(email=email, password=password)


@transaction.atomic
def register(*, email: str, password: str) -> BaseUser:
    user = create_user(email=email, password=password)
    return user

@login_required
@permission_required(
    {
        ("users.add_process"),
        ("users.dg_can_start_process"),
    }, raise_exception=True
)
def create_process(reqeust: HttpRequest, **kwargs):

    try:
        user = reqeust.user
        company = user.last_company_logged_in
        process = Process.objects.create(name=kwargs.get("name"), created_by=user, company=company)
        return success_response(data=process)
    except Exception as ex:
        return error_response(message=str(ex))



