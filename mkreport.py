import sys
import os
import datetime
import requests

REPORTER = os.environ['REPORTER']
REDMINE_URL = os.environ['REDMINE_URL']
REDMINE_API_KEY = os.environ['REDMINE_API_KEY']
BASIC_AUTH_USER = os.environ['BASIC_AUTH_USER']
BASIC_AUTH_PASSWORD = os.environ['BASIC_AUTH_PASSWORD']
today = datetime.date.today()

def main():
    worked_time = input_time()
    worked_ticket = input_ticket_id()
    worked_ticket_text = build_worked_ticket(worked_ticket)
    report_content = build_report_content(worked_time, worked_ticket_text)
    make_report(report_content)


def build_worked_ticket(worked_ticket):
    worked_ticket_text = ''
    for number, title in worked_ticket.items():
        worked_ticket_text += "#{number} {title}\n".format(number=number, title=title)
    return worked_ticket_text


def build_report_content(worked_time, worked_ticket):
    day_of_week_list = ["月", "火", "水", "木", "金", "土", "日"]
    start = worked_time[0]
    end = worked_time[1]
    report_content = open('./report_content.txt', 'r').read().format(
        reporter=REPORTER,
        month=today.month,
        day=today.day,
        day_of_week= day_of_week_list[today.weekday()],
        start=start,
        end=end,
        worked_ticket=worked_ticket
    )
    return report_content

def confirm_issue_title(issue_title):
    dic = {'y': True, 'yes': True, 'n': False, 'no': False}
    while True:
        try:
            inp = dic[input(
                "「{issue_title}」でよろしいですか?(y/n)\n".format(issue_title=issue_title)).lower()]
            break
        except:
            pass
        print('yかnを入力してください。')
    return inp


def get_issue_title(id):
    url = "{url}issues.json?issue_id={id}&key={api_key}".format(
        url=REDMINE_URL,
        id=id,
        api_key=REDMINE_API_KEY
    )

    r = requests.get(url, auth=(BASIC_AUTH_USER, BASIC_AUTH_PASSWORD)).json()

    if len(r["issues"]):
        return r["issues"][0]["subject"]
    else:
        return False


def input_ticket_id():
    ticket_ids = {}
    while True:
        prefix = '作業した' if len(ticket_ids) == 0 else '他にも作業したチケットがあれば'
        inp = input(prefix + 'チケットの番号を入力してください(qを入力すると終了)\n')
        if inp == 'q':
            break
        elif inp.isdigit():
            issue_title = get_issue_title(inp)
            if issue_title:
                if confirm_issue_title(issue_title):
                    ticket_ids[inp] = issue_title
            else:
                print('チケットが存在しません')
        else:
            print('チケットの番号は数字で入力してください')
    return ticket_ids

def input_time():
    while True:
        default_start_time = '0730'
        inp = input('勤務開始時間を「hhmm」で入力してください(デフォルト「' + default_start_time + '」)\n')
        if not(inp):
            start_time = default_start_time
            break
        elif inp.isdigit() and len(inp) == 4:
            start_time = inp
            break
        else:
            print('入力形式が正しくありません。')
    while True:
        default_end_time = '1630'
        inp = input('勤務終了時間を「hhmm」で入力してください(デフォルト「' + default_end_time + '」)\n')
        if not(inp):
            end_time = default_end_time
            break
        elif inp.isdigit() and len(inp) == 4:
            end_time = inp
            break
        else:
            print('入力形式が正しくありません。')
    return [start_time, end_time]

def make_report(report_content):
    dir_name = "./daily_report/{year}/{month}/".format(year=today.year, month=today.month)
    file_name = dir_name + str(today.day) + ".txt"
    os.makedirs(dir_name, exist_ok=True)
    f = open(file_name, 'x')
    f.write(report_content)
    f.close()


if __name__ == '__main__':
    main()