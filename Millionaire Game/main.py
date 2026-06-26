questions = [
    ["What is the output of type([]) in Python?", "<class 'list'>", "<class 'array'>", "<class 'tuple'>", "<class 'dict'>", 1],
    ["Which keyword is used to define a function in Python?", "func", "def", "define", "function", 2],
    ["What does len('hello') return?", "4", "5", "6", "Error", 2],
    ["Which of these is an immutable data type in Python?", "List", "Dictionary", "Tuple", "Set", 3],
    ["What is the correct way to create a lambda function?", "lambda = x: x+1", "lambda x: x+1", "def lambda(x): x+1", "func x: x+1", 2],
    ["What does the 'self' keyword refer to in a class?", "The parent class", "The current module", "The current object instance", "The constructor", 3],
    ["Which method is used to add an element at the end of a list?", "add()", "insert()", "append()", "extend()", 3],
    ["What is the output of bool(0) in Python?", "True", "False", "None", "Error", 2],
    ["Which of these is used to handle exceptions in Python?", "try-catch", "try-except", "try-handle", "try-error", 2],
    ["What does the 'pass' statement do in Python?", "Exits the loop", "Skips current iteration", "Does nothing, acts as placeholder", "Returns None", 3],
]

prizes = [100000, 320000, 400000, 450000, 500000, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000]

i = 0
for question in questions:
    print(question[0])
    print(f'a. {question[1]}')
    print(f'b. {question[2]}')
    print(f'c. {question[3]}')
    print(f'd. {question[4]}')

    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d\n"))

    if question[5] == a:
        print('Correct Answer!')
    else:
        print(f"Incorrect! The correct answer was option {question[5]}")
        print("Better luck next time!")
        break

    print(f"You won ₹{prizes[i]}")  
    i += 1                          
