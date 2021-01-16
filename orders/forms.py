from django import forms


class OrderForm(forms.Form):
    """
    Form for order information, incl. type of payment and delivery address
    """

    payment_type_list= [
        ('online', 'online'),
        ('cash', 'cash'),
        ]
    payment_type = forms.ChoiceField(choices=payment_type_list,
                                     label='Payment type',
                                     widget=forms.RadioSelect(
                                         attrs={
                                             'class': 'form-check-input',
                                         }
                                     ),
                                     required=True)
    phone = forms.CharField(max_length=128,
                            label='Phone to contact',
                            widget=forms.TextInput(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder': '+7(999) 123-45-67',
                            }),
                            required=True)

    info = forms.CharField(widget=forms.TextInput(attrs={
                                                 'class': 'form-control'
                                                        }
                                                 ),
                           label='Additional information',
                           required=False)
    contact_person = forms.CharField(max_length=128,
                                     label='Person to contact',
                                     widget=forms.TextInput(
                                         attrs={
                                             'class': 'form-control',
                                             'placeholder': 'John Smith',
                                         }

                                     ),
                                     required=False)
    delivery_address = forms.CharField(max_length=128,
                                       label='Delivery address',
                                       widget=forms.TextInput(
                                           attrs=
                                           {
                                               'class': 'form-control',
                                               'placeholder': 'Saint-Petersburg, blvrd. Golovnina, 10',
                                           }
                                       ),
                                       required=False)
    delivery_type_list= [
        ('pick-up', 'pick-up'),
        ('delivery', 'delivery'),
        ]
    delivery_type = forms.ChoiceField(choices=delivery_type_list,
                                     label='Delivery type',
                                     widget=forms.RadioSelect(
                                         attrs={
                                             'class': 'form-check-input',
                                         }
                                     ),
                                     required=True)