from django.urls import path
from staticapp import views

urlpatterns=[
    path('mark/',views.mark),

]