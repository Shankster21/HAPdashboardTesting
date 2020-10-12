import ibm_db_dbi
from datetime import datetime
from datetime import date



# SQL statments to query the database
dir()
con = ibm_db_dbi.connect(dsn=None,user='bavery',password='bavery',database='DEV',conn_options=None)
curs = con.cursor()

curs.execute("select distinct brlocname from filelib.locmast order by brlocname")
locations = curs.fetchall()

region2 = ['Nebraska City', 'Howe', 'Missouri Valley', 'Modale', 'Logan', 'California junction', 'Council Bluffs', 'Neola', 'Treynor', 'Henderson', 'Malvern', 'Pacific Junction', 'Silver City', 'Imogene', 'Randolph', 'Woodbine', 'Mondamin', 'Riversioux']
region3 = ['Avon', '18th Street', 'Waukee', 'Dexter', 'Redfield', 'Rippey', 'Dallas Center', 'Minburn', 'Panora', 'Booneville', 'Runnells', 'Winterset', 'Fairfield', 'Wever']
region4 = ['Slater', 'Cambridge', 'Luther', 'Madrid', 'Alleman', 'Enterprise', 'Indianola', 'Mitchellville', 'Lacona', 'Monroe', 'Prairie City West', 'Prairie City', 'Colo', 'Jewell', 'Stanhope', 'Randall']
region5 = ['Newton', 'Collins', 'Melbourne', 'Mingo', 'Malcom', 'Montezuma', 'Reinbeck', 'Kellogg', 'Gilman', 'Grundy Center', 'Holland', 'Laurel', 'Lincoln', 'Voorhies', 'Pickering']


# _________ WRITE HTML FILE ________
with open('locationsListPROD.html','w') as file:

    file.write('<!doctype html><html lang="en"> <head><title>List of Locations</title><meta charset="utf-8"><meta name="description" content="The HTML5 Herald"><meta name="author" content="SitePoint"><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous"> <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script><link rel="stylesheet" type="text/css" href="style.css"><script src="tempData.js"></script></head> \n')

    file.write('<body> \n')

    region2.sort()
    region3.sort()
    region4.sort()
    region5.sort()

    file.write('''    <h3> Region 2 : </h3>\n''')
    for item in region2:
        file.write('<p><a href= "#"> ' + item + '</a></p> \n')

    file.write('\n')
    file.write('''    <h3> Region 3 : </h3>\n''')
    for item in region3:
        file.write('<p><a href= "#"> ' + item + '</a></p>\n')

    file.write('\n')
    file.write('''    <h3> Region 4 : </h3>\n''')
    for item in region4:
        file.write('<p><a href= "#"> ' + item + '</a></p>\n')

    file.write('\n')
    file.write('''    <h3> Region 5 : </h3>\n''')
    for item in region5:
        file.write('<p><a href= "#"> ' + item + '</a></p>\n')




    file.write('<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script> <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script><script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script></body></html>')
