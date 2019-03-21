
def isEven(num):
    return num % 2 == 0



def partition(l, cback):
    truthy_list = []
    falsy_list = []

    for i in l:
        print(cback(i))
        if cback(i):
            truthy_list.append(i)
        else :
            falsy_list.append(i)
    print(truthy_list)
    print(falsy_list)
    print([truthy_list, falsy_list])


partition([1,2,3,4], isEven)


