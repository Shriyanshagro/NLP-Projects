# Author - Shriyansh, 201402238
#provide a file name with command
# to use this tokeniser for different answers, you need to mention question sequence in variable 'ans' below.
import fileinput
import re
import matplotlib.pyplot as plt
import sys
import random
import decimal

print 'Number of files:', len(sys.argv)-1, 'files.'
linestyle = ['dashdot','dashed','dotted','solid',':']
ans = 'c'
tokenise = []
dict = {}
if ans== 'd' or ans =='a' or ans=='c':
    dict = {1:{},2:{},3:{},4:{},5:{},6:{}}

for count in range(1,len(sys.argv)):
    totalwords = 0
    print 'File', str(sys.argv[count])
    for line in fileinput.input(files=(sys.argv[count])):
            # line = ''.join(('<s> ' , line , ' </s>'))
            #  tokeniser used in assignment1
            string = re.split(' | ?:[ -]|\,|\.* |\\n|!|\?|\)|-|\(|!|;|\[|\]|\"|',line)

            totalwords = totalwords + len(string)
            string = [x for x  in string if x!='']
            for n in range(1,2):
                words = ""

                if n> len(string):
                    n = len(string)

                for i in range(1,n+1):
                    words = string[-i]+ " " + words
                # print words
                if words in dict[n].keys():
                    dict[n][words] =  dict[n][words] + 1
                else:
                    # for smoothing already added count 1 from beginning
                    dict[n][words] = 1


    for n in range(1,2):

        # sort = list(set(dict[n].values()))
        # sort =  sorted(sort,reverse=True)
        # # print n, dict[n]
        # num = random.randint(0,len(linestyle)-1)
        # plt.plot(sort,linestyle=linestyle[num])

        # for keys in dict[n].keys():
        #     dict[n][keys] = decimal.Decimal(dict[n][keys])/decimal.Decimal(totalwords)
        #     # dict[n][keys] = (dict[n][keys]+1)/(float(totalwords+v))
        #
        # sort = list(set(dict[n].values()))
        # sort =  sorted(sort,reverse=True)
        # # print n, dict[n]
        # num = random.randint(0,len(linestyle)-1)
        # plt.plot(sort,linestyle=linestyle[num])

        print dict[n]
        v = len(dict[n])
        # print v,totalwords
        # computing probability
        for keys in dict[n].keys():
            dict[n][keys] = decimal.Decimal(dict[n][keys]+1)/decimal.Decimal(totalwords+v)
            # dict[n][keys] = (dict[n][keys]+1)/(float(totalwords+v))

        sort = list(set(dict[n].values()))
        sort =  sorted(sort,reverse=True)
        # print n, dict[n]
        num = random.randint(0,len(linestyle)-1)
        plt.plot(sort,linestyle=linestyle[num])
        plt.axis([0,20,0,0.15])
        # plt.yscale('log')
        # plt.xscale('log')
        frequency = 'frequency-'+sys.argv[count]
        plt.ylabel(frequency)
        plt.xlabel("rank")
        print sort
plt.show()
