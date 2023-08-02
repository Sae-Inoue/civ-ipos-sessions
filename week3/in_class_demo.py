my_2dim_list = [[1,2,3],[4,5,6],[7,8,9]]
print(my_2dim_list[2][0])

# sequential interation over 2D
for row in my_2dim_list:
    for elem in row:
        print(elem, end=' ')

def make_2d(rows, cols, value=None):
    '''Create a rows x colos 2D data structure initialized to _value_
    Example:
        made_2d(3,3)
        [[None, None, None],[None, None, None],[None, None, None]] '''
    list_2d = []  #create a list
    for _ in range(rows):
        elems = []
        for _ in range(cols):
            elems.appe.nd(value)
        '''elems = [value for _ in range(cols)]    This code can replace from elems = []'''
        list_2d.append(elems)
    return list_2d    #List of lists of the required dimentions
print(make_2d(2, 9, 3))