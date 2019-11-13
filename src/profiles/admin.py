from django.contrib import admin

from .models import Profile, Education, Experience, Social


class ProfileAdmin(admin.ModelAdmin):
  list_display = [
    'user', 'status', 'profession', 'company', 'location', 'created_at'
  ]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Social)
