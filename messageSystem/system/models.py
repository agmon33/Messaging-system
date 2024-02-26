from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)



class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    subject = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # New field to track read status

    def __str__(self):
        return f"From: {self.sender} | To: {self.receiver} | Message: {self.message}"

    class Meta:
        ordering = ['creation_date']