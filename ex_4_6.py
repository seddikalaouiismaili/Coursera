def computepay(hours,rate):
 if hours>40.0:
  paye = rate * 40.0
  paye = paye+(1.5*rate*(hours-40))
 else:
  paye = rate*hours
 return p
hours = float(raw_input("Enter worked hours: "))
rate = float(raw_input("Enter Pay rate per hour: "))
print computepay(hours,rate)
