prime_factor =[]

def check_prime(n):
    for _ in range(2,n):
        if n % _ == 0:
            return False
    return True

def find_prime_factor(n):
    for _ in range(2,n+1):
        if check_prime(_) == True and n % _ == 0:
            prime_factor.append(_)

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

x = your_number

for _ in prime_factor:
    x = (1-1/_)*x

print(f"PHI({your_number}) = {round(x)}")