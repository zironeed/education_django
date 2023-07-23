from django.contrib.auth.views import LoginView as BaseLogin
from django.contrib.auth.views import LogoutView as BaseLogout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.views import View

from users.forms import UserForm
from users.models import User

from catalog.utils import sendmail
from users.utils import password_generator

import config.settings
import random


class TitleMixin(object):
    title = None


class LoginView(TitleMixin, BaseLogin):
    template_name = 'users/login.html'
    title = 'Логин'


class LogoutView(BaseLogout):
    pass


class RegisterView(TitleMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog:product_list')
    title = 'Регистрация'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.save()

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy('users:confirm_email', kwargs={'uidb64': uid, 'token': token})
        current_site = config.settings.SITE_NAME

        sendmail(
            user.email,
            "Регистрация на сайте",
            f"Подтвердите свой e-mail адрес: http://{current_site}{activation_url}"
        )
        return redirect('users:email_confirmation_sent')


class UserConfirmationSentView(PasswordResetDoneView):
    template_name = "users/registration_sent.html"


class UserConfirmEmailView(View):

    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('users:email_confirmed')


class UserConfirmedView(TitleMixin, TemplateView):
    template_name = 'users/registration_confirm.html'
    title = "Почта активирована!"


class UserResetView(PasswordResetView):
    template_name = "users/reset/password_reset_form.html"
    email_template_name = "users/reset/password_reset_email.html"
    success_url = reverse_lazy('users:password_reset_done')


class UserResetDoneView(PasswordResetDoneView):
    template_name = "users/reset/password_reset_done.html"


class UserResetConfirmView(PasswordResetConfirmView):
    template_name = "users/reset/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")


class UserResetCompleteView(PasswordResetCompleteView):
    template_name = "users/reset/password_reset_complete.html"


def generate_password(request):
    new_password = password_generator()
    sendmail(request.user.email, "Замена пароля на сайте Skyfarm", new_password)
    request.user.set_password(new_password)
    request.user.save()

    return render(request, 'users/reset/reset_complete.html')
