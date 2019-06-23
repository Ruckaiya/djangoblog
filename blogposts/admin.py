from django.contrib import admin

from .models import NewPost, LatestPost, Popular

admin.site.register(NewPost)
admin.site.register(LatestPost)
admin.site.register(Popular)