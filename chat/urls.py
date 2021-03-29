from django.urls import path
from .views import MessageSingle, MessageCreate, MessageList

urlpatterns = [
    path("list/<int:page>/", MessageList.as_view()),
    path("create/", MessageCreate.as_view()),
    path("single/<int:pk>/", MessageSingle.as_view()),
]
