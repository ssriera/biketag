from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def menu_dict(self):
        current_photo = PhotoEvent.objects.all().order_by('-date_found')[0]
        print current_photo

        menu = {
            'name': self.name,
            'description': self.description,
            'current_photos_user_name': current_photo.user,
            'posted_time': current_photo.date_found,
        }
        return menu


class PhotoEvent(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    user = models.ForeignKey(User)
    finding_user = models.ForeignKey(User, blank=True, null=True,
            related_name='finding_user')
    date_added = models.DateTimeField(auto_now_add=True)
    date_found = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

class PhotoHint(models.Model):
    photo = models.ForeignKey('PhotoEvent')
    hint = models.TextField(blank=True, null=True)
    time_delta = models.IntegerField(help_text='time in minutes since photo was added')

class UserPortfolio(models.Model):
    photo = models.ImageField(upload_to='userphotos/%Y/%m/%d')
