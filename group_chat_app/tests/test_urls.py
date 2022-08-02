from django.test import SimpleTestCase
from django.urls import reverse, resolve
from group_chat_app import views

class TestUrls(SimpleTestCase):

    def test_userlogin_url_is_resolved(self):
        url = reverse('group_chat_app:userlogin')
        self.assertEquals(resolve(url).func, views.userlogin)

    def test_userhome_url_is_resolved(self):
        url = reverse('group_chat_app:userhome')
        self.assertEquals(resolve(url).func, views.userhome)
    
    def test_userlogout_url_is_resolved(self):
        url = reverse('group_chat_app:userlogout')
        self.assertEquals(resolve(url).func, views.userlogout)
    
    def test_adminlogin_url_is_resolved(self):
        url = reverse('group_chat_app:adminlogin')
        self.assertEquals(resolve(url).func, views.adminlogin)

    def test_adduser_url_is_resolved(self):
        url = reverse('group_chat_app:adduser')
        self.assertEquals(resolve(url).func, views.adduser)
    
    def test_adminhome_url_is_resolved(self):
        url = reverse('group_chat_app:adminhome')
        self.assertEquals(resolve(url).func, views.adminhome)
    
    def test_adminlogout_url_is_resolved(self):
        url = reverse('group_chat_app:adminlogout')
        self.assertEquals(resolve(url).func, views.adminlogout)
    
    def test_userinfo_url_is_resolved(self):
        url = reverse('group_chat_app:userinfo', args=('test_user',))
        self.assertEquals(resolve(url).func, views.userinfo)

    def test_updateuser_url_is_resolved(self):
        url = reverse('group_chat_app:updateuser', args=('test_user',))
        self.assertEquals(resolve(url).func, views.updateuser)
    
    def test_deleteuser_url_is_resolved(self):
        url = reverse('group_chat_app:deleteuser', args=('test_user',))
        self.assertEquals(resolve(url).func, views.deleteuser)
    
    def test_creategroup_url_is_resolved(self):
        url = reverse('group_chat_app:creategroup', args=('test_user',))
        self.assertEquals(resolve(url).func, views.creategroup)
    
    def test_viewgroup_url_is_resolved(self):
        url = reverse('group_chat_app:viewgroup', args=('test_group',))
        self.assertEquals(resolve(url).func, views.viewgroup)
    
    def test_removemember_url_is_resolved(self):
        url = reverse('group_chat_app:removemember', args=('test_group', 'test_user'))
        self.assertEquals(resolve(url).func, views.removemember)
    
    def test_deletegroup_url_is_resolved(self):
        url = reverse('group_chat_app:deletegroup', args=('test_group', 'test_user'))
        self.assertEquals(resolve(url).func, views.deletegroup)
    
    def test_viewgroupmessages_url_is_resolved(self):
        url = reverse('group_chat_app:viewgroupmessages', args=('test_group',))
        self.assertEquals(resolve(url).func, views.viewgroupmessages)
    
    def test_like_url_is_resolved(self):
        url = reverse('group_chat_app:like', args=(1,))
        self.assertEquals(resolve(url).func, views.like)
    
    def test_dislike_url_is_resolved(self):
        url = reverse('group_chat_app:dislike', args=(1,))
        self.assertEquals(resolve(url).func, views.dislike)
