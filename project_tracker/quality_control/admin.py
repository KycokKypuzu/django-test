# Register your models here.
from django.contrib import admin
from .models import BugReport, FeatureRequest


@admin.action(description="Change bug status to New")
def change_status_new(modeladmin, request, queryset):
    queryset.update(status="New")


@admin.action(description="Change bug status to In progress")
def change_status_in_progress(modeladmin, request, queryset):
    queryset.update(status="In_progress")


@admin.action(description="Change bug status to Completed")
def change_status_completed(modeladmin, request, queryset):
    queryset.update(status="Completed")


# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')
    fieldsets = [
        (
            None,
            {
                "fields": ['title', 'description', 'project', 'task', 'status', 'priority']
            },
        ),
    ]
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    actions = [change_status_new, change_status_in_progress, change_status_completed]
    # filter_horizontal = ('title',)
    # ordering = ('created_at',)
    # date_hierarchy = 'created_at'

    # Подключение inline для BugReport
    # inlines = [BugReportInline]


# Класс администратора для модели Task
@admin.register(FeatureRequest)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'project')
    search_fields = ('title', 'description')
    fieldsets = [
        (
            None,
            {
                "fields": ['title', 'description', 'project', 'task', 'status', 'priority']
            },
        ),
    ]
    list_editable = ('status', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    # list_editable = ('status', 'assignee')
    # readonly_fields = ('created_at', 'updated_at')
