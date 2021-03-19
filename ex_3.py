#dependencies
import os
import random  
import string  
from datetime import datetime
from pathlib import Path


###################################################################################################################################
#assertion
#The easiest way to think of an assertion is to liken it to a raise-if statement (or to be more accurate, a raise-if-not statement). 
#An expression is tested, and if the result comes up false, an exception is raised.
###################################################################################################################################

#First test case
###################################################################################################################################
class TestFileList:
    #random ic_id
    tc_id = random.randint(1,21)*5
    #random name
    name = ''.join((random.choice(string.ascii_lowercase) for x in range(5))) 

    # 	[prep] If the current system time taken as an integer since the Unix Epoch is not divisible by 2, interrupt the test case.
    def prep(self):
        now = datetime.now() # time object
        time_int=now.strftime('%s') #string current date to integer, UNIX EPOCH
        time_int = int(time_int)
        #Unix Epoch is not divisible by 2, interrupt the test case. Interupted!
        assert(time_int%2 == 0), str(time_int)+" | Current computer time is not divisable by 2"
    #   [run] List all files in the user’s home directory.
    def run(self):
        directory = '/home/'
        assert (os.path.exists(directory) == True), "Dir does not exist"
        files = os.listdir(directory)

        for f in files:
            print(f)
        pass
    #[clean_up] (do nothing).
    def clean_up(self):
         pass
    #Method execute that defines the common workflow of a test and handles all exceptions.     
    def execute(self):
        self.prep()
        self.run()
        self.clean_up()

###################################################################################################################################

#Second test case
###################################################################################################################################
class TestRandomFile:

    tc_id = random.randint(1,21)*5
    name = ''.join((random.choice(string.ascii_lowercase) for x in range(5))) 
    #	[prep] If the current host’s RAM is less than one gigabyte, interrupt the test case.
    def prep(self):
        mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') 
        mem_gib = mem_bytes/(1024.**3) 
        assert(mem_gib >= 1.0), "Less than 1.0GB ram"
    # •	[run] Create a file test of size 1024 KB with random contents.
    def run(self):
        filename = Path('./test')
        assert(os.path.exists("./test") == True), filename.touch(exist_ok=True)


        with open('./test', 'wb') as fout:
            fout.write(os.urandom(1024)) 
        pass
	#[clean_up] Remove the file test.
    def clean_up(self):
        assert(os.path.exists("./test") == True), os.remove("./test")
    #Method execute that defines the common workflow of a test and handles all exceptions.   
    def execute(self):
        self.prep()
        self.run()

###################################################################################################################################




obj = TestFileList()
obj.execute()
obj2 = TestRandomFile()
obj2.execute()


