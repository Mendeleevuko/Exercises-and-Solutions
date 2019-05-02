#!/usr/bin/env python
# coding: utf-8

# In[28]:


week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
accum = 0
count = 0
sum_ = 0
for item in week_temps_f.split(','):
    count += 1
    sum_ = sum_ + float(item)
    accum = sum_/len(week_temps_f.split(',')) # count can be used instead of len(week_temps_f.split(',')) 
    
print(sum_)    
print(accum)


# In[26]:


addition_str = "2+5+10+20"
sum_val = 0
avg_val = 0
for num in addition_str.split('+'):
    sum_val = sum_val + int(num)
    avg_val = int(num)/len(addition_str.split('+'))
print(sum_val)    


# In[31]:


"""Create an empty list called resps. Using the list percent_rain, for each percent, 
if it is above 90, add the string ‘Bring an umbrella.’ to resps, otherwise if it is above 80, 
add the string ‘Good for the flowers?’ to resps, otherwise if it is above 50, add the string ‘Watch out for clouds!’ to resps, 
otherwise, add the string ‘Nice day!’ to resps.  """

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]
resps = list()
for percent in percent_rain:
    if (percent > 90.0):
        resps.append("Bring an umbrella.")
    elif (percent > 80.0) and (percent < 90.0):
        resps.append("Good for the flowers?")
    elif (percent > 50.0) and percent < 80.0:
        resps.append("Watch out for clouds!")
        #resps += "Watch out for clouds!"
    else:
        resps.append("Nice day!")
print(resps)


# In[34]:


"""Do not change the provided conditional statements. 
Find an integer value for x that will cause output to hold the values True and None.""" 

x =  # 64, 65, or 66
output = [] # empty list

if x > 63:
    output.append(True)
elif x > 55:
    output.append(False)
else:
    output.append("Neither")

if x > 67:
    output.append(True)
else:
    output.append(None)

output


# In[35]:


"""For each string in the list words, find the number of characters in the string. 
If the number of characters in the string is greater than 3, add 1 to the variable num_words so that 
num_words should end up with the total number of words with more than 3 characters. """

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for word in words:
    if (len(word) > 3):
        num_words += 1
num_words


# In[40]:


"""Challenge For each word in words, add ‘d’ to the end of the word if the word ends in “e” to make it past tense. 
Otherwise, add ‘ed’ to make it past tense. Save these past tense words to a list called past_tense. """

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
past_tense = []
for word in words:
    if (word[-1] == "e"):
        past_tense.append(word + "d")
    else:
        past_tense.append(word + "ed")
past_tense       


# In[36]:


x = "uk"
x = x + "o"
x


# In[43]:


"""rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) 
with every month separated by a comma. Write code to compute the number of months that have more than 3 inches of rainfall. 
Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.
.............................................
Hard-coded answers will receive no credit."""

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months = 0
for num in rainfall_mi.split(','):
    if (float(num) > 3.0):
        num_rainy_months += 1
num_rainy_months        


# In[44]:


"""The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, 
including one-letter words. Store the result in the variable same_letter_count.
.............................................
Hard-coded answers will receive no credit."""

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = 0
for word in sentence.split():
    if word[0] == word[-1]:
        same_letter_count += 1
same_letter_count        


# In[46]:


"""Write code to count the number of strings in list items that have the character w in it. 
Assign that number to the variable acc_num.
.....................................
HINT 1: Use the accumulation pattern!
HINT 2: the "in" operator checks whether a substring is present in a string.
Hard-coded answers will receive no credit."""

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for item in items:
    if "w" in item:
        acc_num = acc_num + 1
acc_num        


# In[47]:


"""Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.
Note 1: be sure to not double-count words that contain both an a and an e.
HINT 1: Use the "in" operator.
HINT 2: You can either use "or" or "elif".
Hard-coded answers will receive no credit."""

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
for word in sentence.split():
    if ("a" in word) or ("e" in word):
        num_a_or_e += 1
num_a_or_e        


# In[53]:


"""Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. 
For this problem, vowels are only a, e, i, o, and u.
......................................
Hint: use the in operator with vowels. """

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0
for word in s:
    if word in vowels:
        num_vowels = num_vowels + 1
num_vowels  
#id(num_vowels) #identifier


# In[54]:


a = 5
b = 9
setStr = 'The set is {{{}, {}}}.'.format(a, b)
print(setStr)


# In[55]:


x = 2
y = 6
print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))


# In[56]:


v = 2.34567
print('{:.1f} {:.2f} {:.7f}'.format(v, v, v))


# In[58]:


"""Write code to add ‘horseback riding’ to the third position (i.e., right before volleyball) in the list sports."""
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports[2:2] = ["horseback riding"]
sports


# In[73]:


"""Write code to take ‘London’ out of the list trav_dest. """

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
"""First method"""
# trav_dest.pop(-2) # This will return the removed item and can be captured e.g. poped_item = trav_dest.pop(-2)
"""Second method"""
# trav_dest.index('London')
# del trav_dest[7]
"""..........Alternative to first and second methods"""
trav_dest.remove('London')
trav_dest


# In[76]:


"""Write code to add ‘Guadalajara’ to the end of the list trav_dest using a list method. """

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest += ['Guadalajara']
"""... alternative method"""
#trav_dest.append('Guadalajara')
trav_dest


# In[78]:


"""Write code to rearrange the strings in the list winners so that they are in alphabetical order from A to Z."""

winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()
winners


# In[84]:


"""Write code to switch the order of the winners list so that it is now Z to A. Assign this list to the variable z_winners. """

winners = ['Alice Munro', 'Alvin E. Roth', 'Kazuo Ishiguro', 'Malala Yousafzai', 'Rainer Weiss', 'Youyou Tu']
winners.reverse()
z_winners = winners
z_winners


# In[86]:


"""For each word in the list verbs, add an -ing ending. Save this new list in a new list, ing."""

verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for verb in verbs:
    ing.append(verb + 'ing')
ing


# In[88]:


"""Given the list of numbers, numbs, create a new list of those same numbers increased by 5. Save this new list to the variable newlist. """

numbs = [5, 10, 15, 20, 25]
newlist = list()
for numb in numbs:
    newlist.append(numb + 5)
numb    
    


# In[132]:


"""Challenge Now do the same as in the previous problem, but do not create a new list. 
Overwrite the list numbs so that each of the original numbers are increased by 5. """

numbs = [5, 10, 15, 20, 25]
count = 0
for numb in numbs:
    numbs[count] = numb + 5
    count += 1
numbs    


# In[111]:


"""For each number in lst_nums, multiply that number by 2 and append it to a new list called larger_nums."""

lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]
larger_nums = []
for num in lst_nums:
    larger_nums.append(num*2)
larger_nums    


# In[140]:


"""For each character in the string already saved in the variable str1, add each character to a list called chars."""

str1 = "I love python"
# chars = []
# for letter in str1:
#     if letter != ' ':
#         chars += letter  
# chars    

""".....Alternative method"""
# chars = []
# for letter in str1:
#     chars += letter  
# chars 

"""....Another method"""
chars = []
for letter in str1:
    chars.append(letter)   
chars 


# In[142]:


"""Assign an empty string to the variable output. Using the range function, write code to make it so that the variable output has 35 a s inside it (like "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"). 
Hint: use the accumulation pattern!"""

output = ''
for str1 in range(35):
    output = output + "a"
output    


# In[143]:


"""Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1. 
Each character in str1 should be its own element in the list chars. """

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = list()
for letter in str1:
    chars += letter
chars    


# In[149]:


