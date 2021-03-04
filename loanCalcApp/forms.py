from django import forms

class CalcForm(forms.Form):
    loanAmount = forms.DecimalField(label='Loan Amount (€)', min_value=100, decimal_places=2, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'This field is required'}))
    numPayments = forms.IntegerField(label='Number of Monthly Repayments', min_value=1, max_value=600, required=False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    monthlyRepayment = forms.DecimalField(label='Monthly Repayment Amount (€)', min_value=1, decimal_places=2, required=False, widget=forms.NumberInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super(CalcForm, self).clean()
        numPayments = cleaned_data.get("numPayments")
        monthlyRepayment = cleaned_data.get("monthlyRepayment")

        if not numPayments and not monthlyRepayment and not self.errors:  #Do not want this error to arise when a number has been entered but is not saved to the form due to previous form field validation error.
            raise forms.ValidationError("Number of Repayments and Monthly Repayment Amount cannot both be left blank.")

        return cleaned_data