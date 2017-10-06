"""
Info ---------------------------+
+Name: Jiachang Xu
+Course: Computer Science 101
+Assignment: Final Project Fall 2014
+Due Date: 3 December 2014
+-------------------------------+

*Program Description*
 To read the file for a list of employees and calculate their salary and print them to the monitor.
"""


def Single(TI):
    if TI <= 1710:
        Tax = round(0,3)
        NI = round(TI - Tax,3)
    elif 1710 < TI <= 20930:
        Tax = round(87.00 + 0.03 * (TI - 1710),3)
        NI = round(TI - Tax,3)
    elif 20930 < TI <= 28790:
        Tax = round(742.40 + 0.08 * (TI - 20930),3)
        NI = round(TI - Tax,3)
    elif TI >= 28790:
        Tax = round(1449.60 + 0.11 * (TI - 28790),3)
        NI = round(TI - Tax,3)
    return Tax, NI


def Joint(TI):
    if TI <= 3420:
        Tax = round(0,3)
        NI = round(TI - Tax,3)
    elif 3420 < TI <= 47120:
        Tax = round(330.00 + 0.04 * (TI - 3420),3)
        NI = round(TI - Tax,3)
    elif 47120 < TI <= 57580:
        Tax = round(1905.40 + 0.09 * (TI - 47120),3)
        NI = round(TI - Tax,3)
    elif TI >= 57580:
        Tax = round(2899.20 + 0.11 * (TI - 57580),3)
        NI = round(TI - Tax,3)
    return Tax, NI


def Output(FileStatus, TI):
    if FileStatus == "S" or FileStatus == "s":
        Tax, NI = Single(TI)
        Status = "Single"
    elif FileStatus == "J" or FileStatus == "j":
        Tax, NI = Joint(TI)
        Status = "Joint"
    return Status, Tax, NI


def Header():
    print(" Final Project Fall 2014")
    print(" Jiachang Xu")
    print(" Computer Science 1")
    print("\n")
    return


def Menu():
    print("A.  Read course data from a file to update the list")
    print("B.  Print employee list content to a file")
    print("C1. Sort the list of students and print it to the monitor alphabetically based on last name")
    print("C2. Sort the list of students and print it to the monitor in a descending order based on income")
    print("D.  Print the list of employees in a tabular form to the monitor only (Name, Gross Salary, Status, Taxes, NetSalary)")
    print("E.  Search the list of employees and print all the details of an employee to the monitor")
    print("F.  Add a new employee to the list")
    print("G.  Delete an employee from the list")
    print("H.  Edit employe information (Name and Gross Income only)")
    print("I.  Exit")
    return


def Choose():
    Operation = input("Enter the code of operation that you want to execute: ")
    return Operation


def OperationA(): # Operation A
    InputName = input("Enter the input file name: ")
    InputFile = open(InputName)
    
    List = list()
    
    for line in InputFile:
        Dict = dict()
        lines = line.strip()
        FirstName, LastName, FileStatus, FileTI = lines.split()
        TI = eval(FileTI)
        Dict['First Name'] = FirstName
        Dict['Last Name'] = LastName
        Dict['Name'] = (FirstName + " " + LastName)
        if FileStatus == "S" or FileStatus == "s" or FileStatus == "J" or FileStatus == "j":
            if TI >= 0:
                Status, Tax, NI = Output(FileStatus, TI)
                if FileStatus == "S" or FileStatus == "s":
                    Dict['Status'] = 'Single'
                elif FileStatus == "J" or FileStatus == "j":
                    Dict['Status'] = 'Joint'
                Dict['Income'] = str(TI)
                Dict['Tax'] = str(Tax)
                Dict['Net'] = str(NI)
            elif TI < 0:
                if FileStatus == "S" or FileStatus == "s":
                    Dict['Status'] = 'Single'
                elif FileStatus == "J" or FileStatus == "j":
                    Dict['Status'] = 'Joint'
                TI = "Negative value is invalid."
                Tax = ""
                NI = ""
                Dict['Income'] = TI
                Dict['Tax'] = Tax
                Dict["Net"] = NI
        else :
            Status = (FileStatus + " is an invalid status")
            TI = ""
            Tax = ""
            NI = ""
            Dict['Status'] = Status
            Dict['Income'] = TI
            Dict['Tax'] = Tax
            Dict["Net"] = NI
        List.append(Dict)
    return List


def OperationB(List): # Operation B
    List = OperationA()
    
    OutputName = input("Enter the output file name: ")
    OutputFile = open(OutputName, "w")
    OutputFile.write(("%-30s"%("Name"))+("%-30s"%("Status"))+("%-30s"%("Gross Salary"))+("%-30s"%("Taxes"))+"Net Salary\n")
    OutputFile.write("=======================================================================================================================================\n")

    TotalTI = 0
    TotalTax = 0
    TotalNI = 0
    Count = 0
    
    for Dict in List:
        OutputFile.write(("%-30s"%(Dict['Name']))+("%-30s"%(Dict['Status']))+("%-30s"%(Dict['Income']))+("%-30s"%(Dict['Tax']))+str(NI)+"\n")
        if eval(Dict['Income']) >= 0:
            TotalTI += eval(Dict['Income'])
            TotalTax += eval(Dict['Tax'])
            TotalNI += eval(Dict['Net'])
            Count += 1

    OutputFile.write("---------------------------------------------------------------------------------------------------------------------------------------\n")
    OutputFile.write(("%-30s"%("Average"))+("%-30s"%(str(round(TotalTI/Count, 2))))+("%-30s"%(str(round(TotalTax/Count, 2))))+("%-30s"%(str(round(TotalNI/Count, 2))))+"\n")
    OutputFile.close()
    return


