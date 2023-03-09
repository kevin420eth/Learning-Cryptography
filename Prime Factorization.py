prime_factor = []
exponent_list = []

def check_prime(n):
    for _ in range(2,n):
        if n % _ == 0:
            return False
    return True
    
def find_prime_factor(n):
    for _ in range(2,n+1):
        if check_prime(_) == True and n % _ == 0:
            prime_factor.append(_)

def find_exponent(n):
    for q in prime_factor:
        e = 0
        while n % q == 0:
            e += 1
            n /= q
        exponent_list.append(e)

while True:
    try:
        your_number = int(input("Please enter a positive integer:\n"))
    except ValueError:
        print("I need an integer grater than 0!\n")
    else:
        if your_number > 0 and your_number % 1 == 0:
            break
        else:
            print("I need an integer grater than 0!\n")

find_prime_factor(your_number)
find_exponent(your_number)

p=""
for _ in prime_factor:
    if p =="":
        p+=f"{_}^{exponent_list[prime_factor.index(_)]}"
    else:
        p+=f"*{_}^{exponent_list[prime_factor.index(_)]}"

print(f"{your_number} = {p}")
