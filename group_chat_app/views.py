from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from . import models
from datetime import datetime, timezone

# Create your views here.
def userlogin(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if not user.is_staff:
                    login(request, user)
                else:
                    context['message'] = f"Use Admin Login to login an admin user."
                    return render(request, 'group_chat_app/userlogin.html', context)
            else:
                context['message'] = f"Could not login the user. Invalid Credentials."
                return render(request, 'group_chat_app/userlogin.html', context)
        except Exception as e:
            print(e)
            context['message'] = f"Could not login the user due to {e} exception."
            return render(request, 'group_chat_app/userlogin.html', context)
        context['user'] = user
        context['users'] = User.objects.all()
        groups = request.user.groups.all()
        context['groups'] = groups
        return render(request, 'group_chat_app/userhome.html', context)
    return render(request, 'group_chat_app/userlogin.html', context)

def userhome(request):
    context = {}
    users = User.objects.all()
    context['users'] = users
    groups = request.user.groups.all()
    context['groups'] = groups
    context['user'] = request.user
    if not request.user.is_authenticated:
        context['message'] = f"User not logged in!"
        return render(request, 'group_chat_app/userlogin.html', context)
    if request.method == 'POST':
        pass
    return render(request, 'group_chat_app/userhome.html', context)

def userlogout(request):
    logout(request)
    context = {}
    return render(request, 'group_chat_app/userlogin.html', context)

def userinfo(request, username):
    context = {}
    if request.method == 'POST':
        pass
    user = User.objects.get(username=username)
    if not request.user.is_authenticated:
        context['message'] = f"User not logged in!"
        return render(request, 'group_chat_app/userlogin.html', context)
    context['user'] = user
    return render(request, 'group_chat_app/userinfo.html', context)

def adduser(request):
    context = {}
    # users = User.objects.all()
    # context['users'] = users
    if request.user.is_staff:
        if request.method == 'POST':
            username = request.POST['username']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            username = request.POST['username']
            password = request.POST['password']
            if request.POST.get('is_staff', False) == 'True':
                is_staff = True
            else:
                is_staff = False
            try:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname, is_active=True, is_staff=is_staff, is_superuser=False)
                user.save()
                context['message'] = f"User {username} created successfully!"
                try:
                    send_mail(
                        'You are added to Group Chat App',
                        f'You have been successfully added to Group Chat App with username {username}.',
                        'rajeevsharma2129@gmail.com',
                        [email],
                        fail_silently=False,
                    )
                except Exception as e:
                    context['message'] = f"User {username} added successfully but due to {e}, Could not send email to the user."
                users = User.objects.all()
                print(users)
                context['users'] = users
                return render(request, 'group_chat_app/adminhome.html', context)
            except Exception as e:
                context['message'] = f"Could not add user {username} due to {e}!"
                context['data'] = request.POST
                return render(request, 'group_chat_app/adduser.html', context)
        return render(request, 'group_chat_app/adduser.html', context)
    else:
        context['message'] = f"Admin not logged in!"
        return render(request, 'group_chat_app/adminlogin.html', context)

def updateuser(request, username):
    if request.user.is_staff:
        context = {}
        user = User.objects.get(username=username)
        context['data'] = user
        if request.method == 'POST':
            user = User.objects.get(username=username)
            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.email = request.POST['email']
            user.password = request.POST['password']
            if request.POST.get('is_staff', False) == 'True':
                user.is_staff = True
            else:
                user.is_staff = False
            user.save()
            user = User.objects.get(username=username)
            context['message'] = "User updated successfully"
            context['user'] = user
            return render(request, 'group_chat_app/userinfo.html', context)
        return render(request, 'group_chat_app/updateuser.html', context)
    else:
        context = {}
        context['message'] = f"Admin not logged in!"
        return render(request, 'group_chat_app/adminlogin.html', context)

def deleteuser(request, username):
    context = {}
    groups = request.user.groups.all()
    context['groups'] = groups
    if request.user.is_staff:
        if request.method == 'POST':
            user = User.objects.get(username=username)
            user.delete()
            context['message'] = f"User {username} was deleted successfully."
            context['users'] = User.objects.all()
            return render(request, 'group_chat_app/adminhome.html', context)
        user = User.objects.get(username=username)
        context['user'] = user
        return render(request, 'group_chat_app/userinfo.html', context)
    else:
        context['message'] = f"Admin not logged in!"
        return render(request, 'group_chat_app/adminlogin.html', context)

