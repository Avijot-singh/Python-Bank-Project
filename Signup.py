#Here we will be working on the signup page for the banking system
class Signup:
    emails = ['avijot2']
    account_number = 11001101
    
    def __init__(self):
        self.Fname = input("Please Enter Your First Name:  ")
        self.Lname = input("Please Enter Your Last Name:   ")
        self.DOB = input("Please Enter Your Date Of Birth in DD/MM/YYYY format:   ")
        
        while(True):
            self.Email = input("PLease Enter your Email:  ")
            if self.Email in Signup.emails:
             print("This email is already in use.Please Login or use another email.")
             
            else:
                Signup.emails.append(self.Email)
                break
    
    def details(self):
        print("First Name:", new_signup.Fname)
        print("Last Name:", new_signup.Lname)
        print("Date Of Birth:", new_signup.DOB)
        print("Email:", new_signup.Email)
        
        

# Create an instance of Signup to test the input
new_signup = Signup()
new_signup.details()
