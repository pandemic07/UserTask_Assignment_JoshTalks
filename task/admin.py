from django.contrib import admin
from .models import TaskUser, Task


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "mobile", "is_active", "is_staff", "date_joined")
    search_fields = ("username", "email", "mobile")
    list_filter = ("is_active", "is_staff")
    ordering = ("id",)


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "task_type", "status", "get_assigned_users")
    search_fields = ("name", "description")
    list_filter = ("status", "task_type", "created_at")
    ordering = ("-created_at",)

    def get_assigned_users(self, obj):
        return ", ".join([user.username for user in obj.assigned_users.all()])

    get_assigned_users.short_description = "Assigned Users"


admin.site.register(TaskUser, UserAdmin)
admin.site.register(Task, TaskAdmin)
