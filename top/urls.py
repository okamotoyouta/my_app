from django.urls import path

from . import views

app_name = "top"

urlpatterns = [
    path('', views.UpdateList.as_view(), name='UpdateList'),
    path("<int:pk>/", views.UpdateDetailPage.as_view(), name="UpdateDetailPage"),
]
