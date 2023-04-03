from kmgetgbot.utils.api import api


async def check_phone_number_in_db(phone_number: str) -> bool:
    employee_phone_in_db = api.get_employee_by_phone_number(phone_number)
    if employee_phone_in_db:
        return True
    else:
        return False


async def register_chat_id(chat_id: int, phone_number: str) -> None:
    api.patch_employee_chat_id_by_phone_number(phone_number, chat_id)
