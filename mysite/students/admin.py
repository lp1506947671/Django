from django.contrib import admin

# Register your models here.
from students.models import Student

admin.site.site_header = '后台管理系统'
admin.site.site_title = '后台管理系统MIS'
admin.site.index_title = '欢迎使用后台管理系统'


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ['id', "name", "pub_date"]
    search_fields = ['name']
    # fields = ['name']
    fieldsets = (("基本", {"fields": ["name"]}), ('高级', {
        'fields': ["sex", "age", "class_num", "description"],
        'classes': ('collapse',)
    }))
