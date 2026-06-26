try:
    a = float(input('Enter the first number:'))
    b = float(input('Enter the second number:'))

    print('What kind of operation do you want to perform.\nPress + for addition.\nPress - for substration.\nPress * for multiplication.\nPress / for division.')

    o = input('Operator:')
    match o: # It's just a cleaner replacement for multiple if-elif-else.  
        case "+":
            print(f'The result is {a + b}')
        
        case "-":
            print(f'The result is {a - b}')
        
        case "*":
            print(f'The result is {a * b}')

        case "/":
            print(f'The result is {a / b}')  

        case default:
            print(f'There was an error')

except Exception as e:
    print('Enter a valid value of a and b')  
