#Task 1
# #1.1
# arr = [4, 8, 15, 16, 23, 42]
# print(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])

#1.2
# print(f'4','\n8', '\n15', '\n16', '\n23', '\n42')

# # 1.3
# try:
#    a = int(input())
#    b = a + 1
#    c = a + 2
#    print(b)
#    print(c)
#    print(a)
# except ValueError:
#    print('Wrong Input')


# #1.4
# try:
#    a = int(input())
#    b = int(input())
#    c = int(input())
#    print(a + b + c)
# except ValueError:
#    print('Wrong Input')

# # 1.5
# try:
#    a = int(input())
#    vol = a**3
#    S = 6 * a**2
#    print(f'Volume = ', vol)
#    print(f'Total surface area = ', S)
# except ValueError:
#    print('wrong input')
#Task 2
# # #2.1
# try:
#    n = int(input())
#    k = int(input())
#    get = k // n
#    remain = k % n
#    print(get)
#    print(remain)
# except ValueError:
#    print('wrong input')
# #2.2
# try:
#    number = int(input("Enter a four-digit number: "))
#    if 10000 <= number <= 99990:
#       thousandsdasda = number // 10000
#       thousands = (number // 1000) % 10
#       hundreds = (number // 100) % 10
#       tens = (number // 10) % 10
#       ones = number % 10
#       print("The digit in the thousandsdsadsa position is", thousandsdasda)
#       print("The digit in the thousands position is", thousands)
#       print("The number in the hundreds position is", hundreds)
#       print("The digit in the tens position is", tens)
#       print("The digit in the position of units is", ones)
#    else:
#       print("Invalid input. Please enter a four-digit number.")
# except ValueError:
#    print('wrong input')
# # #2.3  
# try:
#    import math
#    n = int(input())
#    print(math.ceil(n/2))
# except ValueError:
#    print('wrong input')
# 2.4
try:
   n = int(input())
   if (n == 0) :
      print('Error')
   else :
      print(f'The result of << is ', (2)**n)
except ValueError:
   print('wrong input')
#2.5
try:
   print(f"Please enter the first number: " )
   a = int(input())
   print(f"Please enter the second number: " )
   b = int(input())
   print(f"Please choose the operation (+, -, *, /): ")
   operation = str(input())
   match operation:
      case "+": 
         print(a + b)
      case "-":
         print(a - b)
      case "*":
         print(a * b)
      case "/":
         print(a / b)
except ValueError:
   print('wrong input')
except ZeroDivisionError:
   print('error')
