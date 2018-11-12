#Exercise 1.
def split(exp,size):        #def starts the function process.
    exps =[]                #this is an empty array which data can later be stored in.
    while len(exp) > size:  #[build front of house][loop][evaluate all arguments within array][while the condition is true][len is length literally][len returns length of specific string][String is bit of text to display]
        pice = exp[:size]   #[build back of house] [matrix] [prepare exp based on number of arguments.][Structure data][First to last digit]
        exps.append(pice)   #[adds the backend arguments to the array][matrix]
        exp = exp[size:]    #[last digit to first digit][complete argument to make sure all placed right on array]
    exps.append(exp)        #append adds an item to end of the list. [final build matrix graph]
    return exps
a = [2,1,3,4,7,5,9,6,8,13,12,11,10,0,15,16,14]
a.sort(reverse=False)                          #sort it out, count from lowest to biggest.
print(split(a,6))                              #split() returns list of stings after breaking it by specific separator.
#Exercise 1.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise 3.
i = 16             # == means to ask if these two are equal?
if i % 2 == 0:     #this is Modulus. % finds modulus of two integers. #Determine if there is a remainder.
    print('True' + 'int is a power of 2') #this will print statement.
else:                                     #if above statement not printed[not the answer show] do this:
    print('False' + 'int is not a power of 2') #print this statement.
#Exercise 3.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Exercise 2.
def countLetterInString(string, letter):
	count = 0
	for x in string:           # [scan independent characters in {string}]
		if x == letter:        # [if scan results are equal to {letter}] [== stands for are they the same]
			count = count + 1  # [add 1 to {count = 0}]
	return count

count = countLetterInString("AAAABBBCCDEF", "A")

print(count)
#Exercise 2.