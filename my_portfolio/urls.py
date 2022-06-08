from django.urls import path

from .views import detail_project, home

app_name = 'my_portfolio'

urlpatterns = [
    path('',home, name = "projects"),
    path("<int:projects_id>", detail_project , name = "detail_project" )
]