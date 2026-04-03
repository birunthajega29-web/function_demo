def decorator(func):
    def inner(*args,**kwargs):
        print("before function run")
        result = func(*args,**kwargs)
        print("after function run")
    return inner

@decorator
def simple():
    print("hello")
simple()

# find the second largest number in the list
# li=[10,30,40,50,20]
# li.sort()
# print(li[-2])


li=[10,30,40,29,89.0,48,65,50]

# for i in range(len(li)-1):
#     for j in range(len(li)-1):
#         if li[j] > li[j+1]:
#             li[j],li[j+1] = li[j+1],li[j]
# print(li[-2])

first_large = float("-inf")
second_large = float("-inf")
for num in li:
    if num > first_large:
        second_large = first_large
        first_large = num
    elif num > second_large and num != first_large:
        second_large = num
print("Second largest number", second_large)
print("first largest number", first_large)


print("Updated branch")