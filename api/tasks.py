import smtplib
import ssl
from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger('celery.tasks')


@shared_task(bind=True, max_retries=3, default_retry_delay=30)
def mail_send(self, port, smtp_server, sender_email, password, receiver_email, message):
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            return server.sendmail(sender_email, receiver_email, message)
    except Exception as err:
        if self.request.retries >= self.max_retries:
            logger.error(f'Error: {err}')
            return False
        raise self.retry(exc=err)

