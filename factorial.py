#n! = 1*2*3*4*5....*n
n=4
product = 1
for i in range(n):
    product = product*(i+1)
print(product)
def factorial(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
    return product

f = factorial(5)
print(f)