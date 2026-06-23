import json
import os
import pathlib
if not os.path.exists("lib.json"):
    b=[{"title":"physics","author":"hc verma","aval":"available"}]
    with open("lib.json","w") as f:
        json.dump(b,f)
def load_json(name):
    with open(name,"r") as data:
        return json.load(data)
    


def save_json(filename,data):
    with open(filename,"w") as file:
        json.dump(data,file)



class Book:
    def __init__(self,title,author,aval):
        self.title=title
        self.author=author
        self.aval=aval
def add():
    data=load_json("lib.json")
    for book in data:
        print(f"the book {book['title']} of {book['author']} is {book['aval']}")
        
    a=input("Enter the name of the book wanted to add: ")
    if any (b['title']==a for b in data) :
        print("book already exist")
    else:  
        b=input("Enter the author of the book: ")
        c=input("enter if the book is available or not : ")

        book=Book(a,b,c)
        f={"title":book.title,"author":book.author,"aval":book.aval}
        data.append(f)
        save_json("lib.json",data)
        print("Book saved")
def remove():

    data=load_json("lib.json")
    for book in data:
        print(f"the book {book['title']} of {book['author']} is {book['aval']}")
    a=input("enter which book to remove:").strip().lower()
    for book in data:
        if book['title'].strip().lower()==a:
            data.remove(book)
            save_json("lib.json",data)
        break
    else:
        print('no such book in library')
def view():
    data=load_json("lib.json")
    for book in data:
        print(f"the book {book['title']} of {book['author']} is {book['aval']}")
def update():
    data=load_json("lib.json")
    for book in data:
        print(f"the book {book['title']} of {book['author']} is {book['aval']}")
    s=input("which book status to uptate:").strip().lower()
    for book in data:
        if book['title'].strip().lower()==s :
            if book['aval']=="available":
                book['aval']="not available"
                save_json("lib.json",data)
            else:
                book['aval']= "available"
        else:
            print('no such book in library ')
            break
while True:
    print('welcome to library \nselect option \n1.view books\n2.add a book \n3.delete a book \n4.borrow \n5.return \n6.press enter to quit')
    l=int(input('tell your option:'))
    if l==1:
        view()
    elif l==2:
        add()
    elif l==3:
        remove()
    elif l==4:
        update()
    elif l==5:
        update()
    else :
        break
