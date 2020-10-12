import ibm_db_dbi
from datetime import datetime
from datetime import date

today = date.today()

# SQL statments to query the database
dir()
con = ibm_db_dbi.connect(dsn=None,user='bavery',password='bavery',database='DEV',conn_options=None)
curs = con.cursor()

curs.execute("select *  from filelib.haptempsv2 where hc_site_name = 'Winterset'")
rows = curs.fetchall()

curs.execute("select distinct hc_bin_code from filelib.haptempsv2 where hc_site_name = 'Winterset' order by hc_bin_code ")
bins = curs.fetchall()

curs.execute("select distinct hc_read_date from filelib.haptempsv2 where hc_site_name = 'Winterset'")
dates = curs.fetchall()

# curs.execute("select distinct hc_read_date from filelib.haptempsv2 where hc_site_name = 'Winterset' and hc_read_date = '{}'").formate(today)
# todayDate = curs.fetchall()

curs.execute("select distinct hc_bin_code from filelib.haptempsv2 where hc_site_name = 'Winterset'")
HAPbins = curs.fetchall()

curs.execute("select distinct gb_bcbin, gb_capacity, gb_bushels_in_bin, gb_bin_will_hold, gb_commodity_code, gb_measure_date from filelib.getbinclct where  gb_location = '37' order by gb_bcbin ")
binMeasurements = curs.fetchall()

# curs.execute("select distinct hc_bin_code from filelib.haptempsv2 where hc_site_name = 'Winterset' and avgf > '80' and hc_read_date = '2020-08-08'")
# hotBins = curs.fetchall()

# _________ WRITE HTML FILE ________
with open('WintersetHomePROD.html','w') as file:

# HTML page head info stuff
    file.write('''<!doctype html><html lang="en">
    <head><title>Winterset Home Page</title><meta charset="utf-8"><meta name="description" content="The HTML5 Herald"><meta name="author" content="SitePoint">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script><script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" type="text/css" href="WintersetHome.css"><script src="WintersetHome.js"></script>\n</head>\n\n''')

# header
    file.write('''<header>

         <div class="row no-gutters">
              <div class="col-7">
                   <div id = "locationHeader">
                        Winterset
                   </div>
              </div> <!-- col 1 -->

              <div class="col-5 col2">
                   <div id = "locationInfo">
                             <p> Location Number: 37 </p>
                           <p> Functional Unit: 17 </p>

                   </div>
                   <!-- <div id = "diagram">
                   <img src="WintersetDiagram.pdf" > -->

                   </div>

              </div> <!-- col 2 -->
         </div> <!-- row 1 -->

    </header>\n''')
    file.write('<body>  \n')

# table
    file.write('''
        <div class = "tableArea">
            <h3> Bin Overview </h3>
            <br>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>Bin Number</th>
                        <th>Commodity</th>
                        <th>Percent full</th>
                        <th>HAP</th>
                    </tr>
                </thead>
                <tbody>  \n''')

