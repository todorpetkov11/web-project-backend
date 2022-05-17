from django.contrib import admin
from core.models import CommentsModel, LikesModel

admin.site.register(CommentsModel)
admin.site.register(LikesModel)
