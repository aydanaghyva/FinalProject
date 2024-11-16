from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from .models import Employee, User
from datetime import timedelta
from django.utils import timezone
from django.core.mail import EmailMessage

import logging
logger = logging.getLogger(__name__)

@shared_task
def notify_active_employees_not_registered():
     logger.info("Running periodic task: notify_active_employees_not_registered")
     print("Task `notify_active_employees_not_registered` is being executed.")   

#     # Get the datetime from exactly 2 days ago
     two_days_ago = timezone.now() - timedelta(days=2)
 #    Fetch active employees created 2 or more days ago who are not in the User table
     active_employees = Employee.objects.filter(
         created_at__lte=two_days_ago, status='active'  # Use 'lte' to include employees created exactly 2 days ago
     ).exclude(email__in=User.objects.values_list('email', flat=True))

     for employee in active_employees:
        # Send an email notification
        email_body_message=f'Dear {employee.name}, please register to complete your profile.'
        email = EmailMessage(
         subject='Registration Reminder',
         #body='Dear User, please register to complete your profile.',
          body=email_body_message,
         from_email=settings.DEFAULT_FROM_EMAIL,
         to=[employee.email],  # Replace with your recipient's email
         )
        email.send()

        print(f'--------------Notification sent to {employee.name} {employee.surname} (Email: {employee.email})')
