import re

i = 1
last = 0

lengths = True

list = []

duplicates = []



#function which determines if input is an integer
def integer(s):

    regex = "^(0|[1-9]{1}[0-9]*)$"

    if re.search(regex, s) == None:
        return False

    return True


#function which checks whether or not input is valid
def check_input(s):

    global lengths

    s=str(s)

    if len(s) == 0:

        lengths = False

        return -3

    elif re.search("^[aA][lL]{2}$", s):
        return -2

    elif re.search("^[lL][aA][sS][tT]$", s):

        return -1

    elif not integer(s):
        return -4

    else:
        return int(s)



def find_substrings(z, string):

    global list
    global last




    y = len(list)-1

    if(z <= -1):

        print("Lexicographically last substring: "+string[last:]+"\n")

        s = "length 0: \n"
        k = 1
        while y>=0 and z < -1:

            #print("\n"+str(list[y])+"\n")

            while k <= len(string)-list[y]:
                print(s+"length "+str(k)+": "+string[list[y]:list[y]+k])
                k=k+1
                s = ""

            y=y-1


    else:


        while y>=0 and len(string)-list[y] < z:
            y=y-1

        print("length "+str(z)+": "+string[list[y]:list[y]+z])




def set_list():
    global list
    global duplicates

    i = 0

    while i < len(duplicates):

        list.append(duplicates[i])
        i=i+1

    duplicates = []




def duplicate(indices, string):

    global i
    global last
    global list
    global duplicates

    s=1

    while s <= indices and i+s<len(string) and string[i+s] == string[last+s]:
        s=s+1

    if i+s>=len(string):
        i=i+s

    elif s > indices:
        #list.append(i)
        i=i+s-1
        duplicates.append(i)
        duplicate(indices, string)

    elif string[i+s] > string[last]:
        last = i+s
        #list.append(i)
        set_list()
        list.append(last)
        i = i+s
    elif string[i+s] > string[last+s]:

        set_list()
        last = i
        #list.append(last)
        i=i+s-1
    else:
        i=i+s

    duplicates = []



loop = 0



#string = "testsfhajhnfdszsohfsoihfz"

while loop == 0:


    size = -1

    duplicates = []

    i = 1
    last = 0
    list = []
    list.append(last)

    string = input("Enter string, or enter nothing to exit: ")
    string = str(string)

    while i < len(string):

        while i < len(string)-1 and string[i] < string[last]:
            i=i+1

        if string[i] == string[last]:

            duplicates.append(i)
            duplicate(i-last, string)

        elif string[i] > string[last]:
            last=i
            #set_list()
            list.append(last)

        i=i+1

    print("Lexicographically last substring: "+string[last:]+"\n")

    lengths = True

    if check_input(string) == -3:
        loop = 1

    while lengths:
        size = input("\n\nEnter the length for the substrings (between 0 and "+str(len(string))+"), 'all' for all lengths, or 'last' for the last substring. Enter nothing to go back:")
        size = check_input(size)

        while (size <-2 or size>len(string)) and lengths:

            print("\nInvalid entry, please try again.")
            size = input("\n\nEnter the length for the substrings (between 0 and "+str(len(string))+"), 'all' for all lengths, or 'last' for the last substring. Enter nothing to go back:")
            size = check_input(size)

        if lengths:
            find_substrings(size, string)
