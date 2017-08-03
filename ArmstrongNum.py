def isArm(value):
   sum = 0
   num = value
   order = len ('' + str(value))
   while num  != 0:
     sum = sum + (num%10)**(order)
     num = num //10
   if sum == value:
     print( value,'is a Armstrong number of order',order)
   else:
     print('False')


isArm(120)