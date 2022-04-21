from django.db import models


class Mailbox(models.Model):
    host = models.CharField(max_length=200)
    port = models.IntegerField(default=465)
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email_from = models.CharField(max_length=20)
    use_ssl = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    sent = models.IntegerField(blank=True, null=True)


class Template(models.Model):
    objects: models.Manager()
    subject = models.CharField(max_length=200)
    text = models.TextField()
    attachment = models.FileField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class Email(models.Model):
    mailbox = models.ForeignKey(Mailbox, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    to = models.CharField(max_length=500)
    cc = models.CharField(max_length=500, blank=True, null=True)
    bcc = models.CharField(max_length=500, blank=True, null=True)
    reply_to = models.CharField(max_length=200, blank=True, null=True)
    sent_date = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
