from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def menu_dict(self):
        current_photo = PhotoEvent.objects.all().order_by('-date_added')[0]
        print current_photo

        menu = {
            'name': self.name,
            'description': self.description,
            'current_photos_user_name': current_photo.user,
            'posted_time': current_photo.date_added,
            'get_absolute_url': '/%s/' % self.id
        }
        id = current_photo.photo_couch_id
        menu['photo_url'] = 'https://fdaf8a38-357f-459f-ae94-ad37be2c14db-bluemix.cloudant.com/images/%s/capture.png' % id
        if current_photo.found_photo_couch_id:
            id = current_photo.found_photo_couch_id
            menu['found_photo_url'] = 'https://fdaf8a38-357f-459f-ae94-ad37be2c14db-bluemix.cloudant.com/images/%s/capture.png' % id
        return menu


class PhotoEvent(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_couch_id = models.CharField(max_length=128, blank=True,
            null=True)
    found_photo = models.ImageField(upload_to='foundphotos/%Y/%m/%d', blank=True, null=True)
    found_photo_couch_id = models.CharField(max_length=128, blank=True,
            null=True)
    user = models.ForeignKey(User)
    finding_user = models.ForeignKey(User, blank=True, null=True,
            related_name='finding_user')
    date_added = models.DateTimeField(auto_now_add=True)
    date_found = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return u'%s: %s - %s' % (self.pk, self.date_added, self.date_found)

class PhotoHint(models.Model):
    photo = models.ForeignKey('PhotoEvent')
    hint = models.TextField(blank=True, null=True)
    time_delta = models.IntegerField(help_text='time in minutes since photo was added')

class UserPortfolio(models.Model):
    photo = models.ImageField(upload_to='userphotos/%Y/%m/%d')
