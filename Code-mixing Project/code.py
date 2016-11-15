# provide file name along with n-gram to consider
import fileinput
import re
import sys
import operator
import matplotlib.pyplot as plt
from random import randint
# filename = raw_input("Filename: ")
# ngram = input("ngram to consider: ")
dict_word = {}
dict_seq= {}
dict_tag_given_word= {}
diff_seq = []

# for monolingual  corpus
def  monolingual(filename,ngram):

	sentence = ""
	sequence = ''
	# code for monolingual corpus
	print '------------------------------------- Data for monolingual corpus -------------------------------------'
	f=open(filename,"r")
	lines = f.readlines()
	# file=open("output.txt","w")

	for i in range(1,len(lines)):
		w=lines[i].split('\t')
		words=w[1].split(' ')
		#print words
		l1=[]
		l2=[]
		for j in range(0,len(words)):
			root=words[j].split('\\')
			hindi_word=root[0]
			word_tag=root[1]
			l1.append(hindi_word)
			l2.append(word_tag)

		final_list=[]
		tag_list=[]
		s=""
		s1=""
		for i in range(2,len(l1)):
	        # hindi fragment
			s=l1[i-2]+" "+l1[i-1]+" "+l1[i]
	        # tag sequence of 3
			s1=l2[i-2]+" "+l2[i-1]+" "+l2[i]
	        # print s,s1
	        # incorporating Hindi fragment in main dict_word
	        if s in dict_word.keys():
	            dict_word[s] =  dict_word[s] + 1
	        else:
	            # for smoothing added count 1 from beginning
	            # dict_word[s] = 2
	            dict_word[s] = 1

	        # incorporating hindi tag sequence in main dict_seq
	        if s1 in dict_seq.keys():
	            # print 'pos tag matched',s1
	            dict_seq[s1] =  dict_seq[s1] + 1
	        else:
	            # for smoothing added count 1 from beginning
	            # dict_seq[s1] = 2
	            dict_seq[s1] = 1

			# final_list.append(s)
			# tag_list.append(s1)

		# for item in final_list:
		# 	file.write(item)
		# 	file.write("\n")
	print

	print 'Fragments with their frequency >>', dict_word
	print 'total fragments>> ', len(dict_word)
	sort = list(set(dict_word.values()))
	sort =  sorted(sort,reverse=True)
	print 'Frequency of similar fragments >>', sort

	# plotting ziff's curve
	# plt.plot(sort)
	# plt.ylabel("frequency")
	# plt.xlabel("rank")
	# plt.show()

	print

	print 'Pos Sequence with their frequency>>', dict_seq
	sort = list(set(dict_seq.values()))
	sort =  sorted(sort,reverse=True)
	print 'Frequency of posseq >>', sort

	# plotting ziff's curve
	# plt.plot(sort)
	# plt.ylabel("frequency")
	# plt.xlabel("rank")
	# plt.show()

	# dict_word ={}
	# dict_seq ={}
	print

# for code-mixed data
# ngram >> grams of POS sequence,dict_seq{}
# kgram >> grams of Words sequence,dict_word{}
# word_gram >> grams of tag_given_word,dict_tag_given_word{}
def codemixed(filename,ngram,kgram,word_gram):
	print '--------------------Data of code-mixed and monolingual corpus combined------------------------'
	print
	index=0

	sentence = ""
	sequence = ''

	for line in fileinput.input(files=(filename)):
	    # print line
	    if line=="\n":
	        string = sentence.split()

	        posseq = sequence.split()
	        # print sentence,len(string)
	        string.insert(0,'<s>')
	        # print string
			#  for word sequences
	        if kgram >= len(string):
	            sentence = '<s> '+ sentence
	            if sentence in dict_word.keys():
	                dict_word[sentence] =  dict_word[sentence] + 1
	            else:
	                # for smoothing already added count 1 from beginning
	                # dict_word[sentence] = 2
					# print sentence
	                dict_word[sentence] = 1


	        else:
	            for j in range(0,len(string)-kgram+1):
	                words = ""
	                # creating individual fragments
	                for i in range(j,kgram+j):
	                    words = words + string[i] + " "


	      	        # putting the fragment into dict_word
	                if words in dict_word.keys():
	                    dict_word[words] =  dict_word[words] + 1
	                else:
	                    # for smoothing added count 1 from beginning
	                    # dict_word[words] = 2
						# print words
						dict_word[words]=1

			#  for tag sequences
	        if ngram >= len(posseq):

	            if sequence in dict_seq.keys():
	                dict_seq[sequence] =  dict_seq[sequence] + 1
	            else:
	                # for smoothing already added count 1 from beginning
	                # dict_seq[sequence] = 2
					# print sequence
	                dict_seq[sequence] = 1
	                diff_seq.append(sequence)

	        else:
	            for j in range(0,len(posseq)-ngram+1):
	                words = ""
	                # creating individual fragments
	                for i in range(j,ngram+j):
	                    words = words + posseq[i] + " "


	      	        # putting the fragment into dict_word
	                if words in dict_seq.keys():
	                    dict_seq[words] =  dict_seq[words] + 1
	                else:
	                    # for smoothing added count 1 from beginning
	                    # dict_seq[words] = 2
						# print words
						dict_seq[words]=1
						diff_seq.append(words)

			#  for words given tags sequences
	        if word_gram >= len(posseq):

	            if sequence in dict_tag_given_word.keys():
	                if sentence in dict_tag_given_word[sequence].keys() :
	                	dict_tag_given_word[sequence][sentence] = dict_tag_given_word[sequence][sentence]  + 1

	                else :
	                	dict_tag_given_word[sequence][sentence] = 1

	            else:
	                # for smoothing already added count 1 from beginning
	                # dict_tag_given_word[sequence] = 2
	                dict_tag_given_word[sequence] = {}
	                dict_tag_given_word[sequence][sentence] = 1

	        else:
	            for j in range(0,len(posseq)-word_gram+1):
	                words = ""
	                seq = ""
	                # creating individual fragments
	                for i in range(j,word_gram+j):
	                    seq = seq + posseq[i] + " "

	                for i in range(j,word_gram+j):
	                    words = words + string[i] + " "

                    if seq in dict_tag_given_word.keys():
                        if words in dict_tag_given_word[seq].keys() :
                            dict_tag_given_word[seq][words] = dict_tag_given_word[seq][words] + 1
                        else:
                            dict_tag_given_word[seq][words] = 1
                    else:
                        dict_tag_given_word[seq] = {}
                        dict_tag_given_word[seq][words] = 1

	        sentence =''
	        sequence =''

	    else:
	        string = line.split()
	        # genration of sentence from corpus
	        sentence = sentence + string[0]+' '
	        sequence = sequence + string[-1]+ ' '

	print 'Fragments with their frequency >>', dict_word
	sort = list(set(dict_word.values()))
	sort =  sorted(sort,reverse=True)
	print 'Frequency of similar fragments in decreasing sorted order >>', sort

	# # plotting ziff's curve
	# plt.plot(sort)
	# plt.ylabel("frequency")
	# plt.xlabel("rank")
	# plt.show()

	print

	print 'Postag Sequence with their frequency>>', dict_seq
	sort = list(set(dict_seq.values()))
	sort =  sorted(sort,reverse=True)
	print 'Frequency of postag sequence in decreasing sorted order >>', sort

	print 
	print "dict_tag_given_word>> ", dict_tag_given_word

	# plt.plot(sort)
	# plt.ylabel("frequency")
	# plt.xlabel("rank")
	# plt.show()

