from math import log

interestRate = 3
interestRateDec = interestRate/100

def calcNumPayments(loanAmount, monthlyRepayments):
    return round((log(monthlyRepayments) - log(monthlyRepayments-loanAmount*(interestRateDec/12)))/log(1+(interestRateDec/12)))

def calcMonthlyRepayments(loanAmount, numPayments):
    discountFactor = (((1 + interestRateDec/12)**numPayments - 1) / ((interestRateDec/12)*(
        (1 + interestRateDec/12) ** numPayments)))
    return round(float(loanAmount)/discountFactor,2)

def aboveThreshold():
    pass

def handleForm(loanAmount, numPayments=None, monthlyRepayments=None):
    above = False
    if not monthlyRepayments:
        monthlyRepayments = calcMonthlyRepayments(loanAmount, numPayments)
        display = "monthlyRepayments"

    elif not numPayments:
        numPayments = calcNumPayments(float(loanAmount), float(monthlyRepayments))
        display = "numPayments"

    else:
        monthlyRepaymentsCompare = calcMonthlyRepayments(loanAmount, numPayments)
        display = "threshold"
        if monthlyRepaymentsCompare < monthlyRepayments:
            above = True

    return {"numPayments": numPayments, "monthlyRepayments": monthlyRepayments, "display": display, "aboveThreshold": above, "interestRate": interestRate}

