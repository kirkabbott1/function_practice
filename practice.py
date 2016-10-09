def tax(asdf):
    if gp <= 16000:
        return gp * .10
    elif gp > 16000 and gp <= 36000:
        return gp * .22
    else:
        return gp * .28

# print "enter gp: "

# print "your tax is $" + str(tax(gp))


def netpay(ehfdgadsfgasgfa):
    return gp - tax(gp)
print "enter gross pay: "
gp = int(raw_input())
print "Net pay is " + str(netpay(gp)) + " and your tax is $" + str(tax(gp))
