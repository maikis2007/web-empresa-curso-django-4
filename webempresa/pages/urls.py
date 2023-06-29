from django.urls import path
from pages import views

urlpatterns = [
    path('<int:page_id>/', views.page, name="page"),
    path('<int:page_id>/<slug:page_title>', views.page, name="page"),
]
