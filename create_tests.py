def run():
    with open("testplan.md","w") as markdown_testplan:
        markdown_testplan.write("# This is a test\n")
        markdown_testplan.write("This is a test markdown file for testing\n")

if __name__ == '__main__':
    run()