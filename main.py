class Main:
    def __init__(self):
        Main.MainMenu(self)
    
    def MainMenu(self):
        while True:
            print("1)Login\n2)Register\n0)Exit")
            choice=int(input("Enter choice: "))
            from user import User
            new_user = User()
            if choice == 1:
                new_user.login()
            elif choice == 2:
                new_user.register()
            elif choice == 0:
                break            
            else:
                print("Please enter correct choice")
                continue
                 
main = Main()