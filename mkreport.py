import sys
import os
import datetime
import requests

REDMINE_URL = os.environ['REDMINE_URL']
REDMINE_API_KEY = os.environ['REDMINE_API_KEY']
BASIC_AUTH_USER = os.environ['BASIC_AUTH_USER']
BASIC_AUTH_PASSWORD = os.environ['BASIC_AUTH_PASSWORD']


def main():
    worked_ticket = input_ticket_id()
    print(worked_ticket)


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
        prefix = '今日作業した' if len(ticket_ids) == 0 else '他にも作業したチケットがあれば'
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


if __name__ == '__main__':
    main()
