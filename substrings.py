

i = 1
last = 0

lengths = True

list = []

duplicates = []



def digit(c):
    if c[0]!="0" and c[0]!="1" and c[0]!="2" and c[0]!= "3" and c[0]!="4" and c[0]!="5" and c[0]!="6" and c[0]!="7" and c[0]!="8" and c[0]!="9":
        return False

    return True



def integer(s):

    x = 1

    if len(s) == 0 or not digit(s[0]) or (len(s) > 1 and s[0] == "0"):
        return False

    while x < len(s):

        if not digit(s[x]):
            return False

        x=x+1

    return True


def check_input(s):

    global lengths

    s=str(s)

    if len(s) == 3 and s[0] == "a" and s[1] == "l" and s[2] == "l":
        return -1
    elif len(s) == 4 and s[0] == "e" and s[1] == "x" and s[2] == "i" and s[3] == "t":
        lengths = False
        return 0
    elif not integer(s):
        return -2
    else:
        return int(s)



def find_substrings(z, string):

    global list

    y = len(list)-1

    if(z == -1):

        print("length 0: ")

        k = 1
        while y>=0 :

            #print("\n"+str(list[y])+"\n")

            while k <= len(string)-list[y]:
                print("length "+str(k)+": "+string[list[y]:list[y]+k])
                k=k+1

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

    s=1

    while s <= indices and i+s<len(string) and string[i+s] == string[last+s] and string[i+s] <= string[last]:
        s=s+1

    if i+s>=len(string):
        i=i+s

    elif s > indices and string[i+s-1] == string[last+s-1] and i+s-1 < len(string)-1:
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
        i=i+s
    else:
        i=i+s





loop = 0



#string = "testsfhajhnfdszsohfsoihfz"

while loop == 0:


    size = -1

    i = 1
    last = 0
    list = []
    list.append(last)

    string = input("Enter string: ")
    string = str(string)

    while i < len(string):

        while i < len(string) and string[i] < string[last]:
            i=i+1

        if i < len(string)-1 and string[i] == string[last]:

            duplicates.append(i)
            duplicate(i-last, string)
        elif i < len(string) and string[i] > string[last]:
            last=i
            set_list()
            list.append(last)

        i=i+1

    print("last substring (of all lengths): \n")
    print(string[last:])

    lengths = True

    while lengths:
        size = input("\n\nEnter the length for the substrings (between 0 and "+str(len(string))+") or 'all' for all lengths:")
        size = check_input(size)

        while (size <-1 or size>len(string)) and lengths:

            print("\nInvalid entry, please try again.")
            size = input("\n\nEnter the length for the substrings (between 0 and "+str(len(string))+") or 'all' for all lengths:")
            size = check_input(size)

        if lengths:
            find_substrings(size, string)