def adminlogin(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['adminusername']
        password = request.POST['adminpassword']
        try:
            adminuser = authenticate(request, username=username, password=password)
            if adminuser is not None:
                if adminuser.is_staff:
                    login(request, adminuser)
                else:
                    context['message'] = f"This is only for admins. Go to user login and try there."
                    return render(request, 'group_chat_app/adminlogin.html', context)
            else:
                context['message'] = f"Could not login the admin. Invalid Credentials."
                return render(request, 'group_chat_app/adminlogin.html', context)
        except Exception as e:
            print(e)
            context['message'] = f"Could not login the admin due to {e} exception."
            return render(request, 'group_chat_app/adminlogin.html', context)
        context['adminuser'] = adminuser
        context['users'] = User.objects.all()
        groups = request.user.groups.all()
        context['groups'] = groups
        return render(request, 'group_chat_app/adminhome.html', context)
    return render(request, 'group_chat_app/adminlogin.html', context)

def adminlogout(request):
    logout(request)
    context = {}
    return render(request, 'group_chat_app/userlogin.html', context)

def adminhome(request):
    context = {}
    users = User.objects.all()
    context['users'] = users
    groups = request.user.groups.all()
    context['groups'] = groups
    context['user'] = request.user
    if not request.user.is_authenticated:
        context['message'] = f"Admin not logged in!"
        return render(request, 'group_chat_app/adminlogin.html', context)
    if request.method == 'POST':
        pass
    if not request.user.is_staff:
        context['message'] = f"You are not an admin. Login as admin first."
        return render(request, 'group_chat_app/adminlogin.html', context)
    return render(request, 'group_chat_app/adminhome.html', context)

def creategroup(request, username):
    context = {}
    user = User.objects.get(username=username)
    users = User.objects.all()
    context['user'] = user
    context['users'] = users
    if request.method == 'POST':
        groupname = request.POST['groupname']
        group_name, created = Group.objects.get_or_create(name=groupname)
        if created:
            content_type = ContentType.objects.get_for_model(models.Message)
            post_permission = Permission.objects.filter(content_type=content_type)
            for perm in post_permission:
                group_name.permissions.add(perm)
            user.groups.add(group_name)
            user.save()
            user = get_object_or_404(User, username=username)
            context['groupname'] = group_name
            users_not_in_group = User.objects.exclude(groups=group_name).all()
            members = list(set(users) - set(users_not_in_group))
            context['non_members'] = users_not_in_group
            context['members'] = members
            return render(request, 'group_chat_app/viewgroup.html', context)
        else:
            context['message'] = "Group creation failed."
            render(request, 'group_chat_app/creategroup.html', context)
    return render(request, 'group_chat_app/creategroup.html', context)

def viewgroup(request, groupname):
    context = {}
    # user = User.objects.get(username=request.user.username)
    users = User.objects.all()
    context['user'] = request.user
    context['users'] = users
    group_name, created = Group.objects.get_or_create(name=groupname)
    context['groupname'] = group_name
    non_members = User.objects.exclude(groups=group_name).all()
    context['non_members'] = non_members
    members = list(set(users) - set(non_members))
    context['members'] = members
    if request.method == 'POST':
        user_to_be_added = request.POST['members']
        user = User.objects.get(username=user_to_be_added)
        user.groups.add(group_name)
        user.save()
        user = get_object_or_404(User, username=user_to_be_added)
        non_members = User.objects.exclude(groups=group_name).all()
        context['non_members'] = non_members
        members = list(set(users) - set(non_members))
        context['members'] = members
        return render(request, 'group_chat_app/viewgroup.html', context)
    return render(request, 'group_chat_app/viewgroup.html', context)
    
def removemember(request, groupname, username):
    group_name, created = Group.objects.get_or_create(name=groupname)
    context = {}
    user = User.objects.get(username=request.user.username)
    users = User.objects.all()
    context['user'] = user
    context['users'] = users
    context['groupname'] = group_name
    non_members = User.objects.exclude(groups=group_name).all()
    context['non_members'] = non_members
    members = list(set(users) - set(non_members))
    context['members'] = members
    if request.method == 'POST':
        user = User.objects.get(username=username)
        user.groups.remove(group_name)
        user.save()
        user = get_object_or_404(User, username=username)
        non_members = User.objects.exclude(groups=group_name).all()
        context['non_members'] = non_members
        members = list(set(users) - set(non_members))
        context['members'] = members
        return render(request, 'group_chat_app/viewgroup.html', context)
    return render(request, 'group_chat_app/viewgroup.html', context)

def deletegroup(request, groupname, username):
    group_name, created = Group.objects.get_or_create(name=groupname)
    context = {}
    user = User.objects.get(username=username)
    users = User.objects.all()
    context['user'] = user
    context['users'] = users
    context['groupname'] = group_name
    non_members = User.objects.exclude(groups=group_name).all()
    context['non_members'] = non_members
    members = list(set(users) - set(non_members))
    context['members'] = members
    if request.method == 'POST':
        user = User.objects.get(username=username)
        user.groups.remove(group_name)
        user.save()
        for member in members:
            member.groups.remove(group_name)
            member.save()
        user = get_object_or_404(User, username=username)
        non_members = User.objects.exclude(groups=group_name).all()
        context['non_members'] = non_members
        members = list(set(users) - set(non_members))
        context['members'] = members
        groups = user.groups.all()
        context['groups'] = groups
        if request.user.is_staff:
            return render(request, 'group_chat_app/adminhome.html', context)
        return render(request, 'group_chat_app/userhome.html', context)
    return render(request, 'group_chat_app/viewgroup.html', context)

def viewgroupmessages(request, groupname):
    context = {}
    group_name, created = Group.objects.get_or_create(name=groupname)
    context['groupname'] = group_name
    messages = models.Message.objects.filter(group_name=group_name)
    if messages is not None:
        context['groupmessages'] = messages
    else:
        context['message'] = "There are no messages in this group."
    if request.method == 'POST':
        text_message = request.POST['mymessage']
        utc_datetime_now = datetime.now(timezone.utc)
        local_datetime = utc_datetime_now.astimezone()
        local_datetime = local_datetime.strftime('%Y-%m-%d %H:%M:%S')
        mymessage = models.Message(message_text=text_message, user_name=request.user.username, group_name=group_name.name, likes=0, dislikes=0, created_at=local_datetime)
        mymessage.save()
        messages = models.Message.objects.filter(group_name=group_name)
        context['groupmessages'] = messages[::-1]
        render(request, 'group_chat_app/viewgroupmessages.html', context)
    return render(request, 'group_chat_app/viewgroupmessages.html', context)

def like(request, messageid):
    context = {}
    group_name, created = Group.objects.get_or_create(name=models.Message.objects.get(id=messageid).group_name)
    context['groupname'] = group_name
    messages = models.Message.objects.filter(group_name=group_name)
    if messages is not None:
        context['groupmessages'] = messages
    else:
        context['message'] = "There are no messages in this group."
    if request.method == 'POST':
        group_message = models.Message.objects.get(id=messageid)
        group_message.likes += 1
        group_message.save()
        messages = models.Message.objects.filter(group_name=group_name)
        context['groupmessages'] = messages[::-1]
        return render(request, 'group_chat_app/viewgroupmessages.html', context)

def dislike(request, messageid):
    context = {}
    group_name, created = Group.objects.get_or_create(name=models.Message.objects.get(id=messageid).group_name)
    context['groupname'] = group_name
    messages = models.Message.objects.filter(group_name=group_name)
    if messages is not None:
        context['groupmessages'] = messages
    else:
        context['message'] = "There are no messages in this group."
    if request.method == 'POST':
        group_message = models.Message.objects.get(id=messageid)
        group_message.dislikes += 1
        group_message.save()
        messages = models.Message.objects.filter(group_name=group_name)
        context['groupmessages'] = messages[::-1]
        return render(request, 'group_chat_app/viewgroupmessages.html', context)
