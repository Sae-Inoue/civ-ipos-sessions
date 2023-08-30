def some_function(some_variable):
    return some_variable + 2

def some_other_function(some1_variable):

    some_function = str(some1_variable)
    print(f'{some1_variable =}')
    return some_function(some1_variable)



some_other_function(42)