from . import print_error

class Issue:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name
        self.comment = self.input_comment()
        self.time = self.input_time()

    def print_name(self):
        print(self.name)

    def input_comment(self):
        inp = input('日報に記載する作業内容を入力してください\n')
        return inp

    def input_time(self):
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

