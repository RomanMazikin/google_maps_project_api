from utils.http_methods import HttpMethods

base_url = 'https://rahulshettyacademy.com'   # базовая url
key = '?key=qaclick123'                       # параметр для всех запросов


class GoogleMapsApi:
    """Методы для создания, изменения и удаления новой локации"""
    @staticmethod
    def create_new_place():
        """Метод для создания новой локации"""

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = '/maps/api/place/add/json'  # Ресурс метода post
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    @staticmethod
    def get_new_place(place_id):
        """Метод проверки созданной локации"""

        get_resource = '/maps/api/place/get/json'  # Ресурс метода get
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_new_place(place_id):
        """Метод изменения новой локации"""

        put_resource = '/maps/api/place/update/json'  # Ресурс метода put
        put_url = base_url + put_resource + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """Метод удаления локации"""

        delete_resource = '/maps/api/place/delete/json'  # Ресурс метода delete
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_location = {
            "place_id": place_id
        }
        result_delete = HttpMethods.delete(delete_url, json_for_delete_location)
        print(result_delete.text)
        return result_delete


