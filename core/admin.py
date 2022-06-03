from django.contrib import admin
from core.models import CommentsModel, LikesModel, AsideModel

admin.site.register(CommentsModel)
admin.site.register(LikesModel)
admin.site.register(AsideModel)