"""Below are a set of scores that students have received in the past semester. 
Write code to determine how many are 90 or above and assign that result to the value a_scores."""

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = 0
for score in scores.split():
    #print(type(score))
    if int(score) >= 90:
        a_scores += 1
a_scores        
    


# In[191]:


"""Write code that uses the string stored in "org" and creates an acronym which is assigned to the variable "acro". 
Only the first letter of each word should be used, each letter in the acronym should be a capital letter, 
and there should be nothing to separate the letters of the acronym. Words that should not be included in the 
acronym are stored in the list "stopwords". For example, if org was assigned the string “hello to world” then the 
resulting acronym should be “HW”."""

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ''
for letter in org.split():
    #print(letter)
     if letter[0] not in stopwords:
        #print(letter[0])
        acro += letter[0].upper()
      
                       
acro 
#stopwords
#acro.lower() in stopwords


# In[210]:


"""Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro. 
The first two letters of each word should be used, each letter in the acronym should be a capital letter, 
and each element of the acronym should be separated by a “. ” (dot and space). 
Words that should not be included in the acronym are stored in the list stopwords. 
For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”. """

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""
for wrd in sent.split():
    if wrd[0:2] not in stopwords:
        #print(wrd[0:2])
        acro += wrd[0:2] + ". " 

acro        


# In[260]:


"""A palindrome is a phrase that, if reversed, would read the exact same. 
Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. 
Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work. """

p_phrase = "was it a car or a cat I saw"
phrase_list = []
for wrd in p_phrase.split():
    #r_phrase += (wrd + ' ')
    phrase_list.append(wrd)
phrase_list.reverse() 
rr_phrase = ' '.join(phrase_list)
rr_phrase
 


# In[267]:


"""Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, 
how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). 
For example, the first print statment should read '**The store has 12 shoes, each for 29.99 USD.**'"""

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for invent in inventory:
    
    article = (invent.split(','))[0]
    num_invent = (invent.split(','))[1]
    cost_invent = (invent.split(','))[2]
    
#     print(article)
#     print(num_invent)
#     print(cost_invent)

    print("The store has{} {}, each for{} USD.".format(num_invent, article, cost_invent))

    


# In[276]:


"""A palindrome is a phrase that, if reversed, would read the exact same. 
Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original. 
Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work. """

p_phrase = "was it a car or a cat I saw"
r_phrase = ''
for wrd in p_phrase.split():
    r_phrase += (wrd + ' ')
r_phrase    


# In[282]:


"""Code counts the number of characters in string "rv" and assigns it to variable "num_chars" """

rv = """Once upon a midnight dreary, while I pondered, weak and weary,
    Over many a quaint and curious volume of forgotten lore,
    While I nodded, nearly napping, suddenly there came a tapping,
    As of some one gently rapping, rapping at my chamber door.
    'Tis some visitor, I muttered, tapping at my chamber door;
    Only this and nothing more."""

count = 0 
for chars in rv:
    count += 1
    num_chars = count

    
num_chars, count    


# In[ ]:


#"""Files Handling in Python"""
## File content
"""This summer I will be travelling.
I will go to...
Italy: Rome
Greece: Athens
England: London, Manchester
France: Paris, Nice, Lyon
Spain: Madrid, Barcelona, Granada
Austria: Vienna
I will probably not even want to come back!
However, I wonder how I will get by with all the different languages.
I only know English!"""
'''.............................'''
"""The textfile, "travel_plans.txt", contains the summer travel plans for someone with some commentary. 
Find the total number of characters in the file and save to the variable "num". """

fileref = open("travel_plans.txt","r")
contents = fileref.read()
num = len(contents)
print(num)


# In[ ]:


# File content
"""Sad upset blue down melancholy somber bitter troubled
Angry mad enraged irate irritable wrathful outraged infuriated
Happy cheerful content elated joyous delighted lively glad
Confused disoriented puzzled perplexed dazed befuddled
Excited eager thrilled delighted
Scared afraid fearful panicked terrified petrified startled
Nervous anxious jittery jumpy tense uneasy apprehensive"""
'''.....................................'''
"""We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
Find the total number of words in the file and assign this value to the variable num_words. """

fileref = open("emotion_words.txt","r")
contents = fileref.read().strip().split()
num_words = len(contents)
print(len(contents))


# In[ ]:


# File content
"""Writing essays for school can be difficult but
many students find that by researching their topic that they
have more to say and are better informed. Here are the university
we require many undergraduate students to take a first year writing requirement
so that they can
have a solid foundation for their writing skills. This comes
in handy for many students.
Different schools have different requirements, but everyone uses
writing at some point in their academic career, be it essays, research papers,
technical write ups, or scripts."""
'''..........................................'''

"""Assign to the variable num_lines the number of lines in the file school_prompt.txt. """
file_obj = open("school_prompt.txt","r")
contents = file_obj.readlines()
num_lines = len(contents)
print(num_lines)


# In[ ]:


"""Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars. """

file_obj = open("school_prompt.txt","r")
contents = file_obj.read()
beginning_chars = contents[:30]
print(beginning_chars)


# In[ ]:


"""Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three. """

file_obj = open("school_prompt.txt","r")
contents = file_obj.readlines()
#print(contents)
three = []
for lines in contents:
    rows = lines.strip().split()
    # the lines are shown
    print(rows)
    
    # to get the index of each line
    lines_index = contents.index(lines)
    print("+++",lines_index,"+++")
    
    # Third word of every line
    print("***",rows[2],"****")
    three.append(rows[2])


# In[ ]:


"""Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt."""
file_obj = open("emotion_words.txt","r")
contents = file_obj.readlines()
#print(contents)
emotions = list()
for lines in contents:
    line = lines.strip().split()
    #print(line)
    # To grab the first word in each line
    first_word = line[0]
    print("***",first_word,"***")
    emotions.append(first_word)


# In[ ]:


"""Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars."""

file_obj = open("travel_plans.txt","r")
contents = file_obj.read()
first_chars = contents[:33]


# In[ ]:


"""Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words. """

file_obj = open("school_prompt.txt","r")
contents = file_obj.read().strip().split()
#print(contents)
p_words = []
for word in contents:
    if "p" in word:
        words = word
        p_words.append(words)
        #print(words)
print(p_words)


# In[ ]:


# File content
"""joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89"""
"""......................................"""
"""The following sample file called studentdata.txt contains one line for each student in an imaginary class. 
The students name is the first thing on each line, followed by some exam scores. 
The number of scores might be different for each student."""

"""Using the text file studentdata.txt write a program that prints out the names of students that have more than six quiz scores."""


# Hint: first see if you can write a program that just prints out the number of scores on each line
# Then, make it print the number only if the number is at least six
# Then, switch it to printing the name instead of the number
file_obj = open("studentdata.txt","r")
contents = file_obj.readlines()
#print(contents)

for score in contents:
    score_ = score.strip().split()
    #print(score_)
    if len(score_[1:]) > 6:
        print(score_[0])
file_obj.close()


# In[ ]:


# File content is already in one of the above lines
"""Create a list called destination using the data stored in travel_plans.txt. 
Each element of the list should contain a line from the file that lists a country and cities inside that country. 
Hint: each line that has this information also has a colon : in it. """

file_obj = open("travel_plans.txt","r")
contents = file_obj.read()
#print(contents)
destination = list()
for line in file_obj:
    lines = line.strip()
    #print(lines)
    if ":" in lines:
        #print(lines)
        destination.append((lines)+ "\n")
print(destination)
file_obj.close()


# In[ ]:


