#declarations 
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

#output
print (x)
print (y)

#more output!
print ("I said : %r." %x)
print ("I also said: '%s'." %y)

#more declarations
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#some more cool output
print (joke_evaluation %hilarious)


#some really nice declarations
w = "This is the left side of..."
e = "a string with a right side."

#ohhh output 
print (w + e)