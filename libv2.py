import json
import os
class Book:
    def __init__(self,title,author,available):
        self.title=title
        self.author=author
        self.available=available
    def convert(self):
        return {"title":self.title,"author":self.author,"available":self.available}
    



class Library:
    def __init__(self):
        self.book=[]
    def view(self):
        for index, book in enumerate(self.book, start=1):
            print(f"{index}. {book}")
    
def load():
    with open("lib.json","r") as file:
       return json.load(file)

library=Library()
def add():
    a=input("enter book name to add:")
    b=input('author of the book:')
    book1=Book(a,b,"available")
    library.append(book1.title)
    p=book1.convert()
    
    with open("lib.json","w") as file:
            json.dump(p,file)
def remove():
    a=input("enter book name to remove:")
    l=load()
    for book in l:
        if book['title'].split().lower()==a.split().lower():
            l.remove(book)
            break
def bowwor():

    



    


        
