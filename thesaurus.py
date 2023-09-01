#stores all thesaurus programme abilities
import os
import sys
import re
import random
import time
class Thesaurus():
    def __init__(self,linked):
        # self.linked=linked
        # self.word=word
        self.choice='1'
        self.linked=linked
        self.myDict={}
        self.keywordcheck=[]
    def add_keywords(self): #keyword entry
        print('We will be starting a new Thesaurus')
        print('You may now enter a series of keywords and their synonyms.')
        print('Press 0 to return to the Main Menu')
        while True:
            self.keyword=input('Enter keyword: ').lower()
            if self.keyword.isalpha()==True and self.keyword not in self.keywordcheck:
                
                print(f'''You may enter one or more synonyms for "{self.keyword}"\n(please press "Enter" once done).''')
                if self.synonym()==False: return #to main menu
            elif self.keyword.lower() in self.keywordcheck:
                print('Keyword already specified once')
            elif self.keyword=='0':
                return 
            else:
                print('invalid keyword')
    def synonym(self): #synonym entry
        synonym_list=[]
        while True:
            newsynonym=input(f'Enter synonym for "{self.keyword}": ').lower()
            if newsynonym.isalpha()==True and newsynonym not in synonym_list and newsynonym !=self.keyword: 
                synonym_list.append(newsynonym)
            elif newsynonym=='':
                if len(synonym_list)==0:
                    print('Add at least one synonym first')
                else:
                    self.linked.inserting(self.keyword,synonym_list)
                    if self.addmore()==True: #prevent stacking
                        return True
                    else: return False
            else:
                print('Invalid Synonym')
    def addmore(self): #addmore synonyms, putting them in 1 func very messy and causes more problems
        while True:
            yn=input('Do you want to add more keywords? y/n: ').lower()
            self.keywordcheck.append(self.keyword)
            if yn=='y': 
                return True
            elif yn=='n':
                print(f'Your new Thesaurus is printed here...')
                print(self.linked.printThesaurus())
                os.system('pause')
                return False
            else:
                print('Please type only y or n') 
    def process(self): # have not added back periods or full stops into program
        while True:
            processfile=input('Please enter input file or press 0 to return: ')

            if processfile=='0':    
                print('Returning...') 
                return
            if os.path.exists(f'{processfile}')==False:
                print('File specified does not exist, please input another file')
            else:
                with open(processfile,'r') as f:
                    words=f.read()
                    print('The text before processing:')
                    print(f'{words}')
                    os.system('pause')
                    if self.linked.head==None:
                        print('You do not have a thesaurus yet inputted, please make one or open one first')
                        return
                    print('Next choose a Text Processing option.\n\t')
                    choice=input('Please select your choice: (1,2,3)\n\t1. Simplified Writing\n\t2. Elegant Writing\n\t3. Back to Main Menu\nEnter choice: ')
                    while True:
                        if choice =='3':
                            return
                        elif choice=='1':
                            print('\nProcessing Text for: Simplified Writing\n')
                            head=self.linked.head
                            wordlist=re.split("(\W)|_",words)#(\W) method to split string and matches 
                            # any Non-alphanumeric character. Non-alphanumeric means no letter, digit, and underscore
                            for i in range(len(wordlist)): # for '_' it gets None so we have to change it
                                if wordlist[i] ==None:
                                    wordlist[i]="_"
                            for i in wordlist:
                                if i=='':
                                    wordlist.remove(i) #remove '' produced from  resplit
                            while head!=None:
                                for i in range(len(wordlist)):
                                    capitalize=False
                                    if wordlist[i][0].isalpha(): #checks if first letter of each word is capitalised
                                        if wordlist[i][0].isupper():
                                            capitalize=True
                                    if wordlist[i].lower() in head.synonyms:
                                        if capitalize:
                                            wordlist[i]=head.keyword.capitalize()
                                        else:
                                            wordlist[i]=head.keyword
                                head=head.next

                            print("The text after processing:")
                            stringText=''
                            for i in wordlist:
                                stringText+=i+''
                            print(stringText)
                            os.system('pause')
                            self.savefile(stringText)
                            return
                        
                        elif choice=='2':
                            print('\nProcessing Text for: Elegant Writing\n')
                            head=self.linked.head
                            wordlist=re.split('(\W)|_',words) #(\W) method to split string and matches 
                            # any Non-alphanumeric character. Non-alphanumeric means no letter, digit, and underscore
                            for i in range(len(wordlist)): # for '_' it gets None so we have to change it
                                if wordlist[i] ==None:
                                    wordlist[i]="_"
                            for i in wordlist:
                                if i=='':
                                    wordlist.remove(i) #remove '' produced from  resplit

                            while head!=None:
                                for i in range(len(wordlist)):
                                    capitalize=False
                                    if wordlist[i][0].isalpha(): #checks if first letter of each word is capitalised
                                        if wordlist[i][0].isupper():
                                            capitalize=True
                                    if wordlist[i].lower() == head.keyword:
                                        if capitalize:
                                            wordlist[i]=random.choice(head.synonyms).capitalize()
                                        else: wordlist[i]=random.choice(head.synonyms)
                                head=head.next

                            print("The text after processing:")
                            stringText=''
                            for text in wordlist:
                                stringText+=text+''
                            print(stringText)
                            os.system('pause')
                            self.savefile(stringText)
                            return
                        else: 
                            print('please only input 1,2 or 3')
    def savefile(self,stringText):
        while True:
            save=input('Do you want to save the text into a file? y/n: ')
            if save=='y': 
                filename=input('Please enter new filename ')
                isExist= os.path.exists(f'{filename}')
                if isExist==True:
                    print('Filepath already exists, please input another name')
                elif isExist==False:
                    with open(filename,'w') as f:
                        f.write(f'{stringText}')
                        print(f'Your file "{filename}" has been saved')
                        os.system('pause')
                    return
            elif save=='n': break
            else: print('Input only y or n')
    def save(self,filename):
        # current=self.linked.head
        f=open(filename,'w')
            # synonym_string=', '.join(current.synonyms)
        f.write(self.linked.printThesaurus(self.choice))
        print(f'Your file "{filename}" has been saved')
        os.system('pause')
        return
    def sort(self):
        choices=['1','2','3','4']
        self.choice=input('''Please select your choice: (1,2,3,4,5)\n\t
        1. Alphabetically (Default)\n\t
        2. Length/Alphabetically\n\t
        3. Length/Random Alphabetically\n\t
        4. Randomly\n\t
        5. Back to Main Menu\nEnter choice: ''')
        while True:
            if self.choice in choices:
                if self.choice=='1':
                    print('Sorting Synonyms Alphabetically (Default)')
                elif self.choice=='2':
                    print('Sorting Synonyms Length/Alphabetically')
                elif self.choice=='3':
                    print('Sorting Synonyms Length/Random Alphabetically')
                elif self.choice=='4':
                    print('Sorting Synonyms Randomly')
                print(self.linked.printThesaurus(self.choice))
            elif self.choice=='5':
                print('Returning... ')
                return
            else:
                print('Invalid input, please only input 1 to 5')

            os.system('pause')
            return
    def edit(self):
        while True:
            editinput=input('Do you want to\n\t1.Delete Keyword\n\t2.Add Synonym\n\t3.Delete Synonym\n\t4.Return to Main Menu:')
            if editinput=='4':return
            elif editinput=='1':
                self.deleteKey()
                return
            elif editinput=='2':
                self.addSyn()
                return
            elif editinput=='3':
                self.delSyn()
                return
            else:
                print('Incorrect input')
    def deleteKey(self):
        while True:
            print(self.linked.printThesaurus())
            keyword_del=input('Input keyword you want to delete: ')
            if self.linked.deleteNode(keyword_del)==True:
                print('Successfully Deleted!')
                # print('Your thesaurus now:')
                # print(self.linked.printThesaurus())
                os.system('pause')
                return
            else:
                print('Error finding keyword, please input valid keyword')
    def addSyn(self):
        while True:
            print(self.linked.printThesaurus())
            synadd=input("Insert keyword you want to add more synonyms for: ")
            synonyms=self.linked.get(synadd)
            if synonyms==0:
                print('Invalid keyword, please type a valid keyword')
            else:
                while True:
                    print(synonyms)
                    newsyn=input('Please input a new synonym:')
                    if newsyn in synonyms:
                        print('Synonym already exists')
                    else:
                        synonyms.append(newsyn.lower())
                        self.linked.deleteNode(synadd)
                        self.linked.inserting(synadd,synonyms)
                        print('Synonym Added')
                        print(self.linked.printThesaurus())
                        break
                return
    def delSyn(self):
        while True:
            print(self.linked.printThesaurus())
            keyworddel=input("Insert keyword you want to remove synonyms for: ")
            synonyms=self.linked.get(keyworddel)
            if synonyms==0:
                print('Invalid keyword, please type a valid keyword')
            else:
                while True:
                    print(synonyms)
                    delsyn=input('Please input a synonym to delete:')
                    if delsyn not in synonyms:
                        print('Synonym does not exist')
                    else:
                        synonyms.remove(delsyn.lower())
                        self.linked.deleteNode(keyworddel)
                        self.linked.inserting(keyworddel,synonyms)
                        print('Synonym Removed') #add if no more synonyms left
                        print(self.linked.printThesaurus())
                        break
                return
    def quiz(self,questions):
        question=0#question counter
        correct=0
        correctwords=[]
        time.sleep(3)
        keywords,keyword_list=self.linked.getkey()
        while question!=int(questions): # if quiz surpass keyword amount in thesaurus prompt exit
            if len(keyword_list)==0:
                print('All keywords have been used, stopping quiz...')
                break
            random_key=random.choice(keyword_list)
            # keyword_list.remove(random_key)
            word_qn=input(f"What word is related to '{random_key}': ").lower()
            question+=1
            if word_qn in correctwords:
                print('You cannot write down the same synonym twice')
            elif word_qn in keywords[random_key] and word_qn not in correctwords: #research,model,model improvement
                print('Correct!')
                correctwords.append(word_qn)
                correct+=1
                if all(item in correctwords for item in keywords[random_key]): # if all synonyms have been used in a keyword, remove keyword
                    print('brwesd')
                    keyword_list.remove(random_key)
            else:
                print('Incorrect')
        print(f'You got {correct} out of {question} questions correct!')
        os.system('pause')
        # print(check)

        
                                
                                
