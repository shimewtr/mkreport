import os
from . import print_error


class WorkedTime:
    DEFAULT_START_TIME = os.environ['DEFAULT_START_TIME']
    DEFAULT_END_TIME = os.environ['DEFAULT_END_TIME']

    def __init__(self):
        self.__time_list = self.build_worked_time()

    def build_worked_time(self):
        return self.format_time(self.input_worked_time())

    def input_worked_time(self):
        while True:
            start_time = self.input_time(self.DEFAULT_START_TIME, '勤務開始時間')
            end_time = self.input_time(self.DEFAULT_END_TIME, '勤務終了時間')
            if start_time <= end_time:
                break
            else:
                print_error.print_error('勤務時間の入力が正しくありません。')
        return [start_time, end_time]

    def input_time(self, default_time, target_time):
        time = default_time
        while True:
            inp = input(
                target_time + 'を「hhmm」で入力してください(デフォルト「' + default_time + '」)\n')
            if not(inp):
                break
            elif inp.isdigit() and len(inp) == 4:
                time = inp
                break
            else:
                print_error.print_error('入力形式が正しくありません。')
        return time

    def format_time(self, times):
        formated_times = []
        for time in times:
            formated_time = time[:2] + ':' + time[2:]
            if formated_time[0] == '0':
                formated_time = formated_time[1:]
            formated_times.append(formated_time)
        return formated_times

    def format_report_time(self):
        return "【勤務時間】\n" + self.__time_list[0] + "-" + self.__time_list[1] + "\n"
