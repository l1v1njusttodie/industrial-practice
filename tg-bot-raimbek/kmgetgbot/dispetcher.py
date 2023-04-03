from handlers.login.chat_id_handler import *
from handlers.registration.phone_number_handler import *
from handlers.menu.menu import *
from handlers.registration.registration_handler import *
from kmgetgbot.handlers.menu.faq.faq import faq_handler, answer_handler
from kmgetgbot.handlers.menu.info.info_menu import info_menu, about_menu_handler
from kmgetgbot.handlers.menu.info.infoSections.aboutCompany.about_company_menu import about_company_menu
from kmgetgbot.handlers.menu.info.infoSections.companyAddresses.addresses_menu import addresses_menu
from kmgetgbot.handlers.menu.info.infoSections.companyAddresses.address_handler import address_handler
from kmgetgbot.handlers.menu.info.infoSections.aboutCompany.about_company_handler import about_company_handler


def append_handlers(application):
    application.add_handler(start_handler)
    application.add_handler(phone_number_handler)
    application.add_handler(registration_handler)
    application.add_handler(faq_handler)
    application.add_handler(answer_handler)
    application.add_handler(info_menu)
    application.add_handler(about_company_menu)
    application.add_handler(addresses_menu)
    application.add_handler(about_menu_handler)
    application.add_handler(about_company_handler)
    application.add_handler(menu_handle)
    application.add_handler(address_handler)
    return application
