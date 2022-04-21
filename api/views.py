from api.models import Template, Mailbox, Email
from api.serializers import MailboxSerializer, TemplateSerializer, EmailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
import logging
logger = logging.getLogger('django')


class MailboxList(generics.ListCreateAPIView):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_active', 'id']


class MailboxDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mailbox.objects.all()
    serializer_class = MailboxSerializer


class TemplateList(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class TemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer


class EmailList(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']


