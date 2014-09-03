def hello_world():
    print("Hello world")

def call_function(f, n):
    if n <= 0:
        return
    f()
    call_function(f, n-1)

f = hello_world
call_function(f, 3)
