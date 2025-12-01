def generator():
    for i in range(1,6):
        yield i
gen = generator()
# print(next(gen))
for i in gen:
    print(i)