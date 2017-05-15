import unittest, datetime
from django.core.urlresolvers import reverse
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.template import Template, Context
from views import *

class exosProjClassBasedViewsTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_list_view(self):
        # Setup the request/response
        request = self.factory.get(reverse('user_list'))
        response = UserList.as_view()(request)

        # Test return code
        self.assertEqual(response.status_code, 200)

        # Render the template
        response.render()
        self.assertIn('There are no users in the system.',response.content)


    def test_detail(self):
        # Setup the request/response
        request = self.factory.get(reverse('user_detail',kwargs={'pk':1}))

        # Test without a user in the database
        try:
            response = UserDetail.as_view()(request,pk=1)
        except Exception as e:
            self.assertIn('No user found matching the query',e)

        # Add a user
        user = User(username='mike')
        user.save()
 
        response = UserDetail.as_view()(request,pk=2)

        # Test return code
        self.assertEqual(response.status_code, 200)

        # Render the template
        response.render()
        self.assertIn('mike',response.content)


    def test_create(self):
        # Setup the request/response
        request = self.factory.get(reverse('user_create'))

        response = UserCreate.as_view()(request)

        # Test return code
        self.assertEqual(response.status_code, 200)

        # Render the template and test for the blank form
        response.render()
        self.assertIn('<input id="id_password" maxlength="128" name="password" type="text" />',response.content)

    def test_update(self):
        # Setup the request/response
        request = self.factory.get(reverse('user_update',kwargs={'pk':1}))

        # Test without a user in the database
        try:
            response = UserUpdate.as_view()(request,pk=1)
        except Exception as e:
            self.assertIn('No user found matching the query',e)

        # Add a user
        user = User(username='mike')
        user.save()

        response = UserUpdate.as_view()(request,pk=3)

        # Test return code
        self.assertEqual(response.status_code, 200)

        # Render the template
        response.render()
        self.assertIn('mike',response.content)


    def test_delete(self):
        # Setup the request/response
        request = self.factory.get(reverse('user_delete',kwargs={'pk':1}))

        try:
            response = UserDelete.as_view()(request,pk=1)
        except Exception as e:
            self.assertIn('No user found matching the query',e)

        # Add a user
        user = User(username='mike')
        user.save()

        response = UserDelete.as_view()(request,pk=1)

        # Test return code
        self.assertEqual(response.status_code, 200)

        # Render the template
        response.render()
        self.assertIn('mike',response.content)

    
    def tearDown(self):
        users = User.objects.all()
        for user in users:
            user.delete() 




class TemplateTagsTest(unittest.TestCase):

    TEMPLATE = Template("{% load exos_extras %}Mike is {% is_eligible birthday %}!! {% bizz_fuzz random_num %}")

    def test_different_dates_and_rand(self):
        # Test with someone old enough AND a random_num that is divisible by 3 and 5
        rendered = self.TEMPLATE.render(Context({'birthday':datetime.date(1975,9,29),'random_num':15}))
        self.assertIn('Mike is allowed!! BizzFuzz', rendered)

        # Test with someone not old enough AND a random_num that is divisible by 3 only
        rendered = self.TEMPLATE.render(Context({'birthday':datetime.date(2004,9,29),'random_num':12}))
        self.assertIn('Mike is blocked!! Bizz', rendered)

        # Test with someone not old enough AND a random_num that is divisible by 5 only
        rendered = self.TEMPLATE.render(Context({'birthday':datetime.date(1975,9,29),'random_num':20}))
        self.assertIn('Mike is allowed!! Fuzz', rendered)

        # Test with someone old enough AND a random_num that is not divisible by 5 or 3
        rendered = self.TEMPLATE.render(Context({'birthday':datetime.date(1975,9,29),'random_num':16}))
        self.assertIn('Mike is allowed!! 16', rendered)

