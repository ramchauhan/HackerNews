from django import forms


class FibonacciInputForm(forms.Form):
    """
    From for Fibonacci input
    """
    input_number = forms.IntegerField(label='Input the Number')
