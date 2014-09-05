import math
def eval_loop():
    while True:
        user_input = input('murugavel>> ')
        if user_input == 'quit' or user_input == 'Quit':
            break
        res = eval(user_input)
        print(res)

eval_loop()
