from django.contrib import admin
from main.models import *

class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ['/static/js/tinymce/tinymce.min.js','/static/js/textareas.js',]

admin.site.register(Blog,PostAdmin)
admin.site.register(Member)
admin.site.register(Tag)
admin.site.register(Kola_message)
admin.site.register(Test)
admin.site.register(Center_user)
