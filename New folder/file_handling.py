# **********************************
# ************file handling********************
# **********************************


# 
filepath = 'D:/PGP_DATA_SIENCE_AND_AIML/python/test_file.txt'
relative_filepath= 'test_file.txt'
file =open(filepath,'r')        
content =file.read()    
    #print(content)
file.close() 

# trying using rilativefilepath 

def read_file_filepath():
    file_1=open(relative_filepath,'r')  #relative file path
    content_1=file_1.read()
    print(content_1)
    print(type(content_1))
    file.close      #a single string


# file read ()willreturn all the value as a simple string 

# reada single line
def read_lines():
    file=open(relative_filepath,'r')
    # reads all lines and populater the list 'content'
    content=file.readline()
    print(content)

    for  line in content:
        print(line)
        print(type(content))


read_lines()

# **********************
# ************write a file*********************
# ********************************
write_path='student_name'

def write_file():
    file=open(write_path,'w')
    file.close()

write_file()



def write_into_file():
    file=open(write_path,'w')
    file.write("gowtham")
    file.close()

write_into_file()
    

def student_name():
    file=open(write_path,'w')
    file.write("grace")
    file.write('vishnu')
    file.write('keerthi')
    file.write('anjaly')
    file.close()

student_name()

# append data into the file

def append_file():
    file=open(write_path,'a')
    file.write('keerthi')
    file.close

append_file()


# genaric funtion to append  a data to a function.

def append_data(write_into_file,name):
    file=open(write_into_file,'a')
    file.write('\n')
    file.write(name)
    file.close

append_data('text_file.txt','bsnl') #new file create aakum athinte ullil aayirikkum 'bsnl' ennu varuka


def append_data_new(write_into_file,name):
    with open(write_into_file,'a')as file:
        file.write('\n')
        file.write(name)
        
append_data_new('text_file.txt','airtel')



