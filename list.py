list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# print type
print (type(list1))

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#List is a collection which is ordered and changeable. Allows duplicate members.#Print the second item of the list
print (thislist[1])

#negative indexing: Negative indexing means start from the end -1 refers to the last item -2 refers to the second last item etc.
print (thislist[-1])

#Ranges of index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # specifying where to start and where to end the range
print(thislist[:4])
print(thislist[2:])

#Range of Negative Indexes
print(thislist[-4:-1])

#Check if Item Exists
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