# File content already in use above
"""Create a list called j_emotions that contains every word in emotion_words.txt that begins with the letter “j”. """
file_obj = open("emotion_words.txt","r")
contents = file_obj.readlines()
#print(contents)
j_emotions = []
for line in contents:
    lines = line.strip().split()
    #print(lines)
    #print(type(lines))
    for word in lines:
        if word[0] == "j":
            #print(word)
            j_emotions.append(word)

"""Best approach"""
contents = file_obj.strip().split()
j_emotions = list()
for word in contents:
    if word[0] == "j":
        j_emotions.append(word)
        print(word)
file_obj.close()


# In[ ]:


# File content used above 
"""The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. 
Find the total number of characters in the file and save to the variable num. """

file_obj = open("travel_plans.txt","r")
contents = file_obj.read()#.strip()
#print(contents)
num = len(contents)
print("Total number of characters in the text file is", num)


# In[ ]:


# File content used above 
"""We have provided a file called emotion_words.txt that contains lines of words that describe emotions. 
Find the total number of words in the file and assign this value to the variable num_words. """

fileref = open("emotion_words.txt","r")
contents = fileref.read().strip().split()
#print(contents)
num_words = len(contents)
print("Total number of words in the text file is",num_words)


# In[ ]:


# File content used above 
"""Assign to the variable num_lines the number of lines in the file school_prompt.txt. """

file_obj = open("school_prompt.txt","r")
contents = file_obj.readlines()
#print(contents)
num_lines = len(contents)
print("Total number of lines in the text file is", num_lines)


# In[ ]:


# File content used above 
"""Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars."""

file_obj = open("school_prompt.txt", "r")
contents = file_obj.read()
#print(contents)
beginning_chars = contents[:30]
print("The first thirty characters of the text file is '{}'.".format(beginning_chars))


# In[ ]:


# File content used above
"""Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three. """

file_obj = open("school_prompt.txt","r")
contents = file_obj.readlines()
#print(contents)
three = list()
for word in contents:
    words = word.strip().split()
    #print(type(words))
    #print(words)
    print(words[2])
    three.append(words[2])


# In[ ]:


# File content used above
"""Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt. """

file_obj = open("emotion_words.txt","r")
contents = file_obj.readlines()
#print(contents)
emotions = []
for word in contents:
    words = word.strip().split()
    #print(words)
    print(words[0])
    emotions.append(words[0])


# In[ ]:


# File content used above
"""Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars. """
fileref =open("travel_plans.txt","r")
contents = fileref.read()
#print(contents)
first_chars = (contents[:33])
print(first_chars)


# In[ ]:


# File content used above 
"""Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words. """
file_obj = open("school_prompt.txt", "r")
contents = file_obj.read().strip().split()
#print(contents)
p_words = []
for word in contents:
    if "p" in word:
        print(word)
        p_words.append(word)


# In[283]:


# Dictionaries in Python
"""Create a dictionary that keeps track of the USA’s Olympic medal count. 
Each key of the dictionary should be the type of medal (gold, silver, or bronze) and each key’s value should be the number 
of that type of medal the USA’s won. Currently, the USA has 33 gold medals, 17 silver, and 12 bronze. 
Create a dictionary saved in the variable medals that reflects this information. """
medals = {"gold":33,"silver":17,"bronze":12}
medals


# In[287]:


"""You are keeping track of olympic medals for Italy in the 2016 Rio Summer Olympics! 
At the moment, Italy has 7 gold medals, 8 silver metals, and 6 bronze medals. 
Create a dictionary called olympics where the keys are the types of medals, 
and the values are the number of that type of medals that Italy has won so far."""
olympics = {"gold":7}
olympics["silver"]= 8
olympics['bronze'] = 6
olympics


# In[301]:


mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print("***Before deleting the key 'dog'\n",mydict)
print("***The numbers of mouse :",mydict["mouse"])

#
dict_2 = len(mydict)
print("*** dict_2 :",dict_2)
# To delete a value
del mydict['dog']


# In[290]:


"""Update the value for “Phelps” in the dictionary swimmers to include his medals from the Rio Olympics 
by adding 5 to the current value (Phelps will now have 28 total medals). Do not rewrite the dictionary. """

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers['Phelps'] += 5 # swimmers["Phelps"] = swimmers['Phelps'] + 5
swimmers


# In[326]:


swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
for key in swimmers.keys():
    #print(key)
    print("The key name",key,"is associated with value {}".format(swimmers[key]))

ks = swimmers.keys() 
#type(ks)
ks
# To get the dictionary keys as list
ky = list(swimmers.keys())
ky
# To get the dictionary values as list
vl = list(swimmers.values())
vl
# To get the dictionary keys as tuple
tp = swimmers.items()
tp
# get it in as list of tuples
tup = list(swimmers.items())
#print(tup)
#tup[0][1]


# In[330]:


mydic = {"cat":12, "dog":6, "elephant":23}
for key in mydic:
    print(key)# to get the keys
    #print(mydic[key])# to get the values
    
if 'elephant' in mydic:
    print(mydic["elephant"])
else:
    print("We have none")


# In[339]:


medals = {"gold":33,"silver":17,"bronze":12}
print(medals.get("gold"))
print(medals.get("precious_stone"))# this would not return error even though its not in dictionary
#print(medals["precious_stone"])# this would throw back error

print(medals.get("platinum", 0)) # if key is not in dictionary, return the value 0 or any value that is after the key "platinum"
print(medals.get("silver", 40)) # if key exist, it would return its associated value regardless what is currently given as an option here


# In[340]:


mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
answer = mydict.get("cat")//mydict.get("dog")
print(answer)


# In[ ]:


total = 0
mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
for akey in mydict:
   if len(akey) > 3:
      total = total + mydict[akey]
print(total)


# In[341]:


"""Every four years, the summer Olympics are held in a different country. 
Add a key-value pair to the dictionary places that reflects that the 2016 Olympics were held in Brazil. 
Do not rewrite the entire dictionary to do this! """
places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
places["Brazil"] = 2016
places


# In[342]:


"""We have a dictionary of the specific events that Italy has won medals in and the number of medals they have won 
for each event. Assign to the variable events a list of the keys from the dictionary medal_events. Do not hard code this. """

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}
events = list(medal_events.keys())
events


# In[345]:


# To make an alias of dictionary would mean a change in the alias would change the original 
alias = mydic
print(alias is mydic)

# To create a copy of original dictionary
acopy = medals.copy()
acopy # Any change in dictionary acopy would not affect the original dictionary medals


# In[347]:


"""At the halfway point during the Rio Olympics, the United States had 70 medals, 
Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany had 17 medals. 
Create a dictionary assigned to the variable medal_count with the country names as the keys and the number of medals 
the country had as each key’s value. """

medal_count = {}
medal_count["United States"] = 70
medal_count["Great Britain"] = 38
medal_count["China"] = 45
medal_count["Russia"] = 30
medal_count["Germany"] = 17

print(medal_count)


# In[348]:


"""Not yet graded
Given the dictionary swiddlers, add an additional key-value pair to the dictionary with "Phelps" as the key and the integer 23 as the value. 
Do not rewrite the entire dictionary. """

swiddlers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
swiddlers["Phelps"] = 23
print(swiddlers)


# In[349]:


"""Add the string “hockey” as a key to the dictionary sports_periods and assign it the value of 3. 
Do not rewrite the entire dictionary."""

sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods["hockey"] = 3
sports_periods


# In[350]:


"""The dictionary golds contains information about how many gold medals each country won in the 2016 Olympics. But today, Spain won 2 more gold medals. 
Update golds to reflect this information. """

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds["Spain"] = golds["Spain"] + 2

