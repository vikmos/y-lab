import math as m 

a = 60
prime_factors = [2,3,5]

exponents =list(map(lambda x:m.floor(m.log(a,x)),prime_factors))
rez = []
count = 0
max_prime = 0
for i in range(exponents[0]+1):
    for j in range(exponents[1]+1):
        for k in range(exponents[2]+1):
            prime = 2 ** i * 3 ** j * 5 ** k
            if prime <= a:
                count += 1
                max_prime = max(max_prime, prime)
rez.append(count)
rez.append(max_prime)
print(rez)
