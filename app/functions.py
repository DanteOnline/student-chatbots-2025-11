import random
import vk_api


def _generate_random_id() -> int:
    """
    Генерация случайного id
    :return:
    """
    return random.randint(1, 2_147_483_647)


def send_message(
    vk: vk_api.VkApiMethod,
    peer_id: int,
    text: str,
    keyboard: str | None = None,
) -> None:
    payload = {
        'peer_id': peer_id,
        'message': text,
        'random_id': _generate_random_id()
    }
    if keyboard:
        payload['keyboard'] = keyboard
    vk.messages.send(**payload)
