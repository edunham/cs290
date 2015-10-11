def li(n):
    print "\t\t\t<li>Item %s</li>" % str(n)

def print_list(ul="ul"):
    print "\t\t<p>The following list is unordered:</p>"
    print "\t\t<%s>" % ul
    for i in range(3):
        li(i)
    print "\t\t</%s>" % ul
