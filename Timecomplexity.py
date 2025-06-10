#Program with O(1) time complexity:
# Time Complexity: O(1)

n = int(input("Enter a number: "))
result = n * 10
print("Result after multiplying by 10:", result)

#O(n) version 
# Time Complexity: O(n)

n = int(input("Enter a number: "))
result = 0
for _ in range(10):
    result += n
print("Result after multiplying by 10:", result)
