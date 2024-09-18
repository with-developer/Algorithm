remainders = set()

for _ in range(10):
    number = int(input())
    
    remainder = number % 42
    remainders.add(remainder)

print(len(remainders))