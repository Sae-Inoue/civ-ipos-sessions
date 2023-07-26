#1
#import greeter
# greeter.greet()
#print(__name__)
#
# #2
# import greeter as g
# g.greet()
#
# #3
# from greeter import greet
# greet()

def modify(n, x):
    n = 2
    x.append(3)

n = 1
list_ = [1, 2]
modify(n, list_)

print(n) # Outputs: 1
print(list_) # Outputs: [1, 2, 3]