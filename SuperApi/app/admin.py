from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Contact, Post, Sermon, Video
from django.utils.translation import ugettext_lazy



class MyAdminsite(AdminSite):
    site_title = ugettext_lazy('Supernatural Encounter')
    site_header = ugettext_lazy('Supernatural Encounter Administration')
    index_title = ugettext_lazy('Supernatural Encounter site Administration')
admin.site = MyAdminsite()

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','fullname', 'phoneNumber','email','message')


class PostAdmin(admin.ModelAdmin):
    list_display=('id','image', 'title','body','date')


class SermonAdmin(admin.ModelAdmin):
    list_display=('id','image','artist', 'name','audio','date')

class VideoAdmin(admin.ModelAdmin):
    list_display=('id','image', 'name','artist','video','date')



admin.site.register(Contact, ContactAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Sermon,SermonAdmin)
admin.site.register(Video,VideoAdmin)
