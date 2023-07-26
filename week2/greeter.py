#input()  #pause
#print(__name__)

def lue():
    a.append()
    # global a
    # a = 42

def greet(a):
    print(a)
    print("Hello, World!")
#     a =12

# def main():
#     greet()
#
# if __name__ == '__main__':
#     a = 42
#     greet()
#a = 42   ##this is global variable(no indentation)
a = []
lue()  #caller
greet(a)

def a():
    print("I am in A")
    return 42

def b():
    a()
    print("I am in B")
def c():
    b()
    print("I am in C")

c()