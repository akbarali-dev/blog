from django.test import TestCase
from datetime import date

from about.models import Location
from blog.models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        phone = '123566'
        location = Location.objects.create(name="Tashkent", link="xajsdsdesfishdr")
        User.objects.create(phone=phone, birth_date=date(1949, 1, 1),
                            email='sadsejfi', job_name='web',
                            image='/axsaxj/xasx', location=location)

    def test_saving_data(self):
        user = User.objects.first()
        print(user)
        self.assertEqual('123566', user.phone)
        # self.assertTrue(True)
