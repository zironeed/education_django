from django.urls import path
from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserConfirmationSentView, UserConfirmEmailView, \
    UserConfirmedView, NewPasswordView, DoneNewPasswordView, UserResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm_your_email/', UserConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm_email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email_confirmed/', UserConfirmedView.as_view(), name='email_confirmed'),

    path('password_forgot/', NewPasswordView.as_view(), name='password_forgot'),
    path('password_forgot/notification/', DoneNewPasswordView.as_view(), name='password_notification'),
    path('password/reset/<uidb64>/<token>/', UserResetConfirmView.as_view(), name='password_reset_confirm'),


]
