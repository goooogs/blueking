from django.contrib import admin

from .models import ConnectionInfo, StorageRegistry
# Register your models here.


admin.site.register([ConnectionInfo, StorageRegistry])
