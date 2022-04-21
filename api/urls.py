from django.urls import path
from api import views

urlpatterns = [
    path('template/', views.TemplateList.as_view()),
    path('template/<int:pk>/', views.TemplateDetail.as_view()),
    path('mailbox/', views.MailboxList.as_view()),
    path('mailbox/<int:pk>/', views.MailboxDetail.as_view()),
    path('email/', views.EmailList.as_view()),
]
