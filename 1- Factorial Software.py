
while True:
    num1 = int(input("--->>>Enter the Number to find its Factorial--->>:"))
    num2 = num1
    for i in range(1, num1):
        fact = num2 - i
        num1 *= fact
    print(f"The Factorial of {num2} is {num1}.")
    a  = input("Enter \"q\" to Quit OR hit Enter to Continue...> ")
    if a=="q":
            break
    else:
            True


    

