medcause=input("Did you have a medical cause for missing the classes? Y or N")
attendence=int(input("enter the attendence "))
if medcause=="Y" :
    print ("allowed")
else :
    if attendence>=75 :
        print ("allowed")
    else :
        print("not allowed")