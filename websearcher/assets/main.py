import os, time
from save import *

os.system("cls")

def main():
    os.system("cls")
    print("Qwerty OS - Web Searcher\n")
    webInput = str(input("] "))

    if webInput == "":
        os.startfile("commandismissing.vbs")
        main()
    
    if webInput == "help":
        os.system("cls")
        os.system("type commandlist.txt")
        print("\n")
        os.system("pause")
        main()

    if webInput == name1:
        os.system("start " + web1)
        main()
    
    if webInput == name2:
        os.system("start " + web2)
        main()
    
    if webInput == name3:
        os.system("start " + web3)
        main()

    if webInput == "exit":
        os.startfile("back.bat")
        exit(0)
    
    else:
        os.startfile("wrongcommand.vbs")
        main()
    
main()