import time
class createProjects:
    def __init__(self):
        pass
    
    def create(self,email):
        while True:
            print("1)Create Project\n2)View All Projects\n0)Exit")
            choice=int(input("Enter choice: "))
            if choice == 1:
                title=input("Enter title: ")
                details=input("Enter details: ")
                total_target=input("Enter total target: ")
                while True:
                    start_date=input("Enter start date(d/m/y): ")
                    end_date=input("Enter end date(d/m/y): ")
                    formatted_date1 = time.strptime(start_date, "%d/%m/%Y")
                    formatted_date2 = time.strptime(end_date, "%d/%m/%Y")
                    if start_date > end_date:
                        print("start date must be smaller than end date")
                    else:
                        data=[email,title,details,total_target,start_date,end_date]
                        open("createData.txt","a").write("|".join(data))
                        open("createData.txt","a").write("\n")
                        print("created")
                        break    
            elif choice == 2:
                show_data=open("createData.txt","r").readlines()
                for i in show_data:
                    print(i)     
            elif choice == 0:
                break            
            else:
                print("Please enter correct choice")
            continue
        