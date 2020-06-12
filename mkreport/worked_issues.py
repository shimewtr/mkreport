import os
from . import issue, print_error
from redminelib import Redmine


class WorkedIssues:
    REDMINE_URL = os.environ['REDMINE_URL']
    REDMINE_API_KEY = os.environ['REDMINE_API_KEY']

    def __init__(self):
        self.__redmine = Redmine(self.REDMINE_URL, key=self.REDMINE_API_KEY)
        self.__issues = self.__input_worked_issues()
        self.__post_time_entry()
        self.__issue_text = self.__build_worked_issue_text()

    @property
    def issue_text(self):
        return self.__issue_text

    def __build_worked_issue_text(self):
        worked_issue_text = "【作業内容】\n"
        for issue in self.__issues:
            if issue.id is not None:
                worked_issue_text += "#" + issue.id
            worked_issue_text += issue.name + "\n"
            worked_issue_text += "  " + issue.comment + "\n"
        return worked_issue_text

    def __confirm_redmine_subject(self, redmine_subject):
        dic = {'y': True, 'yes': True, 'n': False, 'no': False}
        while True:
            try:
                inp = input(redmine_subject + "でよろしいですか?(y/n)\n")
                confirm = dic[inp.lower()]
                break
            except:
                pass
            print_error.print_error('yかnを入力してください。')
        return confirm

    def __get_redmine_subject(self, inp):
        try:
            issue_title = self.__redmine.issue.get(str(inp))
            return issue_title.subject
        except:
            print_error.print_error('チケットが存在しません')
            return False

    def __input_worked_issues(self):
        issues = []
        while True:
            prefix = '作業した' if len(issues) == 0 else '他にも作業したことがあれば'
            inp = input(prefix + 'チケットの番号か内容を入力してください(qを入力すると終了)\n')
            if inp == 'q':
                break
            elif inp.isdigit():
                redmine_subject = self.__get_redmine_subject(inp)
                if redmine_subject and self.__confirm_redmine_subject(redmine_subject):
                    issues.append(issue.Issue(id=inp, name=redmine_subject))
            else:
                issues.append(issue.Issue(id=None, name=inp))
        return issues

    def __post_time_entry(self):
        for issue in self.__issues:
            print("dfadsf")
            print(issue.id)
            print("dfadsf")
            if issue.id is not None:
                try:
                    self.__redmine.time_entry.create(
                        issue_id=issue.id,
                        hours=issue.time
                    )
                except:
                    print_error('作業時間の入力にエラーが発生しました')
