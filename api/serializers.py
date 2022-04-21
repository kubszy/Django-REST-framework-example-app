import time
from rest_framework import serializers
from api.models import Mailbox, Template, Email
import api.tasks
from django_celery_results.models import TaskResult


class MailboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailbox
        fields = ['id', 'host', 'port', 'login', 'password', 'email_from', 'use_ssl', 'is_active', 'date',
                  'last_update', 'sent']


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = ['id', 'subject', 'text', 'attachment', 'date', 'last_update']


class EmailSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        mailbox = validated_data.get('mailbox')
        if mailbox.is_active:
            template = validated_data.get('template')
            to_address = [validated_data['to']]
            if validated_data['cc']:
                to_address.append(validated_data['cc'])
            if validated_data['bcc']:
                to_address.append(validated_data['bcc'])

            port = mailbox.port
            smtp_server = mailbox.host
            sender_email = mailbox.login
            password = mailbox.password
            receiver_email = to_address
            message = f"""\
                    Subject: {template.subject}
                    {template.text}."""

            task = api.tasks.mail_send.delay(port, smtp_server, sender_email, password, receiver_email, message)
            email = Email.objects.create(**validated_data)
            time.sleep(2)
            status = TaskResult.objects.filter(task_id=task.id, status='SUCCESS').values('date_done')
            if status:
                email.sent_date = status[0]['date_done']
                email.save()
            else:
                raise Exception("The task has not been completed with the status failed!")

            return email
        else:
            raise Exception("Mailbox is not active!")

    class Meta:
        model = Email
        fields = ['id', 'mailbox', 'template', 'to', 'cc', 'bcc', 'reply_to', 'sent_date', 'date']
