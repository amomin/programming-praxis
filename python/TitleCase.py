################################### Title case #####################################
#
# April 12, 2016
#
# A string is titlecased when the first letter of each word is capitalized 
# and the remaining letters are lower case. For instance, the string "programming 
# PRAXIS" becomes "Programming Praxis" when titlecased.
#
# Your task is to write a function that takes a string and returns it in 
# titlecase.
#
####################################################################################

def sol1(strIn):
   words = strIn.split(" ")
   words = [x[:1].upper() + x[1:].lower() for x in words]
   return " ".join(words)

if __name__ == '__main__':
    print sol1("The Big bAD WoLfIe jUmPed oer the HOUSEANDOROF")
    print sol1("I am the model of a modern major general.")
    # Some ambiguities such as...
    print sol1("To be, or not to be.  That is the quesiton.  Whether 'tis nobler to...")
