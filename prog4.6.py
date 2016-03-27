def computepay(h,r):
    if	h > 40:
        OT_hours = h-40
        base_hours = float(40)
    else:
        OT_hours = float(0)
        base_hours = h

    pay = (base_hours * r) + (OT_hours * (r	 * 1.5))
    return pay
    
    
h = raw_input("Enter Hours:")
r = raw_input("Enter Rate:")

try:
    h = float(h)
except:
    print "Invalid entry for Hours."
    quit()

try:
    r=float(r)
except:
    print "Invalid entry for Rate."
    quit()


p = computepay(h,r)
print "Pay is",p