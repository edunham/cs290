#! /usr/bin/env python2

#    Create a table that has that is 6x6 (inclusive of the header row).
#
#    The upper left cell should be empty. The others should be non-empty.
#    The table should have a caption detailing the contents of the table.
#    The table should have a header section, all the cells in this section
#        should have bold text. (This is the default for th)
#    The first column of the table should have header cells that have italic
#        text. (These should not be bold)
#    The table should have a footer section made up of two cells, one should be
#        2 columns wide, the other should be 4 columns wide.

def tr(cell, data):
    # cell is the string td or the string th
    # data is an iterable full of things with str()
    print "\t\t<tr>"
    print "\t\t\t<th>" + str(data[0]) + "</th>"
    for d in data[1:]:
        print "\t\t\t<" + cell + ">" + str(d) + "</" + cell + ">"
    print "\t\t</tr>"

print "\t<table>"
print "\t<caption>Multiplication Table</caption>"
timesby = [50,82,9,37,4]
tr("th", ['']+timesby)
for t in timesby:
    tr("td", [t]+[t * b for b in timesby])
print "\t</table>"
