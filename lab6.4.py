values_users = tuple(input()) 
tup_city = ()
tup_city += tuple([i for i in values_users if 'ва' in i]) 
print(*tup_city)