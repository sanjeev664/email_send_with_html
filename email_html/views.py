from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# Create your views here.
def mail_send(request):
    # send_mail(
    #     'hello developers',
    #     'this is pulkit madaan',
    #     'sunilrajputdev@gmail.com',
    #     ['pulkitmadaanit@gmail.com'],
        
    # )
    username = "Pulkit"
    html_message = render_to_string('mail.html', {"usernme": username})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to = 'pulkitmadaanit@gmail.com'
    email = EmailMultiAlternatives(
        "Testing",
        plain_message,
        from_email,
        [to]
    )
    email.attach_alternative(html_message, "text/html")
    email.send()
    # send_mail("subject", plain_message, from_email, [to], html_message=html_message)
    return render(request,"mail.html")