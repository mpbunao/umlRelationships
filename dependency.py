"""Dependency: A report printer temporarily uses a report object."""
class Report:
    def __init__(self, text):
        self.text = text

class ReportPrinter:
    def print_report(self, report):
        print(f'Report: {report.text}')

if __name__ == '__main__':
    report = Report('UML relationships are useful.')
    printer = ReportPrinter()
    printer.print_report(report)
