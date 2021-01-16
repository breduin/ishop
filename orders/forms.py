from django import forms


class OrderForm(forms.Form):
    """
    Form for order information, incl. type of payment and delivery address
    """

    payment_type= [
        ('cash', 'cash'),
        ('online', 'online'),
        ]