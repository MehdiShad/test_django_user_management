from .models import BaseUser, Process
from django.db.models import QuerySet


async def get_all_processes() -> QuerySet[Process]:
    process = await Process.objects.filter()
    return process
