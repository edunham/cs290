def input_fieldset(one, two, three):
    print """
        <fieldset>
            <label>%s Here:
                <input type="%s" name="%s_input" />
            </label>
       </fieldset>
       """ % (one, two, three)

def button(word):
    pretty = word[0].upper()+word[1:]
    print """
            <label>
                <input type="radio" name="candy" value="%s" /> %s
            </label><br>
    """ % (word, pretty)


def print_form(method):
    action = 'http://classes.engr.oregonstate.edu/eecs/winter2015/cs290-400/tools/class-content/form_tests/check_request.php'
    print """
    <form action=%s  method="%s" name = "%sform">
        <legend>Some %s Data</legend> 
    """ % (action, method, method, method)
    input_fieldset('Text','text','text')
    input_fieldset('Number','number','numerical')
    input_fieldset('Password','password','password')

    print """
        <fieldset>
            <legend>Select Between:</legend>
    """
    button("snickers")
    button("skittles")
    button("mentos")
    print """
        <input type="submit" value="Submit" />
        </fieldset>
    </form>
    """
