import datetime
import mdutils
import json
 
# Opening JSON file with tests
json_test_file = open('tests.json')
 
# returns JSON object as 
# a dictionary
List_of_tests = json.load(json_test_file)




def test_template(testplanMD, test_group):
    # Create text for a single test
    tgroup_number = test_group['Group number']
    tgroup_name = test_group['Group name']
    rationale = test_group['Rationale for test']
    test_setup = test_group['Test setup']
    areas = test_group['Possible test areas']
    tcontact = test_group['Technical contact']

    testplanMD.new_header(level=2, title=f'{tgroup_number} {tgroup_name}')
    #testplanMD.new_header(level=2, title=f'{tgroup_name}')
    testplanMD.new_header(level=3, title='Rationale for test', add_table_of_contents="n")
    testplanMD.new_paragraph(rationale)
    testplanMD.new_header(level=3, title='Test setup', add_table_of_contents="n")
    testplanMD.new_paragraph(test_setup)
    testplanMD.new_header(level=4, title=f'Possible areas: {areas}')
    testplanMD.new_header(level=4, title=f'Technical contact: {tcontact}')

    for test in test_group['Tests']:
        t_id = test["Test id"]
        t_name =  test["Test name"]
        t_text = test["Test text"]
        t_power = test["Power or power range"]
        t_time = test["Test time"]
        t_location = test["Location of transmitter"]
        t_comment =  test["Test comment"]

        testplanMD.new_header(level=3, title=f'{t_id} {t_name}')
        testplanMD.write(t_text)
        testplanMD.new_line(' ')
        testplanMD.write(f"Power: **{t_power}**")
        testplanMD.new_line(' ')
        testplanMD.write(f"Test running time: **{t_time}**")
        testplanMD.new_line(' ')
        testplanMD.write(f"Location of transmitter: **{t_location}**")
        testplanMD.new_line(' ')
        testplanMD.write(f"Comment: _{t_comment}_")


#print(List_of_tests)
#print(List_of_tests["Test groups"][0])


def run():
    current_time = str(datetime.datetime.now())

    testplanMD = mdutils.MdUtils(file_name='testplan.md',title='Markdown of testplan for Jammertest')
    testplanMD.new_header(level=1, title='Jammertest 2024 Testplan')
    
    #testplanMD.new_line(testplanMD.new_inline_image("NPRA logo", "graphics/NPRA.png"))
    testplanMD.new_paragraph(mdutils.Html.image(path="graphics/NPRA.png", size='200'))

    testplanMD.new_paragraph(""" This is a test to add a significant block of text
                         and this is the second line 
                         and third line
                         """)
    
    # Insert tests below here
    test_template(testplanMD, List_of_tests["Test groups"][0])

    #testplanMD.new_table_of_contents(table_title='Contents', depth=3)
    #testplanMD.new_table_of_contents(table_title='Contents', depth=2)
    testplanMD.create_md_file()

 
if __name__ == '__main__':
    run()
