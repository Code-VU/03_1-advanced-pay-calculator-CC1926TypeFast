def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours:")
    try:
        ival = float(hrs)
    except:
        ival = -1
    if ival < 0:
        hrs = input('Error, please enter numeric')
    
    rte = input("Enter Rate:")
    try:
        jval = float(rte)
    
    except:
        jval = -1

    if jval < 0:
        rte = input('Error, please enter numeric')
    
   

    if float(hrs) <= 40:
        pay1 = float(hrs) * float(rte)
        print("Pay:",pay1)

    elif float(hrs) > 40:
        ovr = float(hrs) - 40
        rte2 = (float(rte) * 1.5)
        pay1 = float(hrs) * float(rte)
        pay2 = (float(hrs) - ovr) * float(rte)
        pay3 = ovr * rte2
        full_pay = pay2 +pay3
        print("Pay:",full_pay)


    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