golds


# In[353]:


"""Create a list of the countries that are in the dictionary golds, and assign that list to the variable name countries. 
Do not hard code this."""

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = list(golds.keys())
#type(countries)
countries


# In[354]:


"""Provided is the dictionary, medal_count, which lists countries and their respective medal count at the halfway point in 
the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for "Belarus" to the variable belarus. 
Do not hardcode this. """

medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}
belarus = medal_count["Belarus"]
belarus


# In[357]:


"""The dictionary total_golds contains the total number of gold medals that countries have won over the course of history. 
Use dictionary mechanics to find the number of golds Chile has won, and assign that number to the variable name chile_golds. 
Do not hard code this! """

total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
#print(total_golds)
chile_golds = total_golds["Chile"]
chile_golds


# In[358]:


"""Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016, 
and in which category they have won it in. Using dictionary mechanics, assign the value of the key "Fencing" to a variable fencing_value. 
Remember, do not hard code this. """

US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}
fencing_value = US_medals["Fencing"]
fencing_value


# In[370]:


file_obj = open("test.txt","r")
contents = file_obj.read() # long string of the file content
#contents.strip()
text = {}
for txt in contents.strip():
    if txt not in text:
        text[txt] = 0
    # whether we've seen it before    
    text[txt] = text[txt] + 1 
text    


# In[375]:


sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
word_count = dict()
ss = sentence.split()
ss
for word in ss: # instead of ss, see the second code
    if word not in word_count:
        word_count[word] = 0
    word_count[word] = word_count[word] + 1
word_count   

# Second best method
word_accum = {}
for word in sentence.split():
    if word not in word_accum:
        word_accum[word] = 0
    word_accum[word] = word_accum[word] + 1
word_accum    


# In[388]:


stri = "what can i do"
chars = stri.split() # I had to rip the spaces 
#print(chars)
char_join = "".join(chars)# if the "stri" is used in place of "chars", then, spaces would be counted. you could test it by commenting on line 2 and using "stri" instead of "chars"
#print(char_join)

char_d = {}
for char in char_join:# if "stri" is used instead of "char_join", then spaces would be counted
    if char not in char_d:
        char_d[char] = 0
    char_d[char] += 1
char_d


# In[392]:


"""The dictionary "travel" contains the number of countries within each continent that Uko has traveled to. 
Find the total number of countries that Uko has been to, and save this number to the variable name 'total'. Do not hard code this."""

travel = { "North America": 2, "Europe": 8, "South America": 3, "Asis": 4, "Africa": 1, "Antarctica": 0, "Australia": 1}
total = 0
for num in travel:
    #print(travel[num])
    total = total + travel[num]
total    


# In[421]:


placement = "Beaches are cool places to visit in spring however the Mackinaw brindge is near. Most people visit Mackinaw later since the island is a cool place to explore."

d = dict()
for char in placement:
    if char not in d:
        d[char] = 0
    d[char] = d[char] + 1
print(d)   


chars = list(d.keys())
#print(chars)
min_value = chars[0]
for key in chars:
    if d[key]<d[min_value]:
        min_value = key
min_value        


# In[416]:


"""Craete a dictionary called lett_d that keeps track of all the characters in the string product and notes how many times
each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value"""

product = "iphone and android phones"

lett_d = {}

for c in product:
    if c not in lett_d:
        lett_d[c] = 0
    lett_d[c] = lett_d[c] + 1
print(lett_d)    

chars = list(lett_d.keys())# Create a list out of the dictionary 'lett_d'
max_value = chars[0]# assign the first character in chars to variable name max_value

for char in chars:# iterate through the list created 
    if lett_d[char] > lett_d[max_value]:
        max_value = char
max_value        


# In[418]:


"""The dictionary travel contains the number of countries within each continent that Jackie has traveled to. 
Find the total number of countries that Jackie has been to, and save this number to the variable name total. 
Do not hard code this! """

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
total = 0

for key in travel:
    total = total + travel[key] 
total     


# In[420]:


"""schedule is a dictionary where a class name is a key and its value is how many credits it was worth. 
Go through and accumulate the total number of credits that have been earned so far and assign that to 
the variable total_credits. Do not hardcode."""
schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}

total_credits = 0
for key in schedule:
    total_credits = total_credits + schedule[key]
print(total_credits)    


# In[ ]:


"""Write a program that finds the key in a dictionary that has the maximum value. If two keys have the same maximum value, 
it’s OK to print out either one. Fill in the skeleton code"""

d = {'a': 194, 'b': 54, 'c':34, 'd': 44, 'e': 312, 'full':31}

ks = d.keys()
best_key_so_far = ks[0]# initialize variable best_key_so_far to be the first key in d
for k in ks:
    if d[k] > d[best_key_so_far]:
        best_key_so_far = k
    # check if the value associated with the current key is
    # bigger than the value associated with the best_key_so_far
    # if so, save the current key as the best so far

print("key " + best_key_so_far + " has the highest value, " + str(d[best_key_so_far]))


# In[422]:


"""Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times 
each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value."""

placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
d = dict()
for char in placement:
    if char not in d:
        d[char] = 0
    d[char] = d[char] + 1
#print(d)    
keys = list(d.keys())
min_value = keys[0]

for key in keys:
    if d[key] < d[min_value]:
        min_value = key
print(min_value)


# In[ ]:


"""Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many 
times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value. """

product = "iphone and android phones"

lett_d = {}
for char in product:
    if char not in lett_d:
        lett_d[char] = 0
    lett_d[char] = lett_d[char] + 1
#print(lett_d)

keys = list(lett_d.keys())
max_value = keys[0]

for key in keys:
    if lett_d[key] > lett_d[max_value]:
        max_value = key
print(max_value)        


# In[ ]:


"""The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the 
number of credits. Find the total number of credits taken this semester and assign it to the variable credits. 
Do not hardcode this – use dictionary accumulation! """

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for course in Junior:
    credits = credits + Junior[course]
pritn(credits)


# In[ ]:


"""Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value. """

str1 = "peter piper picked a peck of pickled peppers"
freq = dict()
for char in str1:
    if char not in freq:
        freq[char] = 0
    freq[char] = freq[char] + 1 


# In[ ]:


"""Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs. """

s1 = "hello"
counts = {}
for letter in s1:
    if letter not in counts:
        counts[letter] = 0
    counts[letter] = counts[letter] + 1
print(counts)    


# In[425]:




str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
words = str1.split()
print(words)

freq_words = {}
for word in words:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] = freq_words[word] + 1
print(freq_words)   

"""Alternative direct method"""

freq_words = dict()
for word in str1.split():
    if word not in freq_words:
        freq_words[word] = 0
        
    freq_words[word] = freq_words[word] + 1


# In[426]:


"""Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word. """

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
words = sent.split()

wrd_d = dict()
for word in words:
    if word not in wrd_d:
        wrd_d[word] = 0
    wrd_d[word] = wrd_d[word] + 1 
print(wrd_d)    


# In[434]:


"""Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most 
frequent letter based on the dictionary. Assign this letter to the variable best_char. """

sally = "sally sells sea shells by the sea shore"
characters = {}
for char in sally:
    if char not in characters:
        characters[char] = 0
    characters[char] = characters[char] + 1  

print(characters)    
print("...................................................")

keys = list(characters.keys())
best_char = keys[0]

for key in keys:
    if characters[key] > characters[best_char]:
        best_char = key
print("The highest occuring character in Sally:", best_char) 
print("......................................................")

