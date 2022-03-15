#!/usr/bin/python3
#andres
#Tue 15 Mar 2022 04:05:32 AM EDT

#moved all commands under except to prevent double page printing on first program run

page='0'
#attempts to create a file
try:
    ofx=open("scroll_z.txt", 'x', encoding="UTF-8")
    ofx.write("Page"+page+"\n")
    print("Scroll Z forged with success.")
    ofx.close()
#if file can't be created, ignores the first page and appends the next ones    
except:
    print("File Already Exists.Appending to existing file.")
#Extracts the page number from the last line using a for loop
    with open("scroll_z.txt") as f:
        for line in f:
             pass
        last_line=line
#Converts the number into integer so that +1 can be added every time
    ll=(int(last_line[4]))
    ll1= ll+1
#if number reaches 0, deletes this only works with single digits
    if ll1==10:
        print("9 is the limit of pages we can have for now. This process shall reset.")
        import os
        os.remove("scroll_z.txt")
        quit()
#keeps appending pages until page reaches 10
    else:
        ssl= str(ll1)
        type(ssl)
        ofa=open("scroll_z.txt",'a',encoding="UTF-8")
        ofa.write("Page"+ssl+"\n")
        ofa.close()
    
