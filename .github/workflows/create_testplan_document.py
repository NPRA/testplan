import datetime
import mdutils

def run():
    current_time = str(datetime.datetime.now())

    mdFile = mdutils.MdUtils(file_name='testplan.md',title='Markdown of testplan for Jammertest')
    mdFile.new_header(level=1, title='Jammertest 2024 Testplan')
    mdFile.new_line(mdFile.new_inline_image("NPRA logo", "/graphics/logo NPRA.jpg"))

    mdFile.new_paragraph(""" This is a test to add a significant block of text
                         and this is the second line 
                         and third line
                         """)
    mdFile.new_table_of_contents(table_title='Contents', depth=2)
    mdFile.create_md_file()

 
if __name__ == '__main__':
    run()