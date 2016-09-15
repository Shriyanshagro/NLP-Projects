# Author - Shriyansh, 201402238
import fileinput
import re

tokenise = []

for line in fileinput.input(files=('Twitter Dataset.txt')):
    # if fileinput.isfirstline():
        # string = re.split(' |:|\.|\/n|',line)
        string = re.split(' | ?:[ -]|\,|\.* |\\n|!|\?|\)|-|\(|!|;|\[|\]|\"|',line)
        tokenise = string + tokenise
        # print string

print tokenise
