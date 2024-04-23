from rest_framework.test import APITestCase, APIClient
from keep_secrets.models import Secret
from rest_framework import status


class SecretTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.secret = Secret.objects.create(text='test text')

    def test_create_secret(self):
        data = {
            "text": 'test text',
        }
        response = self.client.post(
            'http://127.0.0.1:8000/keep_secrets/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_no_secret(self):
        response = self.client.get(
            'http://127.0.0.1:8000/keep_secrets/check/test/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )
        self.assertEqual(
            response.json(),
            {
                "Ошибка": "Секрет с указанным кодом не найден"
            }
        )

    # def test_get_secret(self):
    #     response = self.client.get(
    #         f'http://127.0.0.1:8000/keep_secrets/check/{self.secret.code}',
    #     )
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK
    #     )
    #     self.assertEqual(
    #         response.json(),
    #         {
    #             "Секрет": "test text"
    #         }
    #     )