'''
Create a function that randomly generates and returns a tuple of two positive one-digit integers. Then prompt the user for the multiplication of the two numbers. For example, if the generated number is 3 and 7, the prompt message is 

How much is 3 times 7? 

Then compare the user answer with the correct result. If the answer is correct, display a message “done”. Otherwise, if the user input 20, prompt:

“3 times 7 is not 20, please try again: “

Keep asking the user input until it type the correct answer.
'''

def generate_tuple():
    import random
    return (random.randint(1,9),random.randint(1,9))

def player_input(x, y):
     while True:
        player_input = input(f'What is {x} x {y} = ? ')
        if player_input.isdigit():
            return int(player_input)

def math():
    x, y = generate_tuple()
    product = x * y

    while True:
        p_input = player_input(x, y)
        if p_input == product:
            print('Done')
            break
        else:
            print(f'{x} x {y} does not equal {p_input}, please try again')

math()
