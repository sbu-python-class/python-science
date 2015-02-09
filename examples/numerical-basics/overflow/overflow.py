from __future__ import print_function

iold = -1
i = 1

type_init = type(i)
print("type currently: ", type_init)

while (i > iold):
    print(i)
    iold = i
    i *= 2

    if (not type(i) == type_init):
        print("type changed, now: ", type(i))
        break

print(i)
