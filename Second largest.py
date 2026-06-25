n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input()))
largest = second = float('-inf')
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second largest number:", second)