# BIN NUMBER COLUMN 1/4
    binCount = 0
    for bin in binMeasurements:
        binCount = binCount + 1

    for i in range(binCount):
        file.write('''
                    <tr>

<!-- BIN NUMBER COLUMN  -->
                        <td>
                            <button type="button" class="btn btn-secondary btn-lg" data-toggle="modal" data-target="#modal''')
        file.write(str(i))
        file.write('''">''')
        file.write('''      <script>
                                binMeasurements = fillTable();
                                document.write(binMeasurements[''')
        file.write(str(i))
        file.write('''].bin);
                            </script>
                            </button>''')
        file.write('''          <div class="modal fade" id="modal''')
        file.write(str(i))
        file.write('''" role="dialog">
                                    <div class="modal-dialog">
                                        <div class="modal-content">
                                            <div class="modal-header">
                                                <h4 class="modal-title">''')
        file.write('''
                                                    <script>
                                                            document.write("Bin " + binMeasurements[''')
        file.write(str(i))
        file.write('''].bin);
                                                    </script>
                                                </h4>
                                            </div> <!-- end modal header  -->
                                            <div class="modal-body">
                                                <script>''')
        file.write('''
                                                    document.write('<p>' + ' Capacity : ' + binMeasurements[''')
        file.write(str(i))
        file.write('''].capacity + '</p>');''')
        file.write('''
                                                    document.write('<p>' + ' Current holdings : ' + binMeasurements[''')
        file.write(str(i))
        file.write('''].currentHoldings + '</p>');''')
        file.write('''
                                                    document.write('<p>' + ' Will Hold : ' + binMeasurements[''')
        file.write(str(i))
        file.write('''].willHold + '</p>');''')
        file.write('''
                                                    document.write('<p>' + 'Last measured on : ' + binMeasurements[''')
        file.write(str(i))
        file.write('''].measureDate + '</p>');''')
        file.write('''
                                                </script>
                                                </div> <!-- end modal body  -->
                                                <div class="modal-footer">
                                                    <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                                </div> <!-- end modal footer -->
                                                </div> <!-- end modal content  -->
                                                </div> <!-- end modal dialog  -->
                                                </div> <!-- end modal  --> \n''')
        file.write('''</td> \n''')

# COMMODITY COLUMN 2/4
        file.write('''<!-- COMMODITY COLUMN  -->
            <td>
                <script>
                    binMeasurements = fillTable();
                    if (binMeasurements[''')
        file.write(str(i))
        file.write('''].commodityCode == "1"){document.write('<div class = "cornColor"> CORN </div>')}
                    else if (binMeasurements[''')
        file.write(str(i))
        file.write('''].commodityCode == "3"){document.write('<div class = "beanColor"> BEANS </div>')}
                    else if (binMeasurements[''')
        file.write(str(i))
        file.write('''].commodityCode == "0"){document.write('-' )}
                </script>
            </td> \n''')

# PERCENTAGE FILL COLUMN  3/4
        file.write(''' <!-- PERCENTAGE FILL COLUMN  -->
            <td>
                <script>
                    binMeasurements = fillTable();var fill = Number( binMeasurements[''')
        file.write(str(i))
        file.write('''].currentHoldings) / Number( binMeasurements[''')
        file.write(str(i))
        file.write('''].capacity);
                    if (binMeasurements[''')
        file.write(str(i))
        file.write('''].commodityCode == "0"){
                        document.write("-")}''')
        file.write('''else {
            fill = fill * 100;document.write(Math.round(fill)+ "%")}
                </script>
            </td> \n''')

# HAP COLUMN
    # binList = []
        #HAPbinList = []
    #
    # for bin in binMeasurements:
    #     binList.append(str(bin[0]).strip())
    #
        # for bin in HAPbins:
        #     HAPbinList.append(str(bin[0]).strip())
        #
        # for listItem in HAPbinList:
        file.write(''' <!-- HAP COLUMN  -->
            <td>
                <script>
                    binMeasurements = fillTable();
                    HAPbins = hasHAP();
                    for(var j = 0; j < HAPbins.length; j++){
                        if(binMeasurements[''')
        file.write(str(i))
        file.write('''].bin == HAPbins[j] ){
                            document.write(' <button type="button" class="btn btn-secondary btn-lg" data-toggle="modal" data-target="#view''')
        file.write(str(i))
        file.write('''"> View </button> <div class="modal fade" id="view''')
        file.write(str(i))
        file.write('''" role="dialog"><div class="modal-dialog modal-xl"><div class="modal-content"><div class="modal-header"><h4 class="modal-title viewButtonModalTitle"> Bin ' + HAPbins[j] + '</h4></div>'); \n''')

