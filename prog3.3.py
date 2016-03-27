score = raw_input("Enter Score between 0.0 and 1.0:")

try:  
   test = float(score)  
except:  
   print "Invalid entry."
   quit()

score = float(score)

if score > 1.0:
   print "Invalid entry."
   quit()
elif score < 0.0:
   print "Invalid entry."
   quit()
elif score >= 0.9:
	print 'A'
elif score >= 0.8:
	print 'B'
elif score >= 0.7:
	print 'C'
elif score >= 0.6:
	print 'D'
else:
	print 'F'
   