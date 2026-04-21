import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from .keyboards import main_keyboard, ABOUT_TEXT
from .functions import send_message
from .config import VK_GROUP_TOKEN


def run() -> None:
    """
    Запуск бота и обработка сообщений
    :return:
    """
    session = vk_api.VkApi(token=VK_GROUP_TOKEN)
    vk = session.get_api()
    group_id = vk.groups.getById()[0]['id']
    long_poll = VkBotLongPoll(session, group_id)

    print('Бот запущен...')

    for event in long_poll.listen():
        if event.type != VkBotEventType.MESSAGE_NEW:
            continue

        message = event.object.message
        text = str(message.get('text', '')).strip()
        peer_id = int(message.get('peer_id', 0))

        if not text:
            continue

        lower_text = text.lower()
        if lower_text in {'/start', 'start', 'menu', 'меню'}:
            send_message(
                vk,
                peer_id,
                (
                    'Привет. На связи тестовый бот VK.\n'
                ),
                keyboard=main_keyboard(),
            )
            continue

        if 'привет' in lower_text:
            send_message(
                vk,
                peer_id,
                'И тебе привет',
                keyboard=main_keyboard(),
            )
            continue

        if lower_text == ABOUT_TEXT.lower():
            send_message(
                vk,
                peer_id,
                'Мы на курсе!',
                keyboard=main_keyboard(),
            )
            continue
