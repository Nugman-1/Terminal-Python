import os

import sys

import getpass

import time
from time import sleep

import rich
from rich.progress import Progress
from rich.console import Console
from rich.table import Table

from ency import ENCRYPT

CWD = os.path.dirname(os.path.abspath(sys.argv[0]))
def create_user():
    InputCredentialsList = []
    InputCredentialsList.append(str(input("please input Your Name") + ".n"))
    InputCredentialsList.append(str(input("please input Your Username") + ".u")) 
    InputCredentialsList.append(str(input("please input Your Password") + ".p"))
    File = open(os.path.join(CWD, "LoginData.txt"), "w") 
    for Object in InputCredentialsList:
        EncryptedCredentials = ENCRYPT.encrypt(DataToEncrypt=Object, TypeOfCypher="sub")
        File.writelines(EncryptedCredentials+ "\n")
    print("[green]User added[/]")
    File.close()
    

def clear_console():
    # Clears the console
    print(chr(27) + "[2J")


def check_credentials():
    Counter = 0
    Credentials2DList = []
    Y = 3
    Z = 0
    
    File = open(os.path.join(CWD, "LoginData.txt"), "r")
    File_Data = File.readlines()
    if File_Data == []:
        File.close()
        create_user()
        
    File = open(os.path.join(CWD, "LoginData.txt"), "r")    
    File_Data = File.readlines()
    File.close
    
    # Sanitises each Item insde File data by Removing newline
    for Item in File_Data:
        File_Data[Counter] = Item.replace("\n", "")     
        Counter = Counter + 1
        
    Counter = int(len(File_Data) / 3)
    
    while Counter != 0:
        Credentials2DList.append(File_Data[Z:Y])
        Z = Z + 3
        Y = Y + 3
        Counter -= 1
        
    return Credentials2DList


def identify_fix(Credentials2DList):
    ValidateList = []
    counter = -1
    ValidateList_2 = []
    templist = []
    for Object in Credentials2DList[0]:
        temp = ENCRYPT.decrypt(DataToDecrypt=Object, TypeOfCypher="ey_one")
        templist.append(temp)
        
    Credentials2DList.clear()
    Credentials2DList = templist
        
    
    
    
    
    # splits off the validation Letter for every value in a new line
    for list in Credentials2DList:
        counter = counter + 1
        for object in Credentials2DList[counter]:
            ValidateDidgit = object.split(".")
            ValidateList.append(ValidateDidgit[1])
    
    Length = len(Credentials2DList)
    while Length != 0:
        Length = Length -1
        counter = 3
        ValidateList_2.append(ValidateList[:3])
        while counter != 0:
            counter = counter -1
            ValidateList.pop(0)
            
    #Places the vilidation Digits in groupes of threes   
    Length = len(ValidateList_2)
    Counter = 0
    for list in ValidateList_2:
        TempVar = ""
        for Char in list:
            TempVar = TempVar + Char
        ValidateList_2[Counter] = TempVar
        Counter = Counter + 1
        
    # checks for Letter  PNU corisponding to Password Name and Username
    # Identifys and Removes broken data
    Counter = -1
    for ValidationDigits in ValidateList_2:
        Counter = Counter + 1
        if ValidationDigits != "nup":
            print("Error Found in UserCredentils in section", Counter + 1, "Fixing")
            Credentials2DList.pop(Counter)
            File = open(os.path.join(CWD, "LoginData.txt"), "w")
            for List in Credentials2DList:
                for Object in List:
                    File.write(Object)
                    File.write("\n")
            print("Fixed")
            File.close
  
            
def login(Credentials2DList):
    
    ValidToken = 0
    Counter2 = -1
    for List in Credentials2DList:
        Counter2 = Counter2 + 1
        Counter = 0
        for Object in List:
            if Counter == 0:
                List[Counter] = Object.replace (".n", "")
            if Counter == 1:
                List[Counter] = Object.replace (".u", "")
            if Counter == 2:
                List[Counter] = Object.replace (".p", "")
            Counter = Counter + 1
            Credentials2DList[Counter2] = List
            
    while ValidToken == 0:
        UserInputUsername = getpass.getpass("Username: ")
        UserInputPassword = getpass.getpass("Password: ")
        
        clear_console()
        
        Counter = 0
        for List in Credentials2DList:
            if UserInputUsername == List[1] and UserInputPassword == List[2]:
                UserName = List[0]
                print("ok", UserName)
                ValidToken = ValidToken + 1
                
                
    return UserName           


def loading_screen_bar():

    with Progress() as progress:

        task1 = progress.add_task("[red]Loading...", total=1000)
        task2 = progress.add_task("[green]Processing...", total=1000)
        task3 = progress.add_task("[cyan]Setting Up...", total=1000)

        while not progress.finished:
            progress.update(task1, advance=1.85)
            progress.update(task2, advance=1.9)
            progress.update(task3, advance=1.7)
            time.sleep(0.02)
 
    
def loading_screen_str():
    

    console = Console()
    tasks = [f"task {n}" for n in range(1, 5)]

    with console.status("[bold green]Working on tasks...") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1)
            console.log(f"{task} complete")    
 
       
CommandsDict = {
    "Game":"placeholder"
}            
 
            
def table_of_commands(CommandsDict):

    table = Table(title="Avalible Commands")
    table.add_column("Commands", justify="right", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")                      
    for Command in CommandsDict: 
        table.add_row(Command,)    
    console = Console()
    console.print(table)
  
     
def console():
    
    #loading_screen_str()
    
    check_credentials()
    LIST_DATA=check_credentials()
    
    identify_fix(Credentials2DList=LIST_DATA)
    
    #login(Credentials2DList=LIST_DATA)

    #loading_screen_bar()
    
    #table_of_commands(CommandsDict=CommandsDict) 


console()

