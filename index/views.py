from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from rest_framework import generics

from index.models import Application
from index.serializers import ApplicationSerializer


class ApplicationListCreate(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


def send_acceptance_email_view(request, application_id):
    try:
        application = Application.objects.get(id=application_id)
        recipient_email = application.email
        firstname, lastname, division = application.firstname, application.lastname, application.division.title
        email_from = settings.EMAIL_HOST_USER
        subject = "Поздравляем с принятием!"
        message = f"Здравствуйте, {firstname} {lastname}!\nВы успешно приняты на позицию {division} в организацию NIC!"
        send_mail(subject, message, email_from, [recipient_email])
        return JsonResponse({'message': 'Письмо о принятии отправлено успешно'}, status=200)
    except Application.DoesNotExist:
        return JsonResponse({'error': 'Заявка с указанным ID не найдена'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def send_rejection_email_view(request, application_id):
    try:
        application = Application.objects.get(id=application_id)
        recipient_email = application.email
        firstname, lastname, division = application.firstname, application.lastname, application.division.title
        email_from = settings.EMAIL_HOST_USER
        subject = "К сожалению, Вас не приняли"
        message = f"Здравствуйте, {firstname} {lastname}!\nК сожалению, Вас не приняли на позицию {division} в организацию NIC. Попробуйте еще раз на следующем семестре!"
        send_mail(subject, message, email_from, [recipient_email])
        return JsonResponse({'message': 'Письмо о отклонении отправлено успешно'}, status=200)
    except Application.DoesNotExist:
        return JsonResponse({'error': 'Заявка с указанным ID не найдена'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
