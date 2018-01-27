import re
x = "From johnsol@google.com  Saturday January.He has only $10.00 ."
y = re.findall('@([^ ]*)',x)
      # starting from @ then selecting the non-space characters 0 or more till space comes.
      # ^ represent starting position.
m = re.findall('\$[0-9 .]*',x)
    # starting from $(\$ means only dollar now its a litteral character, but
    # in case of only dollar sign it represent a meta character represent matches the end of 
    # the line or end.)
    # Then zero(0) to nine(9) or dot(.) , Square brackets represents alternations , either
    # zero to nine or dot.
    # then * means zero or more.
print 'Domain : ',y , 'Ammount :', m

