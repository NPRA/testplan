import datetime

def run():
    current_time = datetime.datetime.now()

    with open("testplan.md","w") as markdown_testplan:
        markdown_testplan.write("# This is a test\n")
        markdown_testplan.write("This is a test markdown file for testing\n")
        markdown_testplan.write(current_time)


if __name__ == '__main__':
    run()