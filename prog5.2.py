largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    
    #is the user trying to exit the loop?
    if num == "done" : break
    
    #make sure we have an integer
    try:
        smallest = int(num)
    except:
        print "Invalid input"
        continue 
        
    if num > largest    : largest = num
    if num < smallest   : smallest = num
    
print "Maximum is", largest
print "Minimum is", smallest