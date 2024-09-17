import sys

# Main program functions

def header():
    ''' This function simply prints the header information and menu of the program '''
    print('Simple Calculator v 1.1 \n=======================')
    print('\n Select Operation:')
    print(' 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division')

def user_input():
    ''' This function takes the user's input for operation selection '''
    usrval = input('Select your operation: ')
    return usrval

def main():
    ''' This function processes the user's choice and performs the corresponding calculation '''
    value = user_input()
    
    if value == '1':
        result = addition()
        print(f"The sum is: {result}")
    
    elif value == '2':
        result = subtraction()
        print(f"The difference is: {result}")
    
    elif value == '3':
        result = multiplication()
        print(f"The product is: {result}")
    
    elif value == '4':
        result = division()
        print(f"The quotient is: {result}")
    
    else:
        print('Invalid operation')

def exit_loop():
    ''' Function to determine if the user wants to restart or exit '''
    print('')
    dec = input('Would you like to do another calculation? (Y/N): ')
    
    if dec == 'Y' or dec == 'y':
        header()
        main()
        exit_loop()  # Recursively call exit_loop() to allow the user to continue or exit
    elif dec == 'N' or dec == 'n':
        print('The program will now terminate!')
        sys.exit()  # Exit the program
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        exit_loop()  # Ask again if the input is invalid

# Defining operator methods    

def addition():
    ''' This function takes two numbers and returns their sum '''
    a = float(input('Enter number 1: '))
    b = float(input('Enter number 2: '))
    return a + b

def subtraction():
    ''' This function takes two numbers and returns their difference '''
    a = float(input('Enter number 1: '))
    b = float(input('Enter number 2: '))
    
    if a > b:
        return a - b
    else:
        return b - a

def multiplication():
    ''' This function takes two numbers and returns their product '''
    a = float(input('Enter number 1: '))
    b = float(input('Enter number 2: '))
    return a * b

def division():
    ''' This function takes two numbers and returns their quotient '''
    a = float(input('Enter number 1: '))
    b = float(input('Enter number 2: '))
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero is impossible."

# Call header and main to run the program
header()
main()
exit_loop()