worst_char = keys[0]
for key in keys:
    if characters[key] < characters[worst_char]:
        worst_char = key
        
print("The least occuring character in Sally:", best_char)


# In[438]:


"""Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. 
Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case. """

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
#print(string1.lower())

letter_counts = {}
for letter in string1.lower():# The trick was to convert all letters into lower or upper characters
    if letter not in letter_counts:
        letter_counts[letter] = 0
    letter_counts[letter] = letter_counts[letter] + 1 
print(letter_counts)    


# In[439]:


"""Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each 
character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are 
both seen as a “t” for example."""

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."

low_d =dict()
for char in p.upper():# The trick was to convert all letters into lower or upper characters
    if char not in low_d:
        low_d[char] = 0
    low_d[char] =low_d[char] + 1
print(low_d)    


# In[471]:


"""Write a program that asks the user for a sentence in English and then translates that sentence to Pirate."""

eng2pir = {"sir":"matey","hotel":'fleabag inn',"student":'swabbie',"boy":'matey',"madam":'proud beauty',"professor":'foul blaggart',
          "restaurant":'galley',"your":'yer',"excuse":'arr',"students":'swabbies',"are":'be',"lawyer":'foul blaggart',"the":'th',
          "restroom":'head',"my":'me',"hello":'avast',"is":'be',"man":'matey'}

word_eng = input("Enter a sentence in English: ")
# translator = eng2pir.get(word_eng)
# print(translator)
words_list = []
for char in word_eng.split():
    #print(type(char))
    #print(char in eng2pir)
    if char in eng2pir:
        words_list.append(eng2pir[char])
    else:
        words_list.append(char)
#print(words_list)        
print(" ".join(words_list))   


# In[472]:


"""Write a program that finds the most used 7 letter word in scarlet3.txt."""

f = open('scarlet3.txt', 'r')
contents = f.read()
#print(contents.split())
words = {}
for word in contents.split():
    if len(word) == 7:
        #print(word)
        if word not in words:
            words[word] = 0
        words[word] = words[word] + 1
#print(words)        
keys = list(words.keys())
most_7_letter_word = keys[0]
for key in keys:
    if words[key] > words[most_7_letter_word]:
        most_7_letter_word = key
print(most_7_letter_word)        

f.close()


# In[501]:


"""Write a program that allows the user to enter a string. It then prints a table of the letters of the alphabet in 
alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. 
A sample run of the program might look this this:"""

"""Please enter a sentence: ThiS is String with Upper and lower case Letters.
a  2
c  1
d  1
e  5
g  1
h  2
i  4
l  2
n  2
o  1
p  2
r  4
s  5
t  5
u  1
w  2
$
"""

string1 = input("Please, enter a sentence: ")
sentence = string1.lower()#.split() # this ensures that all characters are not duplicated (e.g. T = t)
#print((sentence))
alphabet = 'abcdefghijklmnopqrstuvwxyz'

wordlist = {}
for char in sentence:
    if char in alphabet:# ignores any non letter characters
        if char in wordlist:
            wordlist[char] = wordlist[char] + 1
        else:
            wordlist[char] =  1
# This part of the code does same thing as the if amd else conditional part           
#         if char not in wordlist:
#             wordlist[char] = 0
    
#         wordlist[char] = wordlist[char] + 1

print(wordlist) 

# keys = list(wordlist.items())# returns tuples in a list 

# for key in keys:
#     print(key[0], key[1])

keys = list(wordlist.keys())
for key in sorted(keys):
    print(key, wordlist[key])

        


# In[503]:


"""Write a function named same that takes a string as input, and simply returns that string. """
def same(enter_a_string):
    return enter_a_string

call_func = same('Uko')
print(call_func)


# In[509]:


"""Write a function called same_thing that returns the parameter, unchanged."""
def same_thing(para):
    return para

parameter = 'Uko'#10
func_call = same_thing(parameter)
print(func_call)
print(same_thing('Welcome'))


# In[510]:


"""Write a function called subtract_three that takes an integer or any number as input, and returns that number minus three."""
def subtract_three(para):
    return para - 3

print(subtract_three(3))


# In[511]:


"""Write a function called change that takes one number as its input and returns that number, plus 7"""
def change(num):
    add7 = num + 7
    return add7

call_fun = change(0)
print(call_fun)


# In[513]:


"""Write a function named intro that takes a string as input. Given the string “Becky” as input, the function should return: 
“Hello, my name is Becky and I love SI 106.” """
def intro(string1):
    greeting = "Hello, my name is {} and I love SI 106.".format(string1)
    return greeting

func_invoke = intro('Becky')
print(func_invoke)


# In[516]:


"""Write a function called s_change that takes one string as input and returns that string, concatenated with the string ” for fun.”."""
def s_change(string2):
    concatenate = string2 + ' '+ 'for fun.'
    return concatenate

kall_func = s_change('Coding')
print(kall_func)


# In[519]:


"""Write a function called decision that takes a string as input, and then checks the number of characters. 
If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”. """

def decision(string3):
    """This code would evaluate the length of the formal parameter
    and returns the appropriate statement."""
    if len(string3) > 17:
        return "This is a long string"
    else:
        return "This is a short string"
    
invoke_func = decision("Onyemaechi Uko")
print(invoke_func)
    
    


# In[523]:


"""Write a function named accum_num that takes a list of integers as input, and returns the total value of all those integers
   added together."""
def accum_num(list_int):
    total = 0
    for num in list_int:
        total = total + num
    return total
    
invoke_fun = accum_num([2,3,4,5,6,7,8,9])
print(invoke_fun)


# In[527]:


"""Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list."""

def count(list):
    coun = 0
    for num in list:
        coun += 1
    return coun

count_num = count([2,3,4,5,2,0,1,0,0,2,0,0])
print(count_num)


# In[529]:



numbers = [1, 12, 13, 4]
def foo(bar):
    aug = str(bar) + "street"
    return aug

addresses = []
for item in numbers:
    addresses.append(foo(item))
print(addresses)    


# In[534]:


"""Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. 
mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result. """
def addit(num):
    add5 = num + 5
    return add5

def mult(num):
    mult_add5 = num * addit(num)
    return mult_add5

"""This definds global variables and calls the function 'mult'"""
mult_add5 = 4
result = mult(mult_add5)
print(result)


# In[535]:


def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)


# In[536]:


"""Write a function called int_return that takes an integer as input and returns the same integer."""
def int_return(integer):
    return integer

print(int_return(67))


# In[537]:


"""Write a function called add that takes any number as its input and returns that sum with 2 added."""
def add(number):
    return number + 2

print(add(2))


# In[543]:


"""Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string. """
def change(string):
    concate = string + ' ' + "Nice to meet you!"
    return concate

string_input = change('I am Faith.')
print(string_input)


# In[545]:


"""Write a function, accum, that takes a list of integers as input and returns the sum of those integers."""
def accum(list_int):
    sum_int = 0
    for num in list_int:
        sum_int = sum_int + num
    return sum_int

print(accum([2,3,4,5]))    


# In[547]:


"""Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. 
If the length is less than 5, return “Less than 5”."""
def length(length_list):
    if len(length_list) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"

input_para = 'Onyemaechi'
print(length(input_para))


# In[566]:


"""You will need to write two functions for this problem. The first function, divide that takes in any number and returns 
that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. 
It should return this new number. You should call the divide function within the sum function. Do not worry about decimals. """
def divide(num1):
    num1_div = (num1 / 2)
    return num1_div

def sum(num2):
    num2_sum = divide(num2) + 6
    return num2_sum

d = sum(5)
print(d)


