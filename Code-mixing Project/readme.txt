Team 33- 
	Shriyansh Agrawal, 201402238
	Madhur Modi,201401084
	Shreyash Singh, 201401196


Objective of the Project -

	-To generate code-mixed sentences using existing POS Tagged monolingual and code-mixed 	  corpus

Solution our team came up with??
- Given: POS tags we need to generate sentences, so for the same we use inverse-HMM theory
		  P(S|T) = P(T|S)*P(Si|Si-1)
Detailed Solution - 
Start with Parsing and Language Modelling on 2 choosen corpus
Get the corresponding Frequency of ‘Word Sequences(For N=2)’ and ‘Tag Sequences’(Fragments, for N=3) from the corpus.
Get indiviual ‘word given Tag’(For N=1) frequency  from code-mixed corpus
Now, as we have probability of Fragments, so generate POS TAG Sequence using LM
Example - POS sequence generated>>  V_VM V_VAUX RD_PUNC PR_PRP V_VM DT N_NN V_VM RD_PUNC RD_PUNC PSP N_NN RD_PUNC PSP N_NN RD_PUNC PR_PRP RB_AMN RD_PUNC PSP JJ RD_PUNC RB_AMN
Now as we are done with genrating Tag Sequences, start generating Word Sequences using above mentioned probability equation.


Instructions TO use this code - 


CODE-MIXED Corpus - FB_HI_EN_FN.txt
Monolingual Corpus - hin_health_set01.txt

Initial Output is collected in 'out.txt' file

Run the code - 'code.py' using command - 'python code.py'

