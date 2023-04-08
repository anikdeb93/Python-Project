
pc = {
    # "1": {
    #     "os": "Windows",
    #     "status": "fail"
    # },
    # "2": {
    #     "os": "windows",
    #     "status": "pass"
    # },
    # "3": {
    #     "os": "windows",
    #     "status": "weak"
    # }
}


def add_pc():
    pcnum = input("Enter PC number: ")

    if pcnum not in pc:
        os = input("Enter operating system : ")
        status = input("Enter PC status : ")

        newpc = {
            pcnum: {
                "os": os,
                "status": status
            }
        }

        pc.update(newpc)
        print(" PC added successfully!")

    else:
        print("PC number already given!")

    


def all_pcs_display():
    print(pc)
    


def remove_pc(pc_num):
    if pc_num in pc:
        pc.pop(pc_num)
        print("You removed the PC ")
    else:
        print("PC number doesn't given in the dataset")
    


def update_pc(pc_num):
    if pc_num in pc:
        os = input("Enter update OS name: ")
        status = input("Enter update status: ")
        pc[pc_num]["os"] = os
        pc[pc_num]["status"] = status
    else:
        print(" search PC not found.")
     


def display_individual(pc_num):
    if pc_num in pc:
        print(pc[pc_num])
    else:
        print(" search PC not found.")
    


def search_pc(pc_num):
    if pc_num in pc:
        print("search pc is found!")
    else:
        print(" search PC is not found.")
    


def store_to_file():
    file = open("pc.txt", "w")
    file.write(str(pc))
    file.close()
    pass


if __name__ == "__main__":

    program_on = True

    while program_on:
        print("\n HELLO ANIK DEBNATH WELCOME TO PYTHON PROGRAMMING COURSE")
        print("1. Add pc")
        print("2. Remove pc")
        print("3. Update pc")
        print("4.  All pcs Display")
        print("5. individual pc Display ")
        print("6. Search pc")
        print("7. Store function in file")
        print("8. Quit")
        choice = input("Enter number: ")

        if choice == '1':
            add_pc()

        elif choice == '2':
            remove_pc_num = input("Enter the pc number: ")
            remove_pc(remove_pc_num)

        elif choice == '3':
            recent_pc = input("Enter PC Number to update: ")
            update_pc(recent_pc)

        elif choice == '4':
            all_pcs_display()

        elif choice == '5':
            recent_pc = input("Enter pc number: ")
            display_individual(recent_pc)

        elif choice == '6':
            recent_pc = input(" Enter pc number: ")
            search_pc(recent_pc)
        elif choice == '7':
            store_to_file()
        


        elif choice == '8':
            print("Program Executed ")

            program_on = False

        else:
            print("Incorrect option.please enter correct option")



  