# In[582]:


"""Provided is a list of tuples. Create another list called t_check that contains the third element of every tuple."""
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]
#print(len(lst_tups))
t_check = [lst_tups[0][2], lst_tups[1][2], lst_tups[2][2], lst_tups[3][2], lst_tups[4][2], lst_tups[5][2]]
print(t_check)
print("------Alternative------")
"""Alternative"""
s_check = list()
for item in lst_tups:
    s_check.append(item[2])
print(s_check)    


# In[584]:


"""Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds."""
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

seconds = list()
for item in tups:
    seconds.append(item[1])

print(seconds)    


# In[588]:


"""Define a function called information that takes as input, the variables name, birth_year, fav_color, and hometown. 
It should return a tuple of these variables in this order. """
def information(name,birth_year,year_in_college,hometown):
    """This example of tuple packing"""
    return name,birth_year,year_in_college,hometown

info = information("Uko",1985,2012,'Umuchiakuma')
print(info)


# In[591]:



def add(x, y):
    '''This is an example of unpacking'''
    return x+y

z = (5, 4)
print(add(*z)) # this unpacks the values in z


# In[597]:


""" If you remember, the .items() dictionary method produces a sequence of tuples. Keeping this in mind, we have provided 
you a dictionary called pokemon. For every key value pair, append the key to the list p_names, and append the value to the 
list p_number. Do not use the .keys() or .values() methods. """

pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = list()
p_number = []

for key, value in pokemon.items():
    p_names.append(key)
    p_number.append(value)
print(p_names)
print(p_number)    
    


# In[599]:


"""The .items() method produces a sequence of key-value pair tuples. With this in mind, write code to create a list of keys 
from the dictionary track_medal_counts and assign the list to the variable name track_events. Do NOT use the .keys() method. """

track_medal_counts = {'shot put': 1, 'long jump': 3, '100 meters': 2, '400 meters': 2, '100 meter hurdles': 3, 'triple jump': 3, 'steeplechase': 2, '1500 meters': 1, '5K': 0, '10K': 0, 'marathon': 0, '200 meters': 0, '400 meter hurdles': 0, 'high jump': 1}
track_events = []
for key, value in track_medal_counts.items():
    track_events.append(key)
print(track_events)    


# In[ ]:


"""The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable country. """
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = []
for item in tuples_lst:
    country.append(item[1])
    
print(country)    


# In[ ]:


"""With only one line of code, assign the variables city, country, and year to the values of the tuple olymp. """
olymp = ('Rio', 'Brazil', 2016)
city,country,year = olymp


# In[600]:


"""Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 
Olympics. Create a list, num_medals, that contains only the number of medals for each country. 
You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method. """

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals = []
for key, value in gold.items():
    num_medals.append(value)
    
num_medals    


# In[601]:


"""Write a function named num_test that takes a number as input. If the number is greater than 10, the function should 
return “Greater than 10.” If the number is less than 10, the function should return “Less than 10.” If the number is equal 
to 10, the function should return “Equal to 10.”"""

def num_test(number):
    if number > 10:
        return "Greater than 10."
    elif number < 10:
        return "Less than 10."
    else:
        return "Equal to 10."

num = num_test(20)    
print(num)


# In[604]:


"""Write a function that will return the number of digits in an integer."""

def num_digits(num):
    digits = len(str(num))
    return digits
print(num_digits(20))


# In[656]:


"""Write a function that reverses its string argument."""

def str_reverse(str1): 
    #l = len(str1) # commented to reduce lines of code
    count = len(str1)#l # initialize the count to the length of the string
    new_str = "" # set the new string to empty
    for char in str1: # iterate through the string
        if char == str1[0]: # for the first character, skip it and rather concatenate the last character in the new string 
            new_str = new_str + str1[-1] # concatenate the last character instead of the first
        count = count - 1 # decreament the count
        if count == 0:#now the count would be 0 which will result to -1 and equal to the last character once more, therefore, skip
            break
        new_str = new_str + str1[-1+count] # concatenate the resulting characters
    return new_str # returns the new string   

print(str_reverse("abcdefghijklmnopqrstuvwxyz")) # invoke the function    
print(str_reverse(str_reverse("abcdefghijklmnopqrstuvwxyz")))    
     


# In[658]:


def reverse(lst):
    reversed = []
    for i in range(len(lst)-1, -1, -1): # step through the original list backwards
        reversed.append(lst[i])
    return reversed
print(reverse("uko"))


# In[66]:


"""Define a function called nums that has three parameters. The first parameter, an integer, should be required. 
A second parameter named mult_int should be optional with a default value of 5. The final parameter, switch, should also 
be optional with a default value of False. The function should multiply the two integers together, and if switch is True, 
should change the sign of the product before returning it."""

def nums(a, mult_int=5, switch=False):
    if switch == True:
        return (-a*mult_int)
    else:
        return a*mul_int
    


# In[78]:


"""Write a function called together that takes three parameters, the first is a required parameter that is a number 
(integer or float), the second is a required parameter that is a string, and the third is an optional parameter whose 
default is ” “. What is returned is the first parameter, concatenated with the second, using the third."""

def together(x, astr, z=""):
    z = (str(x)+" "+ astr) + z
    return z
print(together(2,":uko"))


# In[665]:


import random
rand_ = random.randrange(1000)
rand_


# In[669]:


"""Write a while loop that is initialized at 0 and steps at 15. If the counter is an even number,
append the counter to a list called eve_nums"""
eve_nums = []
count = 0
while count <= 15:
    if count%2 == 0:
        eve_nums.append(count)
    count = count + 1
eve_nums    


# In[679]:


"""Write a code to sums all the elements in the list and assign it a variable accum."""
accum = 0
list1 = [8,3,4,5,6,7,9]
# len(list1)
# list1[0]
count = 0
while count <= len(list1)-1: # or count < len(str1)
    accum = accum + list1[count]
    count = count + 1
accum    


# In[682]:


def stop_at_four():
    accum = 0
    list1 = [8,3,4,5,6,7,9]
    # len(list1)
    # list1[0]
    count = 0
    while count <= len(list1)-1: # or count < len(str1)
        accum = accum + list1[count]
        count = count + 1
    return accum

print(stop_at_four())


# In[721]:


#list1 = [8,3,4,5,6,7,9]
def stop_at_four():
    list1 = [8,3,4,5,6,7,9]
    count = 0
    new_list = []
    while True:#count < len(list1):
        new_list.append(list1[count])
        count = count + 1
        if list1[count] == 4:
            new_list.append(list1[count])
            return new_list
print(stop_at_four())


# In[736]:


"""Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a 
sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 
(it should not contain the number 5). """

def sublist(lst):
    """This function takes a list of numbers and returns the list."""
    print(type(lst))
    #return lst # this would cause the function to return value but would not continue 


    x = 0
    new_list = []
    while x < len(lst):
        #new_list.append(lst[x]) # here woul include the number 5
        if lst[x] == 5:
            return new_list
        new_list.append(lst[x])
        x = x + 1
    return new_list    
#         if lst[x] != 5:
#             new_list.append(lst[x])
#         else:
#             return new_list
#     return new_list    
lst_num = sublist([1,2,3,4,6,5,7,8,9]) # Always remember the parenthesis when calling a function
print(lst_num)


# In[ ]:


"""Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”)."""
def sublist(lst):
    """This function takes a list of strings and returns the list."""
    #print(type(lst))
    #return lst


    x = 0
    new_list = []
    while x < len(lst):
        #new_list.append(lst[x])
        if lst[x] == "STOP":
            return new_list
        new_list.append(lst[x])
        x = x + 1
    return new_list


