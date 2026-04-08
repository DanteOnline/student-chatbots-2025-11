from django.db import models


class TelegramUser(models.Model):
    tg_id = models.PositiveBigIntegerField(unique=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return f'{self.tg_id} {self.first_name} {self.last_name}'


async def create_user(
    tg_id: int,
    first_name:str=None,
    last_name:str=None
) -> tuple[bool, TelegramUser | None]:
    new_user = None
    created = False
    is_user_exists = await TelegramUser.objects.filter(tg_id=tg_id).aexists()
    if not is_user_exists:
        new_user = await TelegramUser.objects.acreate(
            tg_id = tg_id,
            first_name = first_name,
            last_name = last_name,
        )
        created = True
    return created, new_user


# async def user_list():
#     users = [str(user) async for user in TelegramUser.objects.all()]
#     return users
