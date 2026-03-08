

# 3 - Pomodoro Time


import time

print("Welcome to the Pomodoro Timer")

mins = input("Enter time in minutes: ")
mins = int(mins)

total_seconds = mins * 60


while total_seconds > 0:
    mins = total_seconds // 60
    secs = total_seconds % 60

    clock = f"{mins:02d}:{secs:02d}"

    print(f"\rTime Remaining: {clock}", end="")
    

    time.sleep(1)

    total_seconds -= 1

print("\rTime's up! Take a break.")