'Right justify'

def right_justify(strInput):
    'Right justifies the input string'
    length = len(strInput)
    print(' '*(70-length) + strInput)

right_justify('Hello there! How are you?')
right_justify('Howdy?!')
right_justify('Just another statement!')