# view button's modal body
        file.write('''//START MODAL BODY FOR VIEW BUTTON
                            document.write('<div class="modal-body">'); \n''')
        file.write('''//CALENDER
                            var dateField''')
        file.write(str(i))
        file.write(''' = "dateField''')
        file.write(str(i) + '''" ;''')
        file.write('''
                            document.write('DATE: <input type = "date" id = "dateField''')
        file.write(str(i))
        file.write('''" name = "datefield" onchange="populateSensors(dateField''')
        file.write(str(i))
        file.write(''', binMeasurements[''')
        file.write(str(i))
        file.write('''].bin)"> <br>'); \n''')

        max = 0
        for date in dates:
            max = max + 1

        file.write('''//RANGE SLIDER
                            var rangeValue''')
        file.write(str(i))
        file.write(''' = "rangeValue''')
        file.write(str(i) + '''" ;''')
        file.write('''
                            document.write('<input type="range" id="rangeValue''')
        file.write(str(i))
        file.write('''" value="0" max = "''')
        file.write(str(max) + '"')
        file.write(''' oninput="rangeSlider(rangeValue''')
        file.write(str(i))
        file.write(''', dateField''')
        file.write(str(i))
        file.write(''', binMeasurements[''')
        file.write(str(i))
        file.write('''].bin)"> <br>'); \n''')
        file.write('''
                            document.write('<div class = "binRoof"></div><div class = "bin"><div class = "ch6">6</div> <div class = "ch14">14</div><div class = "ch7">7</div><div class = "ch5">5</div><div class = "ch13">13</div><div class = "ch1">1</div><div class = "ch4">4</div><div class = "ch2">2</div><div class = "ch12">12</div><div class = "ch8">8</div><div class = "ch13">13</div><div class = "ch11">11</div><div class = "ch10">10</div><div class = "ch10">10</div> '); \n''')

