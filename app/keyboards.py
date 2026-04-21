from vk_api.keyboard import VkKeyboard, VkKeyboardColor


ABOUT_TEXT = 'О нас'


def main_keyboard() -> str:
    keyboard = VkKeyboard(one_time=False, inline=False)
    keyboard.add_button(ABOUT_TEXT, color=VkKeyboardColor.PRIMARY)
    return keyboard.get_keyboard()
