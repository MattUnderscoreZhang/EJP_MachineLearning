a = 5
b = 2

for i in range(1, 51):
    a = a+b
    if (i%10 == 0):
        print("We have now looped", i, "times. The value of a is", a)

print("We have finished looping 50 times. The value of a is", a)
