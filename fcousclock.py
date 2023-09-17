import time
import os

def focus_timer(duration_minutes):
    duration_seconds = duration_minutes * 60
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        remaining_time = duration_seconds - elapsed_time

        if remaining_time <= 0:
            break

        minutes, seconds = divmod(int(remaining_time), 60)
        time_display = f"{minutes:02d}:{seconds:02d}"

        os.system('clear')  # For Windows, use 'cls'
        print(f"Focus Timer: {time_display}")
        time.sleep(1)

    os.system('clear')  # For Windows, use 'cls'
    print("Focus Timer: 00:00")
    print("Time's up! Take a break.")

if __name__ == "__main__":
    focus_duration = int(input("请输入专注时长(分钟)："))
    focus_timer(focus_duration)
