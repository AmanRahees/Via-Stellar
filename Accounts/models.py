from django.db import models
from django.contrib.auth.models import User


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profiles/',default='profiles/default.png')
    about = models.CharField(max_length=200, default='Available')
    status = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user

class Friends(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_friends_with')

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_messages')
    content = models.TextField()
    time_shared = models.DateTimeField(auto_now_add=True)

class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared_media')
    file = models.FileField(upload_to='shared_medias')
    time_shared = models.DateTimeField(auto_now_add=True)