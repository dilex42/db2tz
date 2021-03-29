from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer
from rest_framework.schemas.openapi import AutoSchema

# Create your views here.


class MessageSingle(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the given message.

    put:
    Update the given message.

    patch:
    Partially update the given message.

    delete:
    Delete the given message.
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageCreate(generics.CreateAPIView):
    """
    A simple API for creating messages.
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageListSchema(AutoSchema):
    def get_operation_id(self, path, method):
        return "listMessages"


class MessageList(generics.ListAPIView):
    """
    A simple API for listing messages with pagination. 10/page.
    """

    serializer_class = MessageSerializer
    schema = MessageListSchema()

    def get_queryset(self):
        page = self.kwargs["page"]
        return Message.objects.filter(pk__gte=page * 10 + 1, pk__lte=(page + 1) * 10)
