from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    body_text = models.TextField()
    #pub_date = models.DateTimeField()
    #authors = models.CharField()

    def __unicode__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.TextField()

    def __unicode__(self):
        return self.username
