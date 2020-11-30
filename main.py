import datetime
import os

#this should be set before by the user
password='bhushan'

#set the path where you have the program file
PATH=os.getcwd()+'/logs/'

#ask the user 1]Professional or 2]Private
def ask_choice():

    choice=int(input("1]Private\n2]Profssionl\nEnter your choice\n"))


    #if private ask for password
    if choice==1:

        while True:
            pass_check=input("enter the password:")
            if check_password(pass_check):
                option=get_option()
                if option==1:
                    read_particular('private')
                elif option==2:
                    read_previous('private')
                elif option==3:
                    read_complete('private')
                elif option==4:
                    log_entry('private')
                break
            else:
                print('password doesn\'t match' )

    elif choice==2:
        option=get_option()
        if option==1:
            read_particular('professional')
        elif option==2:
            read_previous('professional')
        elif option==3:
            read_complete('professional')
        elif option==4:
            log_entry('professional')

    else:
        print("invalid choice")
        ask_choice()
def get_option():
    print("What you want to perform")
    print("""1 read the particular day file (enter the date)
2 read the previous number of days files togerther (enter the number of days)
3 read the complete log_entry
4 enter the todays contents
            """)
    inp=input()
    try:
        inp=int(inp)
        if inp<=4 and inp>0:
            return inp
        else:
            return get_option()

    except:
        get_option()

def check_password(word):
    if word==password:
        return True
    return False



#option 1
def read_particular(access_mode):
    day=input("enter the date in the form of YYYY-MM-DD\n")
    file_name=day+'.txt'
    PATH=os.getcwd()+'/logs/'

    if access_mode=='private':

        PATH+='private/'

    else:

        PATH+='professional/'

    files=os.listdir(PATH)
    if file_name in files:
        content=open(PATH+file_name,'r')
        print(content.read())
        content.close()
    else:
        print("noting to show")

#option 2
def read_previous(access_mode):

    PATH=os.getcwd()+'/logs/'
    if access_mode=='private':
        PATH+='private/'
    else:
        PATH+='professional/'
    inp=int(input('enter the number of days files you want:\n'))
    #list all the files
    files=os.listdir(PATH)
    files.sort(reverse=True)
    count=0

    for file in files:
        print('FILE NAME: ',file)
        with open(PATH+file,'r') as f:
            print(f.read())
        count+=1
        if count==inp:
            break

#option 3

def read_complete(access_mode):
    PATH=os.getcwd()+'/logs/'
    
    if access_mode=='private':
        PATH+='private/'
    else:
        PATH+='professional/'


    files=os.listdir(PATH)
    files.sort(reverse=True)


    for file in files:
        print('FILE NAME: ',file)
        with open(PATH+file,'r') as f:
            print(f.read())


#option 4
def log_entry(access_mode):
    #if today file not present then create today's file
    PATH=os.getcwd()+'/logs/' #here the directory path should be given
    #based on the access_mode
    if access_mode=='private':
        PATH+='private/'
    else:
        PATH+='professional/'


    check_file=os.listdir(PATH) #this will list all the files in the path

    today=datetime.date.today()

    #if file not created yet
    if str(today)+'.txt' not in check_file:
        #create a file
        file=open(PATH+str(today)+'.txt','w')

        #ask for the entries from the user
        print("Enter the contents you want to insert into the file(Press q to quit):")
        inp=''
        while True:
            inp=input()
            if inp=='q' or inp=='Q':
                break
            file.write('\n'+inp)
        file.close()


    #if you want to add something for the existing file
    else:
        #now we need to previous contents of the file also
        file=open(PATH+str(today)+'.txt','r')
        prev_content=file.read()
        file.close()

        #display the contents that already present
        print('The contents fo the file that already exists are:')
        print(prev_content)
        #open the file to add contents
        file=open(PATH+str(today)+'.txt','w')
        file.write(prev_content)

        #ask the user to add contents
        print("Enter the contents you want to insert into the file(Press q to quit): ")
        inp=''
        while True:
            inp=input()
            if inp=='q' or inp=='Q':
                break
            file.write('\n'+inp)
        file.close()



#driver program
ask_choice()
