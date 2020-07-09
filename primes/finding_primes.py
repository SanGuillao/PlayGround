flag = False
list_of_primes = [1.0]
x = 2.0

while x <= 100000:
    for i in list_of_primes:
        if x % i == 0 and i != 1.0:
            flag = True
            break
            
    if flag == False:
        list_of_primes.append(x)
    
    flag = False
    x += 1

with open('prime_numbers.txt', 'w') as f: 
    for line in list_of_primes:
        f.write(str(line))
        f.write('\n')