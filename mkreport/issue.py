from . import print_error


class Issue:
    def __init__(self, id=None, name=None):
        self.__id = id
        self.__name = name
        self.__comment = self.__input_comment()
        if id is not None:
            self.__time = self.__input_time()

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def comment(self):
        return self.__comment

    @property
    def time(self):
        return self.__time

    def __input_comment(self):
        inp = input('日報に記載する作業内容を入力してください\n')
        return inp

    def __input_time(self):
        while True:
            inp = input('作業時間を入力してください\n')
            try:
                float(inp)
            except ValueError:
                print_error.print_error('数値を入力してください')
            else:
                if float(inp) >= 0:
                    break
                print_error.print_error('0以上の数値を入力してください')
        return float(inp)
