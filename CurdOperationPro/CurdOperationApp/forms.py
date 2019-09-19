from django import forms

class ProductInsertForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Your Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product ID'
            }
        )
    )
    product_name=forms.CharField(
        label='Enter Your Product Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Product Name'
            }
        )
    )
    product_cost=forms.FloatField(
        label='Enetr Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    product_color=forms.CharField(
        label='Enter Your Product Color',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    product_class=forms.CharField(
        label='Enter Product Class',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    customer_name=forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer name',
            }
        )
    )
    customer_email=forms.EmailField(
        label='Enter Customer Email ID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Email Id',
            }
        )
    )
    customer_mobile=forms.IntegerField(
        label='Enter Customer Mobile No.',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Mobile No.'
            }
        )
    )

class UpdateForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )
    product_cost=forms.FloatField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )

class DeleteForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )