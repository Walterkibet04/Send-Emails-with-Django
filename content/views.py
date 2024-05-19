from django.shortcuts import render
from .forms import EmailForm
from .models import Emails
from django.views.generic import ListView, FormView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User 
# Create your views here.

class BasicEmailView(FormView, ListView):
    template_name = 'content/home.html'
    context_object_name = 'mydata'
    model = Emails
    form_class = EmailForm
    success_url = "/"

    def form_valid(self, form):
        my_subject = "Email from our django app"
        my_recipient = form.cleaned_data['email']

        if User.objects.filter(email=my_recipient).exists()
            user =
          


        html_message = render_to_string("content/email.html")
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject = my_subject,
            body = plain_message,
            from_email = None,
            to = [my_recipient]
        )
        message.attach_alternative(html_message, "text/html")
        message.send()

        obj = Emails(
            subject = my_subject,
            message = "we have send this email",
            email = my_recipient
        )
        obj.save()
        return super().form_valid(form)
