

# Pomodoro Time


import time

print("🍅 Welcome to the Pomodoro Timer")

try:
    mins = int(input("Enter time in minutes: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

total_seconds = mins * 60

while total_seconds > 0:

    minutes = total_seconds // 60
    seconds = total_seconds % 60

    timer = f"{minutes:02d}:{seconds:02d}"

    print(f"\r⏳ Time Remaining: {timer}", end="")

    time.sleep(1)

    total_seconds -= 1

print("\n✅ Time's up! Take a break.")