# In[758]:


"""Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new 
list until the string that appears is “z”. The function should return the new list."""
def stop_at_z():
    """This function takes a list of strings and returns the list."""
    #print(type(lst))
    #return lst
    list_str = input("Enter a string: ")# prompts user to enter a list of strings
    #str_list = list(list_str) # if used, change anywhere that contains 'list_str' to 'str_list' 

    x = 0
    new_list = []
    while x < len(list_str):# or len(str_list):or #True:
        new_list.append(list_str[x])
        if list_str[x] == "z":
            return new_list
        #new_list.append(lst[x])
        x = x + 1
    return new_list

call_func = stop_at_z()
print(call_func)


# In[734]:


"""Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a 
while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. 
Once complete, sum2 should equal sum1."""
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
    
sum2 = 0
count = 0
while count < len(lst):
    sum2 = sum2 + lst[count]
    count = count + 1
    
print(sum1 == sum2)    


# In[751]:


"""Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once 
the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless 
of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, 
the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing """

def beginning(lst):
    #print(len(lst))
    
    x = 0
    new_list = list()
    while x < len(lst):
        
        if lst[x] == "bye":
            return new_list
        
        if len(new_list) == 10:
            return new_list
        
        new_list.append(lst[x])
        x = x + 1
    return new_list
    
call_fun = beginning(['uko', 'look', 'carefully','at','your','code.','to','avoid','infinite','loop','bye!','see','you','next','time.']) 
print(call_fun)


# In[763]:


"""Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a 
new list until the string that appears is “z”. The function should return the new list. """

def stop_at_z(list_str):
    x = 0
    new_list = []
    while x < len(list_str):#True:
        #new_list.append(list_str[x])
        if list_str[x] == "z":
            return new_list
        new_list.append(list_str[x])
        x = x + 1
    return new_list

call_func = stop_at_z("ueirzui")
print(call_func)


# In[764]:


"""Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a 
new list until the number 4 appears. The function should return the new list."""

def stop_at_four(list1):
    pass
    
    x = 0
    new = []
    while x < len(list1):
        
        if list1[x] == 4:
            break
        new.append(list1[x])    
        x += 1
    return new
    
    
    
z = [0,9,3,4,5,6]   
print(stop_at_four(z))


# In[768]:


initial = 7
def f(x, y=3, z=initial):
    print("x","y","z","are",x,y,z)
    
f(2)  
f(2, 4)
f(2,3,5)


# In[769]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(2))
print(f(4))
print(f(6))
print(f(7,["Hello"]))
print(f(9,["Hello"]))


# In[ ]:


""" Write a function called str_mult that takes in a required string parameter and an optional integer parameter. The default 
value for the integer parameter should be 3. The function should return the string multiplied by the integer parameter. """
def str_mult(a, s=3):
    return a*s

print(str_mult("uko"))    


# In[770]:


# Keyword parameters
initial = 7
def f(x, y=3, z=initial):
    print("x","y","z","are",x,y,z)
    
f(2)  
f(2, z=4)# use of keyword would mean that only specified values are assigned while other values not mentioned take on their default values
f(2,3,5)


# In[771]:


# When a final formal parameter of the form **name is present, it receives a dictionary (see Mapping Types — dict) containing 
# all keyword arguments except for those corresponding to a formal parameter. This may be combined with a formal parameter of 
# the form *name (described in the next subsection) which receives a tuple containing the positional arguments beyond 
# the formal parameter list. (*name must occur before **name.) For example, if we define a function like this:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# It could be called like this:        
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")        


