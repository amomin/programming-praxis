############### A Common Interview Question ###################
################### September 13, 2016  #######################
#
# https://programmingpraxis.com/2016/09/13/a-common-interview-question/
#
# 
# I’ve seen this question two or three times recently on message boards
# that provide interview questions, so I guess we ought to add it to our
# collection:
#
# Create and implement a data structure that provides
# 
# insert
# delete
# find min
# find max
# delete min
# delete max
# 
# all in O(1) time, regardless of the type of the underlying data.
# 
# Your task is to create and implement that data structure. 
#
###############################################################

############################# ANSWER #############################
#
# There is no such data structure.  If there were, you could sort arbitrary
# comparable lists in time O(n) (insert all elements in your list, then
# find_min() and delete_min() until it is empty).
#
# Such operations are possible only in situations where there is a some
# structure to the data where there is a linear sort algorithm available,
# such as a bounded radix or something.

if __name__ == '__main__':
    print "There is no such data structure."
