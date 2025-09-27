def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# Accept user input
num = int(input())

# Check if the number is happy
if is_happy(num):
    print("True")
else:
    print("False")
