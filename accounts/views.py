from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.urls import reverse_lazy
from django.contrib.sites.shortcuts import get_current_site

from MEDIFIT.settings import EMAIL_HOST_USER
from .forms import PasswordResetSetForm, SignUpForm
    
        
def login_signup_view(request):
    login_form = AuthenticationForm(request)
    signup_form = SignUpForm()

    if request.method == 'POST':
        form_type = request.POST.get("form_type")

        if form_type == 'login':
            print("the form is logged in")

            login_form = AuthenticationForm(request, data=request.POST)

            if login_form.is_valid():
                print("the form is valid")

                user = login_form.get_user()
                login(request, user)

                messages.success(request, "You are now logged in")
                return redirect('home:home')

            else:
                print(login_form.errors)

        elif form_type == 'signup':
            signup_form = SignUpForm(request.POST)

            if signup_form.is_valid():
                print("Signup form is valid")

                user = signup_form.save(commit=False)
                user.is_active = False
                user.save()

                print("User saved:", user)

                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                domain = get_current_site(request).domain
                link = reverse(
                    'accounts:verify_email',
                    kwargs={'uidb64': uid, 'token': token}
                )

                verify_url = f'http://{domain}{link}'

                send_mail(
                    subject="Activate Your Account",
                    message=f"Click the link below to activate your account:\n{verify_url}",
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=False,
                )

                return redirect('accounts:check_email')

            else:
                print(signup_form.errors)

    context = {
        'login_form': login_form,
        'signup_form': signup_form,
    }

    return render(
        request,
        'accounts/login-signup.html',
        context
    )


def check_email_template(request):
    return render(request, "accounts/check-email.html")


User = get_user_model()


def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activated.")
        return redirect("accounts:email_verification_successful")

    else:
        messages.error(request, "Activation link is invalid.")
        return redirect("accounts:email_verification_failed")
    

def email_verification_successful(request):
    return render(request, "accounts/check_email_successfull.html")


def email_verification_failed(request):
    return render(request, "accounts/check_email_failed.html")


def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home:home')


class CustomPasswordResetView(PasswordResetView):
    template_name = "accounts/forgot-password.html"
    email_template_name = "accounts/password_reset_email.html"
    subject_template_name = "accounts/password_reset_subject.txt"
    success_url = reverse_lazy("accounts:password_reset_done")
    from_email = EMAIL_HOST_USER


class PasswordResetDone(PasswordResetDoneView):
    template_name = "accounts/password-reset-check-email.html"


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = "accounts/password-reset-process.html"
    form_class = PasswordResetSetForm
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = "accounts/password-reset-complete.html"

    


