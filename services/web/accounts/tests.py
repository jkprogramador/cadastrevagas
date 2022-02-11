import email
from webbrowser import get
from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='doe', email='doe@email.com', password='123')
        self.assertEqual('doe', user.username)
        self.assertEqual('doe@email.com', user.email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(username='doe', email='doe@email.com', password='123')
        self.assertEqual('doe', user.username)
        self.assertEqual('doe@email.com', user.email)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)