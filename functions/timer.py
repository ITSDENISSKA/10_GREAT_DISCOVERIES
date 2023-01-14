import time


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def get_time(self):
        return time.perf_counter() - self.start_time

    def stop(self):
        end_time = time.perf_counter() - self.start_time
        self.start_time = None
        return end_time
