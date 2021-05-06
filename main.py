# Question 1
# Create variables for first and last name
Lastname = str(input("What's your last name? "))
Firstname = str(input("What's your first name? "))

#Print Lastname then Firstname
print(Lastname,Firstname)

# Question 2
#Create variable for inputed number
#If imputed number is devisible by 2, then print "That is an odd number". Else "Print that is an odd number". If imputed 0, then print "That is a 0"
Number = int(input("Type any number: "))
num = Number % 2

if Number == 0:
  print("That is a 0")

elif num > 0:
  print("That is an odd number")

else:
  print("That is an even number")

# Question 3
#Get user to input number from 1 to 365.
day = int(input("What is the day of the year? "))

#if the inputed number is equal or greater than 1 but less than 31, the month will be January of that date
if day >= 1 and day <= 31: 
  print("January, ", + day)

#if the inputed number is equal or greater than 32 but less than 59, the month will be February of that date
elif day >= 32 and day <= 59:
  print("February, ",day - 31)

#if the inputed number is equal or greater than 60 but less than 90, the month will be March of that date
elif day >= 60 and day <= 90:
  print("March, ",day - 59)

#if the inputed number is equal or greater than 93 but less than 120, the month will be April of that date
elif day >= 93 and day <= 120:
  print("April, ",day - 92)

#if the inputed number is equal or greater than 124 but less than 151, the month will be May of that date
elif day >= 124 and day <= 151:
  print("May, ",day - 123)
  
  #if the inputed number is equal or greater than 152 but less than 181, the month will be June of that date
elif day >= 152 and day <= 181:
  print("June, ",day - 151)

#if the inputed number is equal or greater than 182 but less than 212, the month will be July of that date
elif day >= 182 and day <= 212:
  print("July, ",day - 181)

#if the inputed number is equal or greater than 213 but less than 243, the month will be August of that date
elif day >= 213 and day <= 243:
  print("August, ",day - 212)

#if the inputed number is equal or greater than 244 but less than 273, the month will be September of that date
elif day >= 244 and day <= 273:
  print("September, ",day - 243)

#if the inputed number is equal or greater than 274 but less than 304, the month will be October of that date
elif day >= 274 and day <= 304:
  print("October, ",day - 273)

#if the inputed number is equal or greater than 305 but less than 334, the month will be November of that date
elif day >= 305 and day <= 334:
  print("November, ",day - 304)

#if the inputed number is equal or greater than 335 but less than 365, the month will be December of that date
elif day >= 335 and day <= 365:
  print("December, ",day - 334)

#Question 4
#create 5 coloumns
for x in range(5 + 1):
  for y in range (5, 0 + x, -1):
      print(y, end = ' ')
  print ()

#Question 5
numberline = int(input("Choose any number: "))

#create the coloumns based on imput of numberline
for x in range(numberline + 1):
  for y in range(numberline, 0 + x, -1):
      print(y, end = ' ')
  print()