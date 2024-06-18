from django.db import models
import re
import bcrypt

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        Name_REGEX = re.compile(r'^[a-zA-Z]+$')
        if len(postData['first_name']) <= 2 or not Name_REGEX.match(postData['first_name']):
            errors["first_name"] = "Name should be at least 2 characters"
        if len(postData['last_name']) <= 2:
            errors["last_name"] = "Name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        if len(postData['password']) <= 8:
            errors["password"] = "password should be at least 8 characters"
        if  postData['password'] != postData['Confirmpassword']:
            errors["Confirmpassword"] = "password didnt match"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    objects = UsersManager()
    

class Messages(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users , related_name='messages' , on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(Users , related_name='comments' , on_delete=models.CASCADE)
    message_id = models.ForeignKey(Messages , related_name='comments' , on_delete=models.CASCADE)