def OperationC1(List): # Operation C1
    List = OperationA()
    List.sort(Dict['Name'])
    return List


def OperationC2(List): # Operation C2
    List = OperationA()
    List.sort(Dict['Income'])
    List.reverse()
    return List


def OperationD(List): # Operation D
    List = OperationA
    print(("%-30s"%("Name"))+("%-30s"%("Status"))+("%-30s"%("Gross Salary"))+("%-30s"%("Taxes"))+"Net Salary")
    print("=======================================================================================================================================")

    TotalTI = 0
    TotalTax = 0
    TotalNI = 0
    Count = 0

    for Dict in List:
        print(("%-30s"%(Dict['Name']))+("%-30s"%(Dict['Status']))+("%-30s"%(Dict['Income']))+("%-30s"%(Dict['Tax']))+str(NI))
        if eval(Dict['Income']) >= 0:
            TotalTI += eval(Dict['Income'])
            TotalTax += eval(Dict['Tax'])
            TotalNI += eval(Dict['Net'])
            Count += 1

    print("---------------------------------------------------------------------------------------------------------------------------------------")
    print(("%-30s"%("Average"))+("%-30s"%(str(round(TotalTI/Count, 2))))+("%-30s"%(str(round(TotalTax/Count, 2))))+("%-30s"%(str(round(TotalNI/Count, 2)))))
    print("\n")
    return


def OperationE(List): # Operation E
    List = OperationA()
    SearchLastName = input("Enter the last name the person that you want to search: ")
    print(("%-30s"%("Name"))+("%-30s"%("Status"))+("%-30s"%("Gross Salary"))+("%-30s"%("Taxes"))+"Net Salary")
    print("=======================================================================================================================================")

    for Dict in List:
        if Dict['Last Name'] == SearchLastName:
            print(("%-30s"%(Dict['Name']))+("%-30s"%(Dict['Status']))+("%-30s"%(Dict['Income']))+("%-30s"%(Dict['Tax']))+str(NI))

    print("---------------------------------------------------------------------------------------------------------------------------------------")
    return


def OperationF(List): # Operation F
    List = OperationA()
    AddFirstName = input("Enter the first name of the new employee: ")
    AddLastName = input("Enter the last name of the new employee: ")
    AddStatus = input("Enter the filing status of the new employee: ")
    TI = eval(input("Enter the taxable income of the new employee: "))
    Dict = dict()
    Dict['First Name'] = AddFirstName
    Dict['Last Name'] = AddLastName
    Dict['Name'] = (AddFirstName + " " + AddLastName)
    Dict['Income'] = str(TI)

    if AddStatus == "S" or AddStatus == "s":
        Dict['Status'] = Single
        Tax, NI = Single(TI)
    elif AddStatus == "J" or AddStatus == "j":
        Dict['Status'] = Joint
        Tax, NI = Joint(TI)

    Dict['Tax'] = str(Tax)
    Dict['Net'] = str(NI)        
    return List


def OperationG(List): # Operation G
    List = OperationA()
    DeleteLastName = input("Enter the last name of the employee that you want to delete from the database: ")

    for Dict in List:
        if Dict['Last Name'] == DeleteLastName:
            List.remove(Dict)
    return List


def OperationH(List): # Operation H
    EditLastName = input("Enter the last name of the employee that you want to edit: ")
    TI = input("Enter the taxable income that you want to change into: ")

    for Dict in List:
        if Dict['Last Name'] == EditLastName:
            if Dict['Status'] == "Single":
                Tax, NI = Single(TI)
            elif Dict['Status'] == "Joint":
                Tax, NI = Joint(TI)
            Dict['Income'] = str(TI)
            Dict['Tax'] = str(Tax)
            Dict['Net'] = str(NI)
    return List


def OperationI():
    print("Program terminated on request.")
    print("Thank you for using tax program. Have a nice day.")
    return


def Main():
    Header()
    Menu()
    CountOperation = 0
    while CountOperation >= 0:
        Operation = Choose()
        if Operation == "A" or Operation == "a":
            OperationA()
        elif Operation == "B" or Operation == "b":
            OperationB(List)
        elif Operation == "C1" or Operation == "c1":
            OperationC1(List)
        elif Operation == "C2" or Operation == "c2":
            OperationC2(List)
        elif Operation == "D" or Operation == "d":
            OperationD(List)
        elif Operation == "E" or Operation == "e":
            OperationE(List)
        elif Operation == "F" or Operation == "f":
            OperationF(List)
        elif Operation == "G" or Operation == "g":
            OperationG(List)
        elif Operation == "H" or Operation == "h":
            OperationH(List)
        elif Operation == "I" or Operation == "i":
            OperationI()
            break
        else :
            print("The code you entered is not valid. Please try again.")
        CountOperation += 1
    return


Main()
