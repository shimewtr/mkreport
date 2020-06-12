import os
import pyperclip
import requests
import sys
from . import file_operation, print_error, worked_issues, worked_time



def main():
    fo = file_operation.FileOperation()
    wt = worked_time.WorkedTime()
    wi = worked_issues.WorkedIssues()
    fo.build_report_content(wt.format_report_time(), wi.build_worked_issue_text())
    fo.make_report()
    # pyperclip.copy(report_content)

if __name__ == '__main__':
    main()
