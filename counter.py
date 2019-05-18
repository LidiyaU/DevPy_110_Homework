# def counter(N, k):    #для одного прохода
#     res = 0
#     for i in range(1, N + 1):
#         res = (res + k) % i
#
#     return(res + 1)
#
# print(counter(8,3))

def counter(N, k):
    list_people = [i for i in range(1, N + 1)]
    res = 0
    k -= 1
    while len(list_people) > 1:
        res = (res + k) % len(list_people)
        print(list_people.pop(res),"pops out")

    return f'survivor: {list_people[0]}'

print(counter(8,3))