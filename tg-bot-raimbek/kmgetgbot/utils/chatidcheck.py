from kmgetgbot.utils.api import api


async def check_chat_id(chat_id: int) -> bool:
    if api.get_employee_by_chat_id(chat_id)['chat_id'] == chat_id:
        return True
    return False
