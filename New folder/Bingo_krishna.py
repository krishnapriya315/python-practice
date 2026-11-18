# num=int(input('please enter number'))
# for i in range(1,num+1):
#     if(i%5==0):
#         print('bingo')

#     else:
#         print(i)


age=int(input('please enter our age'))
valid_id=input('do you have a valide is card (\n)')

if(valid_id=='y'):
    valide_id=True
else:
    valid_id=False


# verifiying eligiblity to vote
print('we are cheking your eligiblity')

if(age>=18):
    if(valid_id):
        print('you are eligible to vote')
    else:
        print('you are not eligible to vote')
        print('you should be 18or above to be eligibole')

print('******************************')

# coing the same process using logical operetor 
if(age>=18):
    if(valid_id):
        print('you not eligible to vote')
    else:
        print('you  eligible to vote')
        print('you eligible to vote')




    
     
   

