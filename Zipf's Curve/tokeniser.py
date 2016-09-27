# Author - Shriyansh, 201402238
# to use this tokeniser for different answers, you need to mention question sequence in variable 'ans' below.
import fileinput
import re
import matplotlib.pyplot as plt

ans = 'd'
tokenise = []
dict = {}
if ans== 'd' or ans =='a':
    dict = {1:{},2:{},3:{},4:{},5:{},6:{}}

for line in fileinput.input(files=('toke.txt')):
        line = ''.join(('<s> ' , line , ' </s>'))
        #  tokeniser used in assignment1
        string = re.split(' | ?:[ -]|\,|\.* |\\n|!|\?|\)|-|\(|!|;|\[|\]|\"|',line)
        # string = re.split(' |@| ?:[ -]|\,|\.* |\\n|!|\?|\'|#|\)|-|\(|!|;|\[|\]|\"|/|',line)

        if ans== 'b':
            string = [x for x  in string if x!='']
            for words in string:
                    if words in dict.keys():
                        dict[words] =  dict[words] + 1
                    else:
                        dict[words] =  1

        if ans== 'c':
            string = [x for x  in string if x!='']
            words =  string[-2]
            if words in dict.keys():
                dict[words] =  dict[words] + 1
            else:
                dict[words] =  1

        if ans == 'd':

            string = [x for x  in string if x!='']
            for n in range(1,7):
                words = ""

                if n> len(string):
                    n = len(string)

                for i in range(0,n):
                    words = words + string[i]+ " "
                # print words
                if words in dict[n].keys():
                    dict[n][words] =  dict[n][words] + 1
                else:
                    dict[n][words] =  1


        if ans == 'a':

            string = [x for x  in string if x!='']
            for n in range(1,7):
                words = ""

                if n> len(string):
                    n = len(string)

                for i in range(1,n+1):
                    words = string[-i]+ " " + words
                # print words
                if words in dict[n].keys():
                    dict[n][words] =  dict[n][words] + 1
                else:
                    dict[n][words] =  1



if ans == 'd':
    for n in range(1,7):

        freq = -2000
        w = ''
        for keys in dict[n].keys():
            if freq < dict[n][keys]:
                freq = dict[n][keys]
                w = keys
        print w


if ans == 'a':
    for n in range(1,7):

        print n, ':',   dict[n]
        # freq = -2000
        # w = ''
        # for keys in dict[n].keys():
        #     if freq < dict[n][keys]:
        #         freq = dict[n][keys]
        #         w = keys
        # print w


if ans == 'b':
    # print "sorting------------------------------------------"
    sort = list(set(dict.values()))
    sort =  sorted(sort,reverse=True)
    # plotting ziff's curve
    plt.plot(sort)
    plt.ylabel("frequency")
    plt.xlabel("rank")
    plt.show()

if ans == 'c':
    # print "sorting------------------------------------------"
    sort = list(set(dict.values()))
    sort =  sorted(sort,reverse=True)
    # print sort
    # plotting ziff's curve
    plt.plot(sort)
    plt.ylabel("frequency")
    plt.xlabel("rank")
    plt.show()
