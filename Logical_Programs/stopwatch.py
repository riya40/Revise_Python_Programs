import time
"""
Printing the time lapsed using the stopwatch using the time function
"""


def watch_time(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), sec))


if __name__ == '__main__':
    input("Press Enter to start")
    start_time = time.time()
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    watch_time(time_lapsed)
