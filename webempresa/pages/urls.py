from django.urls import path
from . import views as pages_views

urlpatterns = [
    path('<int:page_id>/', pages_views.page, name="sample"),
]