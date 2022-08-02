# group_chat_app
Simple Group Chat App using Django

A simple django app to show user/admin authentication, manage groups and share messages over groups.

Before cloning the repository make sure you have python3 installed. I would suggest to first setup a virtual environment and then install Django.

Clone the repository. After cloning you will a group_chat_app folder. Go inside it and you will see a manage.py file. Make use of it to run the project by entering below command - 

On mac - 
python3 manage.py runserver 

Others - 
python manage.py runserver

App will be running on the localhost 127.0.0.1 on port 8000. Go to URL "http://127.0.0.1:8000/" and you should be on the user login page.
You might see some users already.
Make use of admin login with credentials username: "chatapp" and password: "Admin@123". You will see a few users already created.
Admin can login only as admin. User can login only as user.

NOTE: This is just a basic application and DOES NOT CONTAIN any styling or CSS. It is just some basic HTML and Python-Django framework.
