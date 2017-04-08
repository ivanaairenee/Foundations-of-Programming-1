#Ivana Irene Thomas // 1606887352
import string
from htmlFunctions import make_HTML_word, make_HTML_box, print_HTML_file

print ("Program to create word cloud from a text file \n The result is stored as a Html File.")
print(string.punctuation)
valid = False 
while not valid: #define a loop for error exceptions  
    try:
        a = input("Please enter input file name: ") #prompt user for input file name
        inputFile = open(a, "r")
        valid = True 
    except FileNotFoundError: #define exception and error message for opening file that doesn't exist
        print ("The file", a , "doesn't exist. \n Try Again")
    except KeyboardInterrupt: #define exception and error message for KeyboardInterrupt error 
        print ("Keyboard Interrupt. Input fie is required.")
stopWords= open("stopWords.txt") #open file containing stopWords
punct=set(string.punctuation) #set a string.punctuation function to a variable
list_baru = [] #make empty lists for further uses 
list_bersih =[]


stopList = []
list_baru = []
for words in stopWords: #iterate every word in the stopWords file, remove punctuation and append them to stopList 
    words = ''.join(x for x in words if x not in punct)
    stopList.extend(words.lower().split())
for sentence in inputFile: #iterate every word in inputFile, split them into words, remove punctuation
    sentence=sentence.split()
    for kata in sentence:
        kata_baru = ''.join(x for x in kata if x not in punct and not x.isdigit())
        kata_baru = kata_baru.lower()
        list_baru.append(kata_baru) #append the words that are removed from punctuation
        
for a in list_baru: #iterate every word in the new list and, make an exception for empty strings and words from stopList, and append them to a newlist
    if a not in stopList and a !='':
        list_bersih.append(a)
counts = dict() #make a dictionary with the name counts 
for word in list_bersih: #iterate every word from list_bersih, and count its frequency using dictionary, the frequency of each word is then stored as values in the dictionary
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word] + 1

sorted_words = sorted(sorted(counts,reverse=True), key=counts.__getitem__, reverse = True) #make a new list containing dictionary that is sorted by its values

list_final = []

#make the words appear in four columns and string-format it so that it displays the right format of word and its frequency

for k in sorted_words[:50]:
      list_final.append("{}:{}".format(counts[k],k))
x=0

a=50
while a >= 0: 
    for k in list_final[x:x+4]:
        print ("{:<20s}".format(k), end="")
    x+=4
    a-=4
print()


#sort the dictionary and take the first 50 words in the dictionary 

counts = sorted(counts.items(), key=lambda x:x[1], reverse = True)[:50]

#using the provided htmlFunctions, generate HTML file for the word cloud

high_count=13
low_count=3
body=''
for word,cnt in sorted(counts):
    body = body + " " + make_HTML_word(word,cnt,high_count,low_count)
box = make_HTML_box(body)  # creates HTML in a box
print_HTML_file(box,'wordCloud')  # writes HTML to file name 'testFile.html'

print ("Please press Enter to continue...")
