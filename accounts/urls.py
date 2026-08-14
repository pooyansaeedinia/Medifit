from django.urls import path

from accounts.views import *
app_name = 'accounts'

urlpatterns = [
    path('', login_signup_view, name='login_signup'),
    path('logout/', logout_view, name='logout'),
    path('check-email/', check_email_template, name='check_email'),
    path('verify-email/<uidb64>/<token>/', verify_email, name='verify_email'),
    path('email-verification-successful/', email_verification_successful, name='email_verification_successful'),
    path('email-verification-failed/', email_verification_failed, name='email_verification_failed'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDone.as_view(), name='password_reset_done'),
    path('password-reset/complete/', PasswordResetComplete.as_view(), name='password_reset_complete'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirm.as_view(), name='password_reset_confirm'),
]
