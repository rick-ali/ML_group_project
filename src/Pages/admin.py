from django.contrib import admin

# Register your models here.

#from .models import {model}
from .models import User
from .models import FileStore
from .models import LearningPage

#admin.site.register({model})
admin.site.register(User)
admin.site.register(FileStore)
admin.site.register(LearningPage)
