numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes= [2, 3,  5, 7, 11, 13, 17]
Not_Primes = [4, 6, 8, 9, 10, 12, 14, 15]
print(Primes)
print(Not_Primes)
Primes=[]
Not_Primes=[]
for i in numbers:
    print(i)
for i in range(2 , 17):
    for j in range(4, 15):
        print(f'{i}  x {j} = {i //j}')
primes = [2, 3 ,5, 7, 11, 13]
is_primes = True
