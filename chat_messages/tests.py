from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import MessageCreateView


class TestViews(TestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()

    def test_create_message_success(self):
        request_success = self.factory.post('api/messages/',
                                            {'email': 'test@gmail.com', 'message': 'test message'},
                                            format='json')
        response_success = MessageCreateView.as_view()(request_success)

        self.assertEqual(response_success.status_code, 201)

    def test_create_message_fail(self):
        request_email_fail = self.factory.post('api/messages/',
                                              {'email': 'testfail.com', 'message': 'test message'},
                                              format='json')
        response_email_fail = MessageCreateView.as_view()(request_email_fail)
        request_message_empty_fail = self.factory.post('api/messages/',
                                                       {'email': 'test@gmail.com', 'message': ''},
                                                       format='json')
        response_message_empty_fail = MessageCreateView.as_view()(request_message_empty_fail)
        request_message_many_fail = self.factory.post('api/messages/',
                                                      {'email': 'test@gmail.com', 'message': 'test' * 25},
                                                      format='json')
        response_message_many_fail = MessageCreateView.as_view()(request_message_many_fail)

        self.assertEqual(response_email_fail.status_code, 400)
        self.assertEqual(response_message_empty_fail.status_code, 400)
        self.assertEqual(response_message_many_fail.status_code, 400)
