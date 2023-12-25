from django.urls import path, include

# import your views files, so you can use view functions
from . import views

urlpatterns = [
    # regist url paths to this app
    path("", views.employee_form),
    path("list/", views.employee_list),
]