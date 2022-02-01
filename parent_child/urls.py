from django.urls import path
from parent_child import views

urlpatterns=[
    path('parentt/',views.parentt),
    path('childd/',views.childd),
]