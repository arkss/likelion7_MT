from django.contrib import admin
from .models import Member,Profile, Mission
from django.utils.safestring import mark_safe



@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'managerFlag', 'manitoFlag']


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'flag']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'team', 'manito', 'mission' ]

    def username(self, profile):
        return profile.user.username
    username.short_description = "이름"