def tags_sequence(dict_temp):
	# print dict_temp
	#print "aaya"
	dict_temp = sorted(dict_temp.iteritems(), key=operator.itemgetter(1), reverse=True)
	length = len(dict_temp)
	if length>5:
		upperbound = 4
	else:
	 	upperbound = length
	number = randint(0,upperbound)
	# key =  max(dict_temp.iteritems(), key=operator.itemgetter(1))[2]
	# key = ''.join(key)
	top5 = dict_temp[:(upperbound+1)]
	# print top5
	return str(top5[number][0])


ngram = 3 # grams of tags
monolingual('hin_health_set01.txt',ngram)
codemixed('FB_HI_EN_FN.txt',ngram,2,1)

#print isinstance(dict_seq,list),219
tags_seq_string = tags_sequence(dict_seq) #returns maximum occuring sequence
#print 'tags_seq>>',tags_seq_string

sequence = tags_seq_string + ' '


for i in range(0,20):
	# splite previous occureed fragments
	tags_seq_string = tags_seq_string.split()
	flag = 0
	if len(tags_seq_string)<ngram:
		break

	temP_dict={}
	# look for all matched pair
	# print tags_seq_string


	for k in dict_seq.keys():
		# print k
		# k = str(k[0])
		seq = k
		k = k.split()
		# print sequence
		if len(k)==3 and k[0]==tags_seq_string[1] and k[1]==tags_seq_string[2]:
			temP_dict[seq] = dict_seq[seq]
			# if dict_seq[seq]>flag:
			# 	flag = dict_seq[seq]
			# 	tags_seq_string=seq
	# print 'temP_dict>> ', temP_dict


	# print isinstance(dict_seq,dict_word),245
	# print isinstance(temP_dict,list),246

	seq = tags_sequence(temP_dict)
	tags_seq_string  = seq
	seq = seq.split()
	# # print seq
	if len(seq)==ngram:
		sequence = sequence +  seq[ngram-1] + ' '
		# print sequence
	i = i+1


def genword(dict_temp):
	# print dict_temp
	#print "aaya"
	dict_temp = sorted(dict_temp.iteritems(), key=operator.itemgetter(1), reverse=True)
	length = len(dict_temp)
	if length>10:
		upperbound = 9
	else:
	 	upperbound = length
	number = randint(0,upperbound)
	# key =  max(dict_temp.iteritems(), key=operator.itemgetter(1))[2]
	# key = ''.join(key)
	top5 = dict_temp[:(upperbound+1)]
	# print top5
	return top5


key = sequence.split()
# print key
value = ['<s> ']
sequence = ''
sentence = ''
for i in range(len(key)):
	sequence = sequence + key[i] + ' '
	sentence = sentence + value[i]
	tag = str(key[i])+' '
	# print dict_tag_given_word[tag]
	word_given_tag = genword(dict_tag_given_word[tag])
	# print word_given_tag
	probability = 0
	for j in range(len(word_given_tag)):
		word_seq = value[i] + word_given_tag[j][0] + " "
		if word_seq in dict_word.keys():
			word_given_prev_word = dict_word[word_seq]
		else:
			word_given_prev_word=0
		temp_probability = word_given_prev_word*word_given_tag[j][1]
		if temp_probability>=probability:
			# print i,len(value),word_given_tag[j][0]
			if i+1==len(value):
				value.append(word_given_tag[j][0])
			else:
				value[i+1]=word_given_tag[j][0]

# print value

# print diff_seq
print 'POS sequence generated>> ', sequence
print 'sentence generated>> ', sentence
