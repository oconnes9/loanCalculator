from django import forms

class CalcForm(forms.Form):
    loanAmount = forms.DecimalField(label='Loan Amount', decimal_places=2, widget=forms.NumberInput)
    numPayments = forms.IntegerField(label='Number of Repayments', max_value=600, required=False, widget=forms.NumberInput)
    monthlyRepayment = forms.DecimalField(label='Monthly Repayment Amount', required=False, widget=forms.NumberInput)