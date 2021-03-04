from math import log

interestRate = 3
interestRateDec = interestRate/100

def calcNumPayments(loanAmount, monthlyRepayments):
    return round((log(monthlyRepayments) - log(monthlyRepayments-loanAmount*(interestRateDec/12)))/log(1+(interestRateDec/12)))

def calcMonthlyRepayments(loanAmount, numPayments):
    discountFactor = (((1 + interestRateDec/12)**numPayments - 1) / ((interestRateDec/12)*(
        (1 + interestRateDec/12) ** numPayments)))
    return round(float(loanAmount)/discountFactor,2)

def handleForm(loanAmount, numPayments=None, monthlyRepayments=None):
    warning = False  #Used to change colour of text to red if above interest threshold.
    if not monthlyRepayments:
        monthlyRepayments = calcMonthlyRepayments(loanAmount, numPayments)
        display = f"Monthly Repayment Amount = €{monthlyRepayments}"

    elif not numPayments:
        numPayments = calcNumPayments(float(loanAmount), float(monthlyRepayments))
        display = f"Number of Repayments = {numPayments}"

    else:
        monthlyRepaymentsCompare = calcMonthlyRepayments(loanAmount, numPayments)  #Calculated monthly repayments with "our" interest rate
        if monthlyRepaymentsCompare < monthlyRepayments:  #If that is less than the monthly repayments entered, the interest rate is above ours.
            warning = True
            display = f"The interest rate is above the threshold of {interestRate}%"
        else:
            display = f"The interest rate is below the threshold of {interestRate}%"

    return {"display": display, "warning": warning}

