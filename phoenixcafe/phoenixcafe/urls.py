#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('welcome/', views.welcome),
    # your custom path will be here
]

# NEW - Add this to the end of your code
# clock/ is the path to trigger our function    
urlpatterns += [path('clock/', views.current_datetime),]
#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('welcome/', views.welcome),
]

