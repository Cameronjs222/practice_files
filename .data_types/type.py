y = [5, 7, 10, 7, 1]
test = {"name": "Cameron", "age": 27, "height": "6ft 2in", "nameage": "test"}
new = test.pop("nameage")
print(test)
print()
# def betterThan(arr, num):
#     i = 0
#     while i <len(arr):
#         if (arr[i] <= num):
#             newArr = arr.pop(arr[i])
#         i = i + 1

# def better(arr, num):
#     i = 0
#     for i in range(i, len(arr)):
#         if (arr[i] <= num):
#             newArr = arr.pop(arr[i])
#     return newArr

def betterThan(arr, num):
    newArr = [i for i in arr if i > num]
    return newArr

print(betterThan(y, 5))
# print(x[0])

x = 37
y = float(x)
print(y)
a = 26.7
b = int(a)
print(b)

my_age = 