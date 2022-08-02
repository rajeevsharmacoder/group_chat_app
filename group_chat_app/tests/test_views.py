from django.test import TestCase, Client
from django.contrib.auth.models import Group, User
from django.urls import reverse
from group_chat_app import models

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_user(username='admin', password='admin', email='admin@gmail.com', first_name='Admin', last_name='Chat', is_active=True, is_staff=True, is_superuser=True)
        self.user = User.objects.create_user(username='user', password='user', email='user@gmail.com', first_name='User', last_name='Chat', is_active=True, is_staff=False, is_superuser=False)
        self.group_name, self.created = Group.objects.get_or_create(name='Hello')
        self.mymessage = models.Message(message_text='Test Text Message', user_name=self.user.username, group_name=self.group_name.name, likes=0, dislikes=0)
        self.mymessage.save()
        self.mymessage = models.Message.objects.get(id=1)
        self.admin.save()
        self.user.save()
        self.user.groups.add(self.group_name)
        self.admin.groups.add(self.group_name)
        self.userlogin_url = reverse('group_chat_app:userlogin')
        self.userhome_url = reverse('group_chat_app:userhome')
        self.userlogout_url = reverse('group_chat_app:userlogout')
        self.userinfo_url = reverse('group_chat_app:userinfo', args=(self.user.username,))
        self.adduser_url = reverse('group_chat_app:adduser')
        self.updateuser_url = reverse('group_chat_app:updateuser', args=(self.user.username,))
        self.deleteuser_url = reverse('group_chat_app:deleteuser', args=(self.user.username,))
        self.adminlogin_url = reverse('group_chat_app:adminlogin')
        self.adminlogout_url = reverse('group_chat_app:adminlogout')
        self.adminhome_url = reverse('group_chat_app:adminhome')
        self.creategroup_url = reverse('group_chat_app:creategroup', args=(self.user.username,))
        self.viewgroup_url = reverse('group_chat_app:viewgroup', args=(self.group_name.name,))
        self.removemember_url = reverse('group_chat_app:removemember', args=(self.group_name.name, self.user.username))
        self.deletegroup_url = reverse('group_chat_app:deletegroup', args=(self.group_name.name, self.user.username))
        self.viewgroupmessages_url = reverse('group_chat_app:viewgroupmessages', args=(self.group_name.name,))
        self.like_url = reverse('group_chat_app:like', args=(self.mymessage.id,))
        self.dislike_url = reverse('group_chat_app:dislike', args=(self.mymessage.id,))

    def test_userlogin_GET(self):
        response = self.client.get(self.userlogin_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/userlogin.html')
    
    def test_userhome_GET(self):
        response = self.client.get(self.userhome_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/userlogin.html')

    def test_userlogin_POST(self):
        response = self.client.post(self.userlogin_url, {
            'username': self.user.username,
            'password': self.user.password
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user.username, 'user')
        self.assertTemplateUsed(response, 'group_chat_app/userlogin.html')
    
    def test_userlogout_GET(self):
        response = self.client.get(self.userlogout_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/userlogin.html')

    def test_userinfo_GET(self):
        response = self.client.get(self.userinfo_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/userlogin.html')

    def test_adduser_POST(self):
        response = self.client.post(self.adduser_url, {
            'username': self.user.username,
            'password': self.user.password,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'is_active': self.user.is_active,
            'is_staff': self.user.is_staff,
            'is_superuser': self.user.is_superuser
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user.username, 'user')
        self.assertTemplateUsed(response, 'group_chat_app/adminlogin.html')
    
    def test_updateuser_POST(self):
        response = self.client.post(self.updateuser_url, {
            'username': self.user.username
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user.username, 'user')
        self.assertTemplateUsed(response, 'group_chat_app/adminlogin.html')
    
    def test_deleteuser_POST(self):
        response = self.client.post(self.deleteuser_url, {
            'username': self.user.username
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user.username, 'user')
        self.assertTemplateUsed(response, 'group_chat_app/adminlogin.html')

    def test_adminlogin_POST(self):
        response = self.client.post(self.adminlogin_url, {
            'adminusername': self.admin.username,
            'adminpassword': self.admin.password
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.admin.username, 'admin')
        self.assertTemplateUsed(response, 'group_chat_app/adminlogin.html')
    
    def test_adminlogout_GET(self):
        response = self.client.get(self.adminlogout_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/userlogin.html')
    
    def test_adminhome_GET(self):
        response = self.client.get(self.adminhome_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/adminlogin.html')
    
    def test_creategroup_GET(self):
        response = self.client.get(self.creategroup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/creategroup.html')

    def test_creategroup_POST(self):
        response = self.client.post(self.creategroup_url, {
            'username': self.user.username,
            'groupname': self.group_name.name
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.user.username, 'user')
        self.assertTemplateUsed(response, 'group_chat_app/creategroup.html')

    # def test_viewgroup_GET(self):
    #     response = self.client.get(self.viewgroup_url)
    #     print(response.status_code)
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'group_chat_app/viewgroup.html')
    
    # def test_viewgroup_POST(self):
    #     response = self.client.post(self.viewgroup_url, {
    #         'groupname': self.group_name.name
    #     })
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'group_chat_app/viewgroup.html')    

    # def test_removemember_POST(self):
    #     response = self.client.post(self.removemember_url, {
    #         'groupname': self.group_name.name,
    #         'username': self.user.username
    #     })
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'group_chat_app/viewgroup.html')

    def test_deletegroup_POST(self):
        response = self.client.post(self.deletegroup_url, {
            'groupname': self.group_name.name,
            'username': self.user.username
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/userhome.html')
    
    def test_viewgroupmessages_GET(self):
        response = self.client.get(self.viewgroupmessages_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/viewgroupmessages.html')
    
    def test_viewgroupmessages_POST(self):
        response = self.client.post(self.viewgroupmessages_url, {
            'groupname': self.group_name.name,
            'mymessage': self.mymessage
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/viewgroupmessages.html')
    
    def test_like_POST(self):
        response = self.client.post(self.like_url, {
            'id': self.mymessage.id
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/viewgroupmessages.html')

    def test_dislike_POST(self):
        response = self.client.post(self.dislike_url, {
            'id': self.mymessage.id
        })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'group_chat_app/viewgroupmessages.html')
