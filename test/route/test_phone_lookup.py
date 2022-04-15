from unittest import TestCase
from app import create_app


class TestNumbers(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_without_country_code(self):
        """
        This test makes sure that the API returns proper error regarding missing value of country code
        """
        url = "/v1/phone-numbers?phoneNumber=2125690123"
        response = self.app.get(url)
        self.assertEqual(
            {
                "error": {"countryCode": "required value is missing"},
                "phoneNumber": "2125690123",
            },
            response.get_json(),
        )

    def test_with_country_code(self):
        """
        This test makes sure that the API returns the supposed response when the correct phoneNumber and countryCode is provided
        """
        url = "/v1/phone-numbers?phoneNumber=12125690123&countryCode=US"
        response = self.app.get(url)
        self.assertEqual(
            {
                "areaCode": "212",
                "countryCode": "US",
                "localPhoneNumber": "5690123",
                "phoneNumber": "12125690123",
            },
            response.get_json(),
        )

    def test_with_spaces(self):
        """
        This test makes sure that the API returns correct response when a valid phone number with spaces is provided
        """
        url = "/v1/phone-numbers?phoneNumber=%2B52%20631%203118150"
        response = self.app.get(url)
        self.assertEqual(
            {
                "areaCode": "631",
                "countryCode": "MX",
                "localPhoneNumber": "3118150",
                "phoneNumber": "+52 631 3118150",
            },
            response.get_json(),
        )

    def test_without_spaces(self):
        """
        This test makes sure that the API return valid response when a correct phone number without spaces is provided
        """
        url = "/v1/phone-numbers?phoneNumber=%2B12125690123"
        response = self.app.get(url)
        self.assertEqual(
            {
                "areaCode": "212",
                "countryCode": "US",
                "localPhoneNumber": "5690123",
                "phoneNumber": "+12125690123",
            },
            response.get_json(),
        )

    def test_invalid_phone_number(self):
        """
        This test makes sure that the API returns proper error when invalid phone number is provided
        """
        url = "/v1/phone-numbers?phoneNumber=%2B121256901233434"
        response = self.app.get(url)
        self.assertEqual({"error": "phone number invalid"}, response.get_json())
