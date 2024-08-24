n = int(input())
num_str = str(n)  
num_digits = len(num_str)
armstrong_sum = 0

for digit in num_str:
    armstrong_sum += int(digit) ** num_digits

if armstrong_sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")






