#1: Write a personalGreeting function which, after asking for the user’s name, 
#outputs a personalised greeting. E.g., for user input Sam, the function should 
#output the greeting Hello Sam, nice to see you! Note the details of the spaces 
#and punctuation.
def personalGreeting():
    user_name = input('Enter name: ')
    print(f'Hello {user_name}.')

#2: Write a formalName function which asks the user to input their given name 
#and family name, and then outputs a more formal version of their name. E.g., 
#on input Sam and Brown, the function should output S. Brown. Again, note 
#the spacing and punctuation. 
def formalName():
    user_name = input('Enter name: ')
    split_name = user_name.split()
    last_name = split_name[1]
    print(f'{user_name[0]}. {last_name}.')

#3: Copy the kilos2Ounces conversion function from your pract1.py file into 
#your pract4.py file. Modify this function so that its output takes the form of a 
#message such as s “12.34 kilos is equal to 435.28 ounces” where both the user’s 
#kilos value and the calculated ounces values are displayed to two decimal places.
def kilos2Ounces():
    kilos = float(input('Enter weight in kilos: '))
    ounces = kilos * 35.274
    print(f'{kilos}kg in ounces is {ounces}Oz')

#4: Suppose the university decides that students’ email addresses should be made 
#up of the first 4 letters of their surname, the first letter of their forename, 
#and the final two digits of the year they entered the university, separated by dots.
#Write a function called generateEmail that outputs an email address given 
#a student’s details.
def generateEmail():
    forename = input('Enter first name: ')
    surname = input('Enter last name: ')
    year_joined = input('Enter year joined: ')
    email_address = f'{surname[0:4]}.{forename[0]}.{year_joined[2:]}'
    print(email_address)

#5: A teacher awards letter grades for test marks as follows: 8, 9 or 10 marks 
#give an A, 6 or 7 marks give B, 4 or 5 marks give C, and 0, 1, 2 or 3 marks 
#all give F. Using string indexing, write a function gradeTest which asks the 
#user for a mark (between 0 and 10) and displays the corresponding grade. 
def gradeTest():
    mark = int(input('Enter mark: '))
    if mark >= 8:
        print('A')
    elif mark >= 6:
        print('B')
    elif mark >= 4:
        print('C')
    elif mark >= 0:
        print('F')

#6: Write a function graphicLetters which first asks the user to enter a word, 
#opens a graphics window, and then allows the user to display the letters of 
#the word at different locations by clicking the mouse once for each letter. 
#(Use the setSize method of the Text class to make the letters appear big.) 
from graphics import *
def graphicLetters():
    win = GraphWin()
    word = input('Enter word: ')
    for i in word:
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        message = Text(Point(x,y),i)
        message.draw(win)

#7: Write a singASong function which outputs a “song” based on a single word. 
#The user should be asked for the song’s word, how many lines long the song 
#should be, and how many times the word should be repeated on each line. 
def singASong():
    song_name = input('Enter word: ')
    line_amount = int(input('How many lines: '))
    word_repetition = int(input('How many repetitions: '))
    for _ in range(line_amount):
        linefin = (song_name + ' ') * word_repetition
        print(linefin)

#8: Write a function exchangeTable that gives a table of euros values and their 
#equivalent values in pounds, using an exchange rate of 1.17 euros to the pound. 
#The euro values should be 0, 1, 2, …, 20, and should be right justified. 
#The pound values should be right justified and given to two decimal 
#places (i.e. with decimal points lined up and with 
#pence values after the points). 
def exchangeTable():
    print('euros\t|\tpounds')
    print('----------------------')
    for i in range(0,20):
        pounds = float(i / 1.17)
        print(f'{i}\t|\t{pounds:.2f}')

#9: Write a makeInitialism function that allows the user to enter a phrase, 
#and then displays the first letters of the words in capitals for that phrase. 
#For example, if the user enters “University of Portsmouth”, the function 
#should display UOP. (Hint: first use the split method to 
#find the words in the inputted string.)
def makeInitialism():
    phrase = input('Enter phrase: ')
    phrase_split = phrase.split()
    abbrev_phrase = str()
    for i in range(len(phrase_split)):
        abbrev_phrase += f'{phrase_split[i][0].upper()}'
    print(abbrev_phrase)

#10: Harder: Write a nameToNumber function that asks the user for their name 
#and converts it into a numerical value by adding up the “values” of its 
#letters (where ‘a’ is 1, ‘b’ is 2, …, ‘z’ is 26). So, for example, “Sam” 
#has the value 19 + 1 + 13 = 33. 
def nameToNumber():
    name = input('Enter name: ')
    number = 0
    for i in range(len(name)):
        todigit = name[i]
        number += (ord(todigit)) - 96
    print(number)

#11: Write a fileInCaps function which prints the contents of a file in 
#capital letters. The name of the input file should be typed in 
#by the user. Try your function with our quotation.txt file.
import os
def fileInCaps():
    os.chdir('Python/worksheets')
    file_name = f"{input('Enter filename: ')}.txt"
    in_file = open(file_name,'r')
    contents = in_file.read()
    print(contents.upper())
    in_file.close()

#12: Jenny uses a text file to write down how much she spends on food every 
#day of the week. Open the spending.txt file that she wrote last week and 
#save it. See the content of this file. Observe, for example, that Jenny spent 
#£29.10 on Wednesday. Then write a function called totalSpending that reads 
#the spending.txt file and prints the total sum of money spent that week.
def totalSpending():
    os.chdir('Python/worksheets')
    in_file = open('spending.txt','r')
    total = 0
    for _ in in_file:
        line = in_file.readline().replace('\n','')
        try:
            total += float(line)
        except ValueError:
            continue
    print(f'£{total:.2f}')

#13: Harder: The file rainfall.txt contains rainfall data in millimetres (mm) for 
#several UK cities for a particular day. Open it to see the format of this file 
#and download it. Write a function rainfallChart that displays this data as a 
#textual bar chart using one asterisk for each mm of rainfall.
def rainfallChart():
    os.chdir('Python/worksheets')
    in_file = open('rainfall.txt','r')
    for i in in_file:
        linesplit = i.split()
        amount_of_rain = int(linesplit[1])
        asterisk_amount = str('*' * amount_of_rain)
        print(linesplit[0],'\n',asterisk_amount)

#14: Harder: Write a rainfallInInches function that reads the rainfall.txt file, 
#and outputs the data to a file rainfallInches.txt where all the mm values 
#are converted to inches (there are 25.4 mm in an inch). The inch values should 
#be given to two decimal places.
def rainfallInInches():
    os.chdir('Python/worksheets')
    in_file = open('rainfall.txt','r')
    new_file = open('rainfallInches.txt','w')
    for i in in_file:
        linesplit = i.split()
        place = str(linesplit[0])
        rain_num = int(linesplit[1])
        rain_inches = float(rain_num/25.4)
        newline = place + f' {rain_inches:.2f}'
        print(newline)
        newline += '\n'
        new_file.write(newline)
    in_file.close()
    new_file.close()
    
#15: Harder: In Linux, there is a command called wc which reports the number of 
#characters, words, and lines in a file. Write a function wc which performs the 
#same task. The name of the file should be entered by the user.
def wc():
    os.chdir('Python\worksheets')
    file_name = f'{input("Enter file name: ")}.txt'
    in_file = open(file_name, 'r')
    char_amount = 0
    word_amount = 0
    for i, line in enumerate(in_file):
        char_amount += len(line)
        word_amount += len(line.split())
    print(char_amount, word_amount, i)