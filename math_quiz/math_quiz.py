import random


def getRandomNumber(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def getRandomOperation():
    """
    Random operation.
    """
    return random.choice(['+', '-', '*'])       

def calculate(num1, num2, operation):
    """
    calculation
    """
    p = f"{num1} {operation} {num2}"
    if operation == '+': answer = num1 + num2
    elif operation == '-': answer = num1 - num2
    else: answer = num1 * num2
    return p, answer

def math_quiz():
    """
    getting user input
    """
    s = 0
    t_q = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        try:
            num1 = getRandomNumber(1, 10);
            num2 = getRandomNumber(1, 5);
            operation = getRandomOperation()

            PROBLEM, ANSWER = calculate(num1, num2, operation)
            print(f"\nQuestion: {PROBLEM}")
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)

            if useranswer == ANSWER:
                print("Correct! You earned a point.")
                s += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
                
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
