import math
import sys
import time


class ProgressTimer:

    def __init__(self, total_process):
        self.start_time = time.time()
        self.total_process = total_process
        self.current_time = self.start_time
        self.current_process = 0
        self.remaining_time = sys.maxint
        self.current_percentage = 0

    def increase_process(self, increment):
        self.current_process += increment
        self.current_time = time.time()
        self.current_percentage = self.current_process * 100 / self.total_process
        elapsed_time = self.current_time - self.start_time
        if self.current_percentage:
            self.remaining_time = elapsed_time * 100 / self.current_percentage - elapsed_time

    def __str__(self):
        out_string = "finished: {0:0=2d}".format(self.current_percentage) + "%, remaining time: "
        remaining_time = self.remaining_time

        hours = math.floor(remaining_time / (60 * 60))
        remaining_time -= hours * 60 * 60

        minutes = math.floor(remaining_time / 60)
        remaining_time -= minutes * 60

        out_string += "{0:0=2d}".format(int(hours)) + ":" + "{0:0=2d}".format(int(minutes)) + ":" + \
                      "{0:0=2d}".format(int(round(remaining_time)))

        out_string += ", passed time: "
        passed_time = self.current_time - self.start_time

        hours = math.floor(passed_time / (60 * 60))
        passed_time -= hours * 60 * 60

        minutes = math.floor(passed_time / 60)
        passed_time -= minutes * 60

        out_string += "{0:0=2d}".format(int(hours)) + ":" + "{0:0=2d}".format(int(minutes)) + ":" + \
                      "{0:0=2d}".format(int(round(passed_time)))

        return out_string
