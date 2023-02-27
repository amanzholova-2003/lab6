#tuple() 1 esep
my_tuple = ('банан', 'груша', 'манго')
print(my_tuple[0], my_tuple[-1])
print(len(my_tuple))
print(min(my_tuple, key=len))
print(max(my_tuple, key=len))
print(my_tuple.index('груша'))