# In[ ]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
        print("-- This parrot wouldn't" + action,)
    
        print("if you put" + str(voltage) + "volts through it.")
    
        print("-- Lovely plumage, the" +  type)
    
        print("-- It's " + state + "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# In[ ]:


names_scores = [("Jack",[67,89,91]),("Emily",[72,95,42]),("Taylor",[83,92,86])]
for name, scores in names_scores:
    print("The scores {nm} got were: {s1},{s2},{s3}.".format(nm=name,s1=scores[0],s2=scores[1],s3=scores[2]))


# In[772]:


# this works
names = ["Jack","Jill","Mary"]
#for n in names:
#    print("'{}!' she yelled. '{}! {}, {}!'".format(n,n,n,"say hello"))

# but this also works!
names = ["Jack","Jill","Mary"]
for n in names:
    print("'{0}!' she yelled. '{0}! {0}, {1}!'".format(n,"say hello")) # n is position 0 and "say hello" is position 1


# In[ ]:


names = ["Alexey", "Catalina", "Mitsuki", "Pablo"]
print("'{first}!' she yelled. 'Come here, {first}! {f_one}, {f_two}, and {f_three} are here!'".format(first = names[1], f_one = names[0], f_two = names[2], f_three = names[3]))


# In[773]:


"""Define a function called multiply. It should have one required parameter, a string. It should also have one optional 
parameter, an integer, named mult_int, with a default value of 10. The function should return the string multiplied by 
the integer. (i.e.: Given inputs “Hello”, mult_int=3, the function should return “HelloHelloHello”) """
def multiply(a, mult_int= int(10.0)):
    return a * mult_int

print(multiply("All you need to get!"))
print(multiply("Hello"))


# In[ ]:


"""Currently the function is supposed to take 1 required parameter, and 2 optional parameters, however the code doesn’t work. 
Fix the code so that it passes the test. This should only require changing one line of code."""

def waste(var = "Water", mar, marble = "type"):# make it run?
    final_string = var + " " + marble + " " + mar
    return final_string


# In[ ]:


"""Create a function called mult that has two parameters, the first is required and should be an integer, the second is an 
optional parameter that can either be a number or a string but whose default is 6. The function should return the first 
parameter multiplied by the second."""
def mult(a, b=6):
    return a*b


# In[ ]:


"""Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, 
and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, 
the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. 
If the boolean parameter is False, return the boolean value “False”. """

def test(a, b=True, dict1={2:3, 4:5, 6:8}):
    if b == True:
        if a in dict1:
            return dict1[a]
    
    return False
        
print(test(3))  


# In[775]:


"""Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a 
string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter 
called d that has a default value of 
{'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function 
checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; 
if it is, return True, otherwise return False.

But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. 
If it’s not, the function should return True in this case, and if it is, it should return False."""

def checkingIfIn(astring, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
            if direction == True:
                
                if astring in d:
                    return True
                else:
                    return False
                    
            elif direction == False:
                
                if astring not in d:
                    return True
                else:
                    False
                    
            return False        
            
print(checkingIfIn("fruit"))


# In[ ]:


"""We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input 
parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code 
window for specific variable assignmemts. """

def checkingIfIn(astring, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
            if direction == True:
                
                if astring in d:
                    return d[astring]
                else:
                    return False
                    
            else:
                
                if astring not in d:
                    return True
                else:
                    return d[astring]
                    
                   

                
# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn("uko")
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn("uko", False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn("fruit")
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn("fruit",d={"fruit":8})


# In[780]:


"""using the function lambda, takes the place of defining any function. That means, if you would like to reuse the particular lambda in another code, then you must assign it to a variable to help you make reference to it later.
Lambda makes it easier, shorter and I believe faster than defining a function consisting of couple of lines traditionally. 
By illustration: 
def add(a, b):
return a+b

equivalent of using the lambda function:

lambda a,b: a+b


If you would want to reuse the defined function "add", then you must call it by name "add(a,b)". Sometimes, you also assign the function to a variable when calling, e.g. call_func = add(a=2, b=5).


Now, if you would like to reuse your lambda subsequently, then assign your lambda to a variable and use it over and again. e.g.
kool = lambda a,b: a+b

sool = kool(8,9)
print(sool)

I hope that was helpful. Cheers!"""

kool = lambda a,b: a+b

sool = kool(8,9)
print(sool)


# In[ ]:


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(astr):
    ast_list = list()
    for ast in astr:
        ast_list.append(ast)
    
    ast_str = ""
    for item in ast_list:
        if item not in punctuation_chars:
            ast_str = ast_str + item
    return ast_str 


# In[53]:


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of negative words to use
negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# Function to strip punctuations
def strip_punctuation(astr):
    
    for char in punctuation_chars:
        char_strip = astr.replace(char, '')
        astr = char_strip
    return  char_strip 


def get_neg(astr):
    num_neg_words = 0
#     astr_split = astr.split()
#     astr = astr_split
    for word in astr:
        words_neg_strip = strip_punctuation(word)
        if words_neg_strip in negative_words:
            num_neg_words = num_neg_words + 1
    return num_neg_words
     


# In[69]:


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# Function to strip punctuations
def strip_punctuation(astr):
    
    for char in punctuation_chars:
        char_strip = astr.replace(char, '')
        astr = char_strip
    return  char_strip 


# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
#print(positive_words[50:200])  


def get_pos(astr):
    num_pos_words = 0
#     astr_split = astr.split()
#     astr = astr_split
    for word in astr:
        words_pos_strip = strip_punctuation(word.strip())# not really needed strip()
        if words_pos_strip in positive_words:
            num_pos_words = num_pos_words + 1
        else:
            continue
    return num_pos_words

print(get_pos([":;go'o'#d","#@lu#cky","nice","##u#s#eless",'#en#!jo@,y']))


# In[54]:


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(astr):
    
    for char in punctuation_chars:
        char_strip = astr.replace(char, '')
        astr = char_strip
    return  char_strip.strip()  

print(strip_punctuation(":;go'o'#d"))


# In[65]:


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(astr):
    
    for char in punctuation_chars:
        char_strip = astr.replace(char, '')
        astr = char_strip
    return  char_strip#.strip() 

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
                               

def get_pos(astr):
    num_pos_words = 0
    astr_split = astr.split()
    astr = astr_split
    for word in astr:
        words_pos_strip = strip_punctuation(word.strip())
        if words_pos_strip in positive_words:
            num_pos_words = num_pos_words + 1
        else:
            continue
    return num_pos_words

# list of negative words to use

negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
                      
    
def get_neg(astr):
    num_neg_words = 0
    astr_split = astr.split()
    astr = astr_split
    for word in astr:
        words_pos_strip = strip_punctuation(word.strip())
        if words_pos_strip in negative_words:
            num_neg_words = num_neg_words + 1
        else:
            continue
    return num_neg_words


with open('project_twitter_data.csv') as pro_tweet_f:
    #print(pro_f.readlines())
    #header = pro_f.readlines()[0]
    #print(header)
    with open("resulting_data.csv","w") as output_tweet_f:
         #header = pro_tweet_f.readlines()[0]
        #output_tweet_f.write(pro_tweet_f.readline()[0][1:])
        output_tweet_f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
        output_tweet_f.write("\n")
        for tweet in pro_tweet_f.readlines()[1:]:
            tweets = tweet.strip().split(",")
            num_retweets = tweets[1]
            num_replies = tweets[2]
            pos_tweets = get_pos(strip_punctuation(tweets[0]))
            neg_tweets = get_neg(strip_punctuation(tweets[0])) 
            net_tweets = pos_tweets - neg_tweets
            row_str_tweets = "{}, {}, {}, {}, {}".format(num_retweets, num_replies, pos_tweets, neg_tweets, net_tweets)
            output_tweet_f.write(row_str_tweets)
            output_tweet_f.write("\n")
            #print(net_tweets)
            print("{} {} {}".format(pos_tweets, neg_tweets, net_tweets))

   


# In[64]:


with open('project_twitter_data.csv') as pro_tweet_f:
    #print(pro_f.readlines())
    #header = pro_f.readlines()[0]
    #print(header)
    with open("resulting_data.csv","w") as output_tweet_f:
         #header = pro_tweet_f.readlines()[0]
        #output_tweet_f.write(pro_tweet_f.readline()[0][1:])
        output_tweet_f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
        output_tweet_f.write("\n")
        for tweet in pro_tweet_f.readlines()[1:]:
            tweets = tweet.strip().split(",")
            num_retweets = tweets[1]
            num_replies = tweets[2]
            pos_tweets = get_pos(strip_punctuation(tweets[0]))
            neg_tweets = get_neg(strip_punctuation(tweets[0])) 
            net_tweets = pos_tweets - neg_tweets
            row_str_tweets = "{}, {}, {}, {}, {}".format(num_retweets, num_replies, pos_tweets, neg_tweets, net_tweets)
            output_tweet_f.write(row_str_tweets)
            output_tweet_f.write("\n")
            #print(net_tweets)
            print("{} {} {}".format(pos_tweets, neg_tweets, net_tweets))

   


# In[79]:


"""Write code that uses iteration to print out the length of each element of the list stored in str_list. """
str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
for word in str_list:
    print(len(word))


# In[81]:


"""What happens if you put the initialization of accum inside the for loop as the first instruction in the loop?"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for w in nums:
   accum = 0
   accum = accum + w
print(accum)
"""It will print out 10 instead of 55"""


# In[83]:


"""You can even have a list of functions (!)."""
def square(x):
    return x*x

L = [square, abs, lambda x: x+1]

print("****names****")
for f in L:
    print(f)

print("****call each of them****")
for f in L:
    print(f(-2))

print("****just the first one in the list****")
print(L[0])
print(L[0](3))


# In[84]:


nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]

#write code to print the value associated with key 'c' in the second dictionary (90)
print(nested2[1]["c"])
#write code to print the value associated with key 'b' in the third dictionary
print(nested2[2]["b"])
#add a fourth dictionary add the end of the list; print something to check your work.
nested2.append({"g":33,"w":"no"})
print(nested2)
#change the value associated with 'c' in the third dictionary from "yes" to "no"; print something to check your work
nested2[2]["c"]="no"
print(nested2)


# In[86]:


"""Use indexing to assign the element ‘horse’ to the variable name idx1."""
animals = [['cat', 'dog', 'mouse'], ['horse', 'cow', 'goat'], ['cheetah', 'giraffe', 'rhino']]

idx1=animals[1][0]
idx1


# In[87]:


"""Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant."""
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]

plant=data[7][0][0]
print(plant)


# In[91]:


d = {'key1': {'a': 5, 'c': 90, 5: 50}, 'key2':{'b': 3, 'c': "yes"}}
print(d)

"""5 is a valid key; {1:2, 3:4} is a dictionary with two keys, and is a valid value to associate with key 5."""
d[5] = {1: 2, 3: 4}
print(d)

"""d['key2'] is {'b': 3, 'c': "yes"}, a python object. It can be bound to the key 'd' in a dictionary {'a': 5, 'c': 90, 5: 50}"""
d['key1']['d'] = d['key2']
print(d)


# In[95]:


""" Extract the value associated with the key color and assign it to the variable color. Do not hard code this."""

info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }


color = info["personal_data"]["physical_features"]["color"]
print(color)
print("***After assigning new value to color***")
print("-"*40)
"""Assign a new value to dictionary color"""
info["personal_data"]["physical_features"]["color"] = 200
print(info)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




