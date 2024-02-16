from django.urls import path

from index import views

urlpatterns = [
    path('application/', views.ApplicationListCreate.as_view(), name='application-create'),
    path('application/accept/<int:application_id>/', views.send_acceptance_email_view, name='send_acceptance_email'),
    path('application/reject/<int:application_id>/', views.send_rejection_email_view, name='send_rejection_email'),
]