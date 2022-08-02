from django.test import TestCase, Client
from group_chat_app import models
from datetime import datetime, timezone

class TestModels(TestCase):

    def setUp(self):
        utc_datetime_now = datetime.now(timezone.utc)
        local_datetime = utc_datetime_now.astimezone()
        local_datetime = local_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.mymessage = models.Message(message_text='Test Text Message', user_name='test_user_1', group_name='Lavelle', likes=0, dislikes=0, created_at=local_datetime)

    def test_message_creation(self):
        utc_datetime_now = datetime.now(timezone.utc)
        local_datetime = utc_datetime_now.astimezone()
        local_datetime = local_datetime.strftime('%Y-%m-%d %H:%M:%S')
        self.new_message = models.Message(message_text='New Test Text Message', user_name='test_user_2', group_name='Lavelle', likes=0, dislikes=0, created_at=local_datetime)
        self.assertNotEquals(self.mymessage.user_name, self.new_message.user_name)
