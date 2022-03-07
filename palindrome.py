#function returns if number is prime
def is_prime(x):

    prime = True
    n = 1

    if x == 1:
        return False

    while n in range(1, x): 
        if x % n == 0 and n > 1 and n < x: 
            prime = False
            break
        n += 1
    
    return prime

#reverse a number
def reverse_num(x):

    num = x
    reversed_num = 0

    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return reversed_num

#returns palindrome primes in specified range
#parameters: x - min range, y - max range
def pal_primes(x, y):

    primes_list = []

    while x <= y:
        #python will not evaluate second condition unless first is true
        #is_prime(x) takes significantly longer to execute since it checks thru all #'s 1 - x
        if x == reverse_num(x) and is_prime(x) == True: 
            primes_list.append(x)
        x += 1

    return primes_list

print(pal_primes(10000, 99999))

        