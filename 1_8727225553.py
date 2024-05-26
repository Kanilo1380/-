import random

"""

جاروبرقی

در این برنامه، یک شبیه‌سازی از نظافت‌کار بین دو اتاق است (اتاق A و اتاق B) هر اتاق می‌تواند در دو وضعیت "کثیف" یا "تمیز" باشد. مکان فعلی نیز در یکی از اتاق‌ها است

و سپس با شبیه‌سازی حرکت نظافت‌کار، وضعیت اتاق‌ها را به‌روزرسانی می‌کند


"""

ROOM_A = random.randint(1, 2)
ROOM_B = random.randint(1, 2)
Current = random.randint(1, 2)

# نمایش وضعیت اولیه
print("if Room A = 1:dirty else if Room A = 2:clean")
print("if Room B = 1:dirty else if Room B = 2:clean")
print("-------------------------------------------")
print("if Current = 1 : location is Room A else if Current = 2 : location is Room B")
print("-------------------------------------------")
print(f"Room A = {ROOM_A} Room B = {ROOM_B} Current = {Current}")
print("-------------------------------------------")

# شرایط حرکت 1
if Current == 1:
    print("our location in Room A")
    if ROOM_A == 1:
        print("Room A is dirty")
        ROOM_A = 2
        print("Room A has been cleaned")
        print("moving location to Room B")
        if ROOM_B == 1:
            print("Room B is dirty")
            B = 2
            print("Room B has been cleaned")
        else:
            print("Room B is clean")
    elif ROOM_A == 2:
        print("Room A has been cleaned")
        if ROOM_B == 2:
            print("Room B has been cleaned")
        elif ROOM_B == 1:
            print("Room B is dirty")
            ROOM_B = 2
            print("Room B has been cleaned")

#شرایط حرکت 2
elif Current == 2:
    print("our location in Room B")
    if ROOM_B == 1:
        print("Room B is dirty")
        ROOM_B = 2
        print("Room B has been cleaned")
        print("moving location to Room A")
        if ROOM_A == 1:
            print("Room A is dirty")
            ROOM_A = 2
            print("Room A has been cleaned")
        else:
            print("Room A is clean")
    elif ROOM_B == 2:
        print("Room B has been cleaned")
        if ROOM_A == 2:
            print("Room A has been cleaned")
        elif ROOM_A == 1:
            print("Room A is dirty")
            ROOM_A = 2
            print("Room A has been cleaned")