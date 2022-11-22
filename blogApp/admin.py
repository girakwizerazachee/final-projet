# from xml.etree.ElementTree import Comment
from django.contrib import admin
from blogApp.models import Blog, Comment
# from django.contrib.auth.models import Group
# Register your models here.
admin.site.register(Blog)
admin.site.register(Comment)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     def has_module_permission(self, request) :
#         q=Group.objects.get(name='blogers')
#         if request.user.is_authenticated() :
#             if request.user in q.use
#         return super().has_module_permission(request)