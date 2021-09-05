#!/usr/bin/env python3.8
from user import User
from credentials import Info

def create_account(f_name,m_name,e_mail):
    new_user = User(f_name,m_name,e_mail)
    return new_user
def create_credentials(face_bookp,e_mailp):
    new_cred = Info(face_bookp,e_mailp)
    return new_cred
def save_account(user):
    user.save_user()
def save_credentials(credentials):
    credentials.save_info()
def display_users():
    return User.display_users()
def display_creds():
    return Info.display_info()
def main():
    print(" ")
    print(""" 
WELCOME TO PASSWORD LOCKER APPLICATION                           
""")
    print("Once more Welcome!!")
    print(" ")
    print(" ")
    while True:
        print("-" * 200)
        print("""The following short codes are used in this project!!
1. ca - Creation of an account
2. xx - Exiting the system
3. ds - Accounts display
4. gp - Password generation""")


        print(" ")
        print("      Enter a code of your choice!")
        print(" ")
        short_code = input() .lower()
        if short_code =='ca':
            print(" ")
            print("-" * 200)
            print("      CREATE A NEW ACCOUNT!")
            print(" ")
            print(" ")
            print("what is your first name?..")
            print(" ")
            f_name =input()
            print("What is your middle name?..")
            print(" ")
            m_name= input()
            print("what is your email address?..")
            print(" ")
            e_mail= input()
            print ("what is your facebook password?..")
            print(" ")
            face_bookp =input()
            print("what is your email password?..")
            print(" ")
            e_mailp= input()
            save_account(create_account(f_name,m_name,e_mail))
            print('\n')
            save_credentials(create_credentials (face_bookp,e_mailp))
            print('\n')
            print("-" * 156)
            print(f"New Account  {f_name } { m_name} { face_bookp } has been created")
            print('\n')
        elif short_code =='ds':
            if display_users():
                print(" ")
                print("The user name")
                print(" ")
                print('\n')
                for user in display_users():
                    print(f"{user.f_name}{user.m_name}")
                for credentials in display_creds():
                    print (f"{face_bookp}")
                    print(" ")

            else:
                    print('\n')
                    print("-" * 200)
                    print(" ")
                    print("                         PLEASE CREATE AN ACCOUNT ")
                    print("                    You have not created an account yet :( ")
                    print(" ")
        elif  short_code == 'gp':
            print(" ")
            print(" ")
            print("TO GENERATE A PASSWORD ADD IN YOUR FIRST NAME AND FACEBOOK BELOW!!")
            print(" ")
            list_of_inputs = [c for c in input()]

            # list_of_inputs= list(list_of_inputs)
            list_of_inputs.reverse()



            print (list_of_inputs)






        elif short_code == "xx":
            print("-" * 200)
            print(" ")
            print("                        THAX FOR DROPING IN!")
            print("                           Bye... Bye...")
            print(" ")
            print("-" * 200)
            break
        else:
            print("-" * 200)
            print(" ")
            print("                              RETRY!!")
            print(" ")
            print("                Please Select One Of The Options Provided")
            print(" ")

if __name__ == '__main__':

    main()
