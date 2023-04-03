import requests


class API:
    def __init__(self):
        self.base_url = 'http://127.0.0.1:8000/'

    def _get_request(self, additional_url: str) -> dict:
        try:
            response = requests.get(self.base_url + additional_url)
            return response.json()
        except ConnectionError as e:
            response = "No response"
            print(e, response)

    def _patch_request(self, additional_url: str, data: dict) -> None:
        try:
            requests.patch((self.base_url + additional_url), data)
        except ConnectionError as e:
            response = "Could not change"
            print(response, e)

    def _post_request(self, additional_url: str, data: dict) -> None:
        try:
            requests.post((self.base_url + additional_url), data)
        except ConnectionError as e:
            response = "Can't create"
            print(response, e)

    def get_employee_by_id(self, employee_id: int) -> dict:
        additional_url = f"employee/?type=id&value={employee_id}"
        employee = self._get_request(additional_url)
        return employee

    def get_employee_by_phone_number(self, phone_number: str) -> dict:
        additional_url = f"employee/?type=phone_number&value={phone_number}"
        employee = self._get_request(additional_url)
        return employee

    def get_employee_by_chat_id(self, chat_id: int) -> dict:
        additional_url = f"employee/?type=chat_id&value={chat_id}"
        employee = self._get_request(additional_url)
        return employee

    def get_employee_list(self) -> dict:
        additional_url = "employee/detail/"
        employee_list = self._get_request(additional_url)
        return employee_list

    def get_answer_by_id(self, answer_id: int) -> dict:
        additional_url = f"faq/?type=id&value={answer_id}"
        answer = self._get_request(additional_url)
        return answer

    def get_faq_list(self) -> dict:
        additional_url = "faq/faq/"
        faq_list = self._get_request(additional_url)
        return faq_list

    def get_about_company(self, answer_id: int) -> dict:
        additional_url = f"info/?type=id&value={answer_id}"
        about_company = self._get_request(additional_url)
        return about_company

    def get_address(self, address_id: int) -> dict:
        additional_url = f"info/address/?type=id&value={address_id}"
        address_company = self._get_request(additional_url)
        return address_company

    def patch_employee_chat_id_by_phone_number(self, phone_number: str, chat_id: int) -> None:
        patch_data = {"chat_id": f"{chat_id}"}
        additional_url = f"employee/?type=phone_number&value={phone_number}"
        self._patch_request(additional_url, patch_data)

    # def post_employee(self, username: str, firstname: str):


api = API()
