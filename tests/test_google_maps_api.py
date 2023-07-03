from utils.check import Check
import allure
from utils.api import GoogleMapsApi


@allure.epic('Test create place')
class TestCreatePlace:
    """Тест на создание, изменение и удаление новой локации"""

    @allure.description("Test create, update, delete new place")
    def test_create_new_place(self):
        print("метод POST")
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Check.check_status_code(result_post, 200)
        Check.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Check.check_json_value(result_post, "status", "OK")

        print('метод GET(post)')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Check.check_status_code(result_get, 200)
        Check.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                            'types', 'website', 'language'])
        Check.check_json_value(result_get, "address", "29, side layout, cohen 09")

        print('метод PUT')
        result_put = GoogleMapsApi.put_new_place(place_id)
        Check.check_status_code(result_put, 200)
        Check.check_json_token(result_put, ['msg'])
        Check.check_json_value(result_put, "msg", "Address successfully updated")

        print('метод GET(put)')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Check.check_status_code(result_get, 200)
        Check.check_json_token(result_get,
                               ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                'language'])
        Check.check_json_value(result_get, "address", "100 Lenina street, RU")

        print('метод DELETE')
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Check.check_status_code(result_delete, 200)
        Check.check_json_token(result_delete, ['status'])
        Check.check_json_value(result_delete, "status", "OK")

        print('метод GET(delete)')
        result_get = GoogleMapsApi.get_new_place(place_id)
        Check.check_status_code(result_get, 404)
        Check.check_json_token(result_get, ['msg'])
        Check.check_json_value(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")






