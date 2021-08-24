from django.conf.urls import url
from django.urls import path
from spreedsheet import views

urlpatterns = [
    path('api/spreedsheet/<str:string>', views.column_number)
]