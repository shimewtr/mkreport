import os
from . import issue, print_error
from redminelib import Redmine


class WorkedIssues:
    REDMINE_URL = os.environ['REDMINE_URL']
    REDMINE_API_KEY = os.environ['REDMINE_API_KEY']

    def __init__(self):
        self.redmine = Redmine(self.REDMINE_URL, key=self.REDMINE_API_KEY)
        self.issues = self.input_worked_issues()
        self.post_time_entry()

    def get_redmine_subject(self, inp):
        try:
            issue_title = self.redmine.issue.get(str(inp))
            return issue_title.subject
        except:
            return False

    def input_worked_issues(self):
        issues = []
        while True:
            prefix = '作業した' if len(issues) == 0 else '他にも作業したことがあれば'
            inp = input(prefix + 'チケットの番号か内容を入力してください(qを入力すると終了)\n')
            if inp == 'q':
                break
            elif inp.isdigit():
                redmine_subject = self.get_redmine_subject(inp)
                if redmine_subject and self.confirm_redmine_subject(redmine_subject):
                    issues.append(issue.Issue(id=inp, name=redmine_subject))
                else:
                    print_error.print_error('チケットが存在しません')
            else:
                issues.append(issue.Issue(id=None, name=inp))
        return issues

    def confirm_redmine_subject(self, redmine_subject):
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

    def post_time_entry(self):
        for issue in self.issues:
            if issue.id is not None:
                try:
                    self.redmine.time_entry.create(
                        issue_id=issue.id,
                        hours=issue.time
                    )
                except:
                    print_error('作業時間の入力にエラーが発生しました')

    def build_worked_issue_text(self):
        worked_issue_text = "【作業内容】\n"
        for issue in self.issues:
            if issue.id is not None:
                worked_issue_text += "#" + issue.id
            worked_issue_text += issue.name + "\n"
            worked_issue_text += "  " + issue.coment + "\n"
        return worked_issue_text
