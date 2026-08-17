from django import forms


class CheckoutForm(forms.Form):
    phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'id': 'phone',
            'placeholder': 'Enter your phone number',
        })
    )

    address = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'address',
            'placeholder': 'Enter your address',
        })
    )

    city = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'city',
            'placeholder': 'Enter your city',
        })
    )

    postal = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'postal',
            'placeholder': 'Enter your postal code',
        })
    )

    PAYMENT_CHOICES = [
        ('card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cod', 'Cash on Delivery'),
    ]

    payment = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect
    )