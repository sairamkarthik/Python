# To Reverse a Number 
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
     Remainder = Number %10
     Reverse = (Reverse *10) + Remainder
     Number = Number /10
print("\n Reverse of entered number is = %d" %Reverse)
