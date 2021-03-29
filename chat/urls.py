from django.urls import include, path
from rest_framework import routers
from .views import MessageSingle, MessageCreate, MessageList

router = routers.DefaultRouter()
# router.register(r'list', MessageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path("list/<int:page>/", MessageList.as_view()),
    path("create/", MessageCreate.as_view()),
    path("single/<int:pk>/", MessageSingle.as_view()),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