# start grain area in bin
        file.write('''//START GRAIN AREA
                            document.write('<div class = "grain">');\n\n''')

        file.write('''
                            document.write('<div class = "c6">''')
        for i in reversed(range(81,107)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                            document.write('<div class = "c14">''')
        for i in reversed(range(2010,225)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                            document.write('<div class = "c7">''')
        for i in reversed(range(107,113)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                            document.write('<div class = "c5">''')
        for i in reversed(range(65,81)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                             document.write('<div class = "c13">''')
        for i in reversed(range(1103,2010)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                            document.write('<div class = "c1">''')
        for i in reversed(range(1,17)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write('''');\n ''')

        file.write('''
                            document.write('<div class = "c4">''')
        for i in reversed(range(410,65)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write('''');\n ''')

        file.write('''
                            document.write('<div class = "c2">''')
        for i in reversed(range(17,33)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                            document.write('<div class = "c12">''')
        for i in reversed(range(177,1103)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write('''');\n ''')

        file.write('''
                            document.write('<div class = "c8">''')
        for i in reversed(range(113,1210)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                            document.write('<div class = "c3">''')
        for i in reversed(range(33,410)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                            document.write('<div class = "c10">''')
        for i in reversed(range(1210,145)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                            document.write('<div class = "c11">''')
        for i in reversed(range(161,177)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write('''');\n ''')

        file.write('''
                            document.write('<div class = "c10">''')
        for i in reversed(range(145,161)):
            file.write('''<div class = "cs''')
            file.write(str(i))
            file.write('''"> - </div>''')
        file.write('''"</div>''')
        file.write(''''); \n''')

        file.write('''
                            document.write('</div> '); \n''') # end of grain area
        file.write('''
                            document.write('</div> '); \n''') # end of bin
        file.write('''
                            document.write('</div>'); \n''') # end of mod body
        file.write('''
                            document.write('<div class="modal-footer"><button type="button" class="btn btn-default" data-dismiss="modal" onclick = "clearBin()">Close</button></div></div></div></div>');\n''')

        file.write('''
                    }
                        }

                    </script>
                </td>
     </tr>\n''')

    file.write(''' </tbody>
         </table>
         </div>\n\n''') # end of table container

    file.write('''<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>''')
    file.write('</body>  \n')
    file.write('</html>  \n')

# ________ WRITE JAVASCRIPT FILE ________
with open('WintersetHome.js','w') as file:

# function to get all the rows of data for all the bins on all dates
    file.write("function HAPdata(){ \n")
    file.write('     var rows = [ \n')
    for row in rows:
        file.write("         {")
        file.write(" bin : " + '"' + row[2].strip() + '"' + ",")
        file.write(" cable : " + '"' + str(row[3]).strip() + '"' + ",")
        file.write(" sensor : " + '"' + str(row[4]).strip() + '"' + ",")
        file.write(" date : " + '"' + str(row[5]).strip() + '"' + ",")
        file.write(" avgTemp : " + '"' + str(row[6]).strip() + '"' )
        file.write("}, \n")
    file.write('     ]\n')
    file.write('    return rows;\n')
    file.write('} \n\n')

# displays overview of stats for all Bins in table
    file.write('function fillTable(){ \n')
    file.write('     var binMeasurements = [ \n')

    for bin in binMeasurements:
        file.write("         {")
        file.write("bin : " + '"' + str(bin[0]).strip() + '"' + ",")
        file.write(" capacity : " + '"' + str(bin[1]).strip() + '"' + ",")
        file.write(" currentHoldings : " + '"' + str(bin[2]).strip() + '"' + ",")
        file.write(" willHold : " + '"' + str(bin[3]).strip() + '"' + ",")
        file.write(" commodityCode : " + '"' + str(bin[4]).strip() + '"' + ",")
        file.write(" measureDate : " + '"' + str(bin[5]).strip() + '"' + ",")
        file.write("}, \n")
    file.write('     ]\n\n')
    file.write('     return binMeasurements;\n')
    file.write('}\n \n')

# list of HAP Bins
    file.write('function hasHAP(){ \n')
    file.write('     HAPbins = [ ')
    for bin in HAPbins:
        file.write( '"' + str(bin[0]).strip() + '"' + ',' )
    file.write('];\n ')
    file.write('return HAPbins;\n')
    file.write('     }\n\n')

# select date function
    file.write('''function selectDate(id){
        var selectedDate = document.getElementById(id).value;
        return selectedDate;
    } \n\n''')

# function to get list of dates for the slider to work
    file.write('function rangeSlider(rangeId, dateFieldId, binNum){ \n')
    varNum = 0
    file.write('     var selectedRangeNum = document.getElementById(rangeId).value; \n')
    file.write('     var dates = [ \n')
    for date in dates:
        file.write('         {rangeNum :')
        file.write( '"' + str(varNum) + '" ,')
        file.write(' date : ')
        file.write( '"' +str(date[0]).strip() +  '"'  + '}, \n' )
        varNum = varNum + 1
    file.write('     ] \n\n')
    file.write('''
        for(var i = 0; i < dates.length; i++){
            if(dates[i].rangeNum == selectedRangeNum){
                document.getElementById(dateFieldId).value = dates[i].date;
            }
    } \n''')
    file.write('     populateSensors(dateFieldId, binNum);\n')
    file.write('} \n\n')


# function to fill in the numbers on the sensors
    file.write("function populateSensors(dateFieldId, binNum){ \n")
    file.write('     var selectedDate = selectDate(dateFieldId); \n ')
    file.write('     var selectedBin = binNum; \n\n')

    file.write('     rows = HAPdata(); \n\n ')

    file.write('     var wantedRows = []; \n ')
    file.write('     var cableNum = [];  \n ')
    file.write('     var temp = [];  \n\n ')

    file.write('     for (var i = 0; i < rows.length; i++){\n')
    file.write('          if (rows[i].date == selectedDate && rows[i].bin == selectedBin){\n')
    file.write('               wantedRows.push(rows[i]);\n')
    file.write('          } \n')
    file.write('      }\n\n')

    file.write('     for (var i = 0; i < wantedRows.length; i++){\n')
    file.write('          cableNum.push(wantedRows[i].cable);\n')
    file.write('          temp.push(wantedRows[i].avgTemp);\n')
    file.write('     }\n\n')

    for i in range (1,17):
        file.write('     var numSensorsOn_c')
        file.write(str(i))
        file.write(' = 0;\n')
    file.write('\n')

    file.write('     for (var i = 0; i < cableNum.length; i++){\n')
    for i in range (1,17):
        file.write('          if (cableNum[i] == "')
        file.write(str(i))
        file.write('"){\n')
        file.write('             numSensorsOn_c')
        file.write(str(i))
        file.write(' ++;\n')
        file.write('          }\n')
    file.write('     }\n\n')

    for i in range (1,17):
        file.write('     var c')
        file.write(str(i))
        file.write(' = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"];\n')
    file.write('\n')

    for i in range (1,17):
        file.write('    for (var i = 0; i < numSensorsOn_c')
        file.write(str(i))
        file.write('; i++ ){\n')
        file.write('          c')
        file.write(str(i))
        file.write('[i] = (i+1).toString();\n')
        file.write('    }\n')
    file.write('\n')

    file.write('    var allCables = [];\n\n')

    for i in range (1,17):
        file.write('    for (var i = 0; i < c')
        file.write(str(i))
        file.write('.length; i++){\n')
        file.write('          allCables.push(c')
        file.write(str(i))
        file.write('[i]);\n')
        file.write('    }\n')
    file.write('\n')

    file.write('    var j = 0\n')
    file.write('    for (var i = 0; i < allCables.length; i++){\n')
    file.write('          if (!(allCables[i] == "-")){\n')
    file.write('               allCables[i] = temp[j];\n')
    file.write('               j++;\n')
    file.write('          }\n')
    file.write('    }\n\n')

    for i in range(224):
        file.write(''' x = document.getElementsByClassName("cs''')
        file.write(str(i+1))
        file.write('''");\n''')
        file.write('''for (let e of x) { e.innerHTML = allCables[''')
        file.write(str(i) + '''];}\n\n''')

    file.write('\n')

    file.write('    color(selectedBin, allCables);\n')
    file.write('}\n\n') #function end

# changes sensor color
    file.write('function color(selectedBin, allCables){\n')

    file.write('     var thisBin = selectedBin;\n')
    file.write('     var binMeasurements = [ \n')
    for bin in binMeasurements:
        file.write("         {")
        file.write("bin : " + '"' + str(bin[0]).strip() + '"' + ",")
        file.write(" capacity : " + '"' + str(bin[1]).strip() + '"' + ",")
        file.write(" currentHoldings : " + '"' + str(bin[2]).strip() + '"' + ",")
        file.write(" willHold : " + '"' + str(bin[3]).strip() + '"' + ",")
        file.write(" commodityCode : " + '"' + str(bin[4]).strip() + '"' + ",")
        file.write(" measureDate : " + '"' + str(bin[5]).strip() + '"' + ",")
        file.write("}, \n")
    file.write('     ]\n\n')

    file.write('     for(var i = 0; i< binMeasurements.length; i++){\n')
    file.write('               if (binMeasurements[i].bin == thisBin){\n')
    file.write('                    if(binMeasurements[i].commodityCode == "1"){\n')
    file.write('''                         const x = document.getElementsByClassName("grain");
                                        for (let e of x) { e.style.background = "rgb(214, 187, 77)"; }\n''')
    file.write('                    }\n')

    file.write('               else if(binMeasurements[i].commodityCode == "3"){ \n')
    file.write('''                        const x = document.getElementsByClassName("grain");
                         for (let e of x) { e.style.background = "#e0d8bf"; }\n''')
    file.write('               }\n')

    file.write('               else {\n')
    file.write('''                         const x = document.getElementsByClassName("grain");
                         for (let e of x) { e.style.background = "#f205ee"; }\n''')
    file.write('               }\n')
    file.write('          }\n')
    file.write('     }\n')

    file.write('   var sensor = allCables.map(Number);\n')
    file.write('   var temp100_currant = 150;\n')
    file.write('   var temp105_ruby = 105;\n')
    file.write('   var temp100_crimson = 100;\n')
    file.write('   var temp85_candy = 85;\n')
    file.write('   var temp80_fireOrange = 80;\n')
    file.write('   var temp75_apricot = 75;\n')
    file.write('   var temp70_marigold = 70;\n')
    file.write('   var temp65_pineapple = 65;\n')
    file.write('   var temp60_lime = 60;\n')
    file.write('   var temp55_chartreuse = 55 ;\n')
    file.write('   var temp50_shamrock = 50;\n')
    file.write('   var temp45_arctic = 45;\n')
    file.write('   var temp40_skyBlue = 40;\n')
    file.write('   var temp35_cerulean = 35;\n')
    file.write('   var temp30_cobalt = 30;\n')
    file.write('   var temp25_indigo = 25;\n')
    file.write('   var temp20_mauve = 20;\n')
    file.write('   var temp15_grape = 15;\n')
    file.write('   var temp10_fushcia = 10;\n')
    file.write('   var temp5_watermelon = 5;\n')
    file.write('   var temp0_rose = 0;\n')
    file.write('   var tempNeg5_flamingo = -5;\n')
    file.write('   var tempNeg10_lemonade = -10;\n')
    file.write('   var tempNeg15_blush = -15;\n')
    file.write('   var tempNeg16_white   = -20;\n\n')

    for i in range(224):
        file.write('    if (sensor[')
        file.write(str(i))
        file.write('] <= tempNeg16_white){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#ffffff"; }\n''')
        file.write('     }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= tempNeg15_blush){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#ffeff8"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= tempNeg10_lemonade){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#ffddf0"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= tempNeg5_flamingo){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#ffbbd10"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp0_rose){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#fe10cc4"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp5_watermelon){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#fe7cac"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp10_fushcia){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#ff00fe"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp15_grape){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#102278d"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp20_mauve){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#652f102"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp25_indigo){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#1a1463"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp30_cobalt){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#0000fe"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp35_cerulean){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#007fff"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp40_skyBlue){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#00cdff"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp45_arctic){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#06f8f6"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp50_shamrock){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#3ab448"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp55_chartreuse){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#7fff00"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp60_lime){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#cefe00"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp65_pineapple){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#fffe00"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp70_marigold){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#fed828"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp75_apricot){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#f6a403"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp80_fireOrange){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#f26622"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp85_candy){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#fe0000"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp100_crimson){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#d100000"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp105_ruby){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#10b0000"; }\n''')
        file.write('    }\n')

        file.write('    else if (sensor[')
        file.write(str(i))
        file.write('] <= temp100_currant){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "#7F0001"; }\n''')
        file.write('    }\n')

        file.write('    else if (isNaN(sensor[')
        file.write(str(i))
        file.write('] )){ \n')
        file.write('''          const x = document.getElementsByClassName("cs''')
        file.write(str(i+1) + '''");\n''')
        file.write('''          for (let e of x) { e.style.background = "rgba(0, 0, 0,0.0)"; }\n''')
        file.write('    }\n')
    file.write('}\n \n') #function end

# function that resents the bin graph back to empty
    file.write('''function clearBin(){\n''')
    file.write('''    x = document.getElementsByClassName("grain");
    for (let e of x) { e.style.background = "rgba(160, 160, 160, 0.3)"; }\n\n''')
    for i in range(224):
        file.write('''    x = document.getElementsByClassName("cs''')
        file.write(str(i + 1))
        file.write('''");\n''')
        file.write('''    for (let e of x){
            e.innerHTML = "-";
            e.style.background = "rgba(160, 160, 160, 0.0)";
        }\n\n''')

    file.write('''}''')
