# 1

write_path='C:/Users/admin/OneDrive/Desktop/friends.txt'

def read_file():
        try:
            file=open(write_path,'r')
            file1=file.read()
            print(file1)
        except Exception as error:
              print(f'error : {error}')
        

read_file()

# 2

def create_file():
      file2=open(write_path,'a')
      file_2=file2.write('hello')
      print(file_2)
create_file()

# 3

def writ_file():
      friend_name=input('enter name')
      file3=open(write_path,'a')
      file_3=file3.write(friend_name)
      print(file_3)
writ_file()


      













