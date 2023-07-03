import json


class Check:
    """Методы для проверки запросов"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод проверки статус кода"""

        assert status_code == result.status_code
        print("Статус код: " + str(result.status_code) + ", Успешно!")

    @staticmethod
    def check_json_token(result, expected_value):
        """Метод проверки обязательных полей ответа"""

        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """Метод проверки значений обязательных полей ответа"""

        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print("значение поля " + field_name + ", верно")

