import time
import math

while True:
    subnum = 1
    times = 0

    while True:
        try:
            num = int(input("\nInput the number you want to square root: "))
            break
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.")
    display = input("\nDo you want to show steps: ")
    display = display.lower()
    firstsecond = time.time()
    print(display)
    if display.startswith("y") or display.startswith("s"):
        print("\nSeconds    Times    Subnum     Num")
    if num == 0:
        print("\n The number is 0")
    else:
        while num > 0:
            finaltime = time.time()
            totaltime = round(finaltime - firstsecond, 3)
            num -= subnum
            subnum += 2
            times += 1
            if display.startswith("y") or display.startswith("s"):
                print(f"{totaltime}         {times}         {subnum}        {num}")
        if num == 0:
            if display.startswith("y") or display.startswith("s"):
                print("\nSeconds    Times    Subnum     Num")
            print(f"\nThe square root of the number is: {times}")
        elif num < 0:
            if display.startswith("y") or display.startswith("s"):
                print("\nSeconds       Times       Subnum        Num")
            print("\nThe number is not a perfect square.")
    repeat = input("\nDo you want to calculate another square root? (y/n): ")
    if repeat.startswith("n"):
        break