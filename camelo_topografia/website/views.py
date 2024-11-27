from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Renderiza o arquivo HTML

from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings

def send_email(request):
    if request.method == 'POST':
        try:
            # Captura os dados enviados pelo formulário
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')

            # Cria o corpo do e-mail com as informações do remetente
            email_message = f"""
            Nome: {name}
            E-mail: {email}

            Mensagem:
            {message}
            """

            # Envia o e-mail para o destinatário (você)
            send_mail(
                f'Nova mensagem de {name}',  # Assunto
                email_message,               # Corpo da mensagem
                email,                        # E-mail de quem está enviando
                [settings.EMAIL_HOST_USER],  # Para quem vai o e-mail
                fail_silently=False,
            )

            return JsonResponse({'status': 'success', 'message': 'E-mail enviado com sucesso!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Erro ao enviar o e-mail: {str(e)}'})

    return JsonResponse({'status': 'error', 'message': 'Método de requisição inválido'})
