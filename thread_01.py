import threading

def first_fun(age):
    while True:
        print('I am first child.', age)
    pass
    return
def second_fun(age):
    while True:
        print('I am second child.', age)
    pass
    return
if __name__== "__main__":
    first = threading.Thread(target=first_fun , args = (5,))
    second = threading.Thread(target=second_fun, args = (3,))
    first.start()
    second.start()
    first.join() #연락을 했으니 전화를 받아야한다.
    second.join()
    while True:
        print('I am child.')
    pass