#! /usr/bin/env python2
import multiplicationtable
import listentries
import form

print """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>HTML/CSS Assignment</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
    <h1>edunham's HTML/CSS assignment</h1>
    <p>I balanced my desire to learn more about HTML and CSS with my hated of
       writing HTML by hand by offloading the boring, repetitive bits to some
       Python scripts that I built for this purpose. They're <a
       href="https://github.com/edunham/cs290/tree/master/html_css_assignment">
       here</a>.
    </p>
    <hr>
"""
multiplicationtable.print_table()

listentries.print_list()

print """
    <div id="outer-content">
        We interrupt our program to bring you a haiku written by a robot:
        <div id="inner-content">
            <p>0 1 1 1</p>
            <p>0 1 0 0</p> 
            <p>1 1 0 1</p>
        </div>
        It's only a haiku if you read it out loud in English, though.
    </div>
    <br>
"""

form.print_form('GET')

print "    <br>"

form.print_form('POST')

print """
    </body>
</html>
"""
