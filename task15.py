age = int(input("your age: "))
# if age % 2 == 0:
#     for i in range (0, age + 1, 2):
#         print(i)
# else:
#     for i in range (1, age + 1, 2):
#         print(i)

def your_age(a):
    if a % 2 == 0:
        for i in range (0, a + 1, 2):
            print(i)
    else:
        for i in range (1, a + 1, 2):
            print(i)

print(your_age(age))