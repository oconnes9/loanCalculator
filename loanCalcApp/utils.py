from math import log

interestRatePercent = 3
interestRateDec = interestRatePercent/100

def calcNumPayments(loanAmount, monthlyRepayments):
    return (log(monthlyRepayments) - log(monthlyRepayments-loanAmount*(interestRateDec/12)))/log(1+(interestRateDec/12))

def calcMonthlyRepayments(loanAmount, numPayments):
    discountFactor = (((1 + interestRateDec/12)**numPayments - 1) / ((interestRateDec/12)*(
        (1 + interestRateDec/12) ** numPayments)))
    return float(loanAmount)/discountFactor

def aboveThreshold():
    pass

def handleForm(loanAmount, numPayments=None, monthlyRepayments=None):
    if not monthlyRepayments:
        monthlyRepayments = calcMonthlyRepayments(loanAmount, numPayments)

    elif not numPayments:
        numPayments = calcNumPayments(float(loanAmount), float(monthlyRepayments))

    else:
        pass

    return {"numPayments": numPayments, "monthlyRepayments": monthlyRepayments}

