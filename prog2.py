hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")

h = float(hrs)
rate=float(rate)

if	h > 40:
	OT_hours = h-40
	base_hours = float(40)
else:
	OT_hours = float(0)
	base_hours = h

pay = (base_hours * rate) + (OT_hours * (rate * 1.5))
print pay