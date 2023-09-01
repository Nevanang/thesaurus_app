
import os
import sys
import re
from thesaurus import Thesaurus
from linkedlist import SortedList
# Python program to use
# main for function call.




#self is a way to refer data of a particular object within class definition, self is the stand-in for future object, 
# it is to access attr and call other methods when no objects are created yet
class DisplayMenu:
    # Beginning of Thesaurus Prompt 
    def __init__(self,thesaurus): # every method should have a self arg
        """Doing .help shows this"""
        self.filename=''
        self.savefile=''
        self.choice='1'
        self.thesaurus=thesaurus #self.thesaurus= Thesaurus() so i can call thesaurus class funcs
        self.dictChoice={ #using it into another function hence need self
            '1':self.new, # functions made in class
            '2':self.open,
            '3':self.sort,
            '4':self.processText,
            '5':self.edit,
            '6':self.quiz,
            '7':self.print,
            '8':self.save,
            '9':self.saveAs,
            '10':self.exit
        }
        self.path=os.getcwd()
        #if userinput>10: print('invalid')
    def menu(self):
        while(True):
            choice=input("""Please select your choice: (1,2,3,4,5,6,7,8,9,10)
        \t1. New
        \t2. Open
        \t3. Sort
        \t4. Process Text
        \t5. Edit Thesaurus
        \t6. Thesaurus Quiz
        \t7. Print
        \t8. Save
        \t9. Save As
        \t10. Exit
        Enter choice: """
        )
            selectedChoice=self.dictChoice.get(choice) 
            #becomes function as get 1 from dict is self.new, if it is outside range, will return nothing

            if selectedChoice: # will not go here if it returns with noneType so if invalid will go to elif loop
                print('')
                selectedChoice() # continues with functions, if invalid will go into
            elif choice.isalpha():
                print(f'"{choice}" is not a number, please input a number')
            elif choice.isnumeric():
                print('Please only input 1 to 10')
    def new(self): # keywords remain in alphabetical order
        thesaurus.add_keywords()
        pass
    def open(self): # must check for existing filename, empty filename and that it is a new thesaurus, open replaces old thesaurus
        self.thesaurus.linked.deleteAll() #delete previous linked list
        print('We will be opening an existing Thesaurus.')
        while(True):
            openThesaurus=input('Please enter input file or press 0 to return to Main Menu: ')
            if openThesaurus=='0':
                return
            # elif isExist==True:
            #     print('File path has been specified already, please try another name')
            else:
                try: 
                    with open(openThesaurus,"r") as f:
                        self.filename=openThesaurus # for saving file
                        newdict=f.read()
                        keyword=re.split(":|\n",newdict)#split based off , and \n delimiters
                        for i in keyword:
                            self.thesaurus.keywordcheck.append(i) # to ensure no duplicates when making a new keyword
                        self.thesaurus.linked.open(keyword)
                        print(self.thesaurus.linked.printThesaurus())
                        os.system('pause')
                        return 
                except (IndexError,AttributeError):
                    print('File format not supported')
                except FileNotFoundError: # inputting /
                    print('no file found')
                except (OSError,PermissionError):
                    print('Please input the file name properly')
    def sort(self): #sorting makes dictionary sort
        if self.thesaurus.linked.lengthOfList()==0:
            self.thesauruschecker(2)#2
            return
        else:
            self.thesaurus.sort()
        return
    def processText(self):# fiel must exist and save text to file
        thesaurus.process()
        return
    def edit(self):
        if self.thesaurus.linked.lengthOfList()==0:
            self.thesauruschecker(2)#2
            return
        else:
            self.thesaurus.edit()
            return
    def quiz(self):
        if self.thesaurus.linked.lengthOfList()==0:
            self.thesauruschecker(2)#2
            return
        while True:
            questions=input('Input how many questions you would like: ')
            if questions.isnumeric() and int(questions)>0:
                print('A random keyword will be shown, please input a related word that exists in the thesaurus')
                self.thesaurus.quiz(questions)
                return
            else:
                print('Enter a numeric value that is more than 0')
    def print(self):
        if self.thesaurus.linked.lengthOfList()==0:
            self.thesauruschecker(2)#2
            return
        elif self.filename=='' and self.savefile=='':
            self.thesauruschecker(1)
            return
        else:
            print(f'The Thesaurus "{self.filename}" is printed here...')
            f=open(self.filename,'r')
            print(f.read())
            # self.thesaurus.linked.printThesaurus()
            print (" " * 2)
            os.system('pause')
            return
    def save(self): #save thesaurus #error from sort, make sure sorted synpynm
        if self.thesaurus.linked.lengthOfList()==0:
            self.thesauruschecker(2)#2
            return
        elif self.filename=='' and self.savefile=='': # thesaurus made but yet to save it as a file
            self.thesauruschecker(1)
            return
        thesaurus.save(self.filename)
        return
    def saveAs(self): #error from sort, make sure sorted synpynm
        if self.thesaurus.linked.lengthOfList()==0:
            self.thesauruschecker(2)#2
            return
        else:
            while True:
                self.savefile=input('Please enter new filename or press 0 to return: ')
                if self.savefile=='0':
                    return
                isExist= os.path.exists(f'{self.path}\{self.savefile}')
                if isExist==True:
                    print('Filepath already exists, please input another name')
                elif isExist==False:
                    with open(self.savefile,'w') as f:
                        f=open(self.savefile,'w')
                        f.write(self.thesaurus.linked.printThesaurus(self.choice))
                        print(f'Your file "{self.savefile}" has been saved')
                        self.filename=self.savefile # ensure u can use filename and check file in other functions
                        os.system('pause')
                    return
    def exit(self):
        print('Bye, thanks for using ST1507 DAAA: Thesaurus Based Text Processor ')
        sys.exit(0)
    def thesauruschecker(self,number):
        if number==1:
            print('You have not made a Thesaurus file yet, prompting to save as a new file first')
            self.saveAs()
            return
        if number ==2:
            print('Thesaurus has not yet been made, please make one first')
            return




    
if __name__ == "__main__": #ensures it is not called by other modules
    
    print("\n"+"*"*55)
    print('* ST1507 DSAA: Welcome to:'+' '*28+'*')
    print("*"+" "*53+"*")
    print("* ~ Thesaurus Based Text Processing Application ~     *")
    print("*"+"-"*53+"*")
    print("*"+" "*53+"*")
    print("* - Done By: Nevan Ang Kai Wen"+" "*24+"*")
    print("*"*55+"\n\n")
    os.system('pause')
    linkedlist=SortedList()
    thesaurus=Thesaurus(linkedlist)
    userinput1=DisplayMenu(thesaurus) #obj data describing object should be bundled into the object
    userinput1.menu()  
# empyty lkeyowrd mention error must add at least one synonym for each keyword
# capital y or small y should both be accept.isupper?
#