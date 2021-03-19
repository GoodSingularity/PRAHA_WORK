import hashlib
import sys
def data(Lines, directory):
    #check each line of text
    for line in Lines:
        #split to elements
        arr= (line.strip()).split()
        #if there are 3 elements, check again
        if (len(arr) ==3):
            #Catch error for open function, if cant, text = " NOT FOUND" because file cant be open.
            try:
                #Based on what user've typed in command line arguments, check if It is md5, sha1, sha256 and calculate hash.
                if (arr[1] == "md5"):
                    myhash=hashlib.md5(open(directory+arr[0], 'rb').read()).hexdigest()
                    

                if (arr[1] == "sha1"):
                    myhash=hashlib.sha1(open(directory+arr[0], 'rb').read()).hexdigest()
                if (arr[1] == "sha256"):
                    myhash=hashlib.sha256(open(directory+arr[0], 'rb').read()).hexdigest()
                ############################################################################################################
                
                #If hash sum  == last parameter of command line arguments', text = OK
                if (myhash == arr[2] ):
                    text = " OK"
                #If not, text = FAIL
                else:
                    text = " FAIL"

            except OSError as e:
                    text = " NOT FOUND"
            #print filename text
            print(arr[0] + text)
            pass
def main(argv):
    try:

        file1 = open(sys.argv[1], 'r')

        Lines = file1.readlines()
        directory= sys.argv[2]
        data(Lines, directory)
    except OSError as e:
        print("Such file does not exist.")
        pass

if __name__ == "__main__":
    main(sys.argv)
