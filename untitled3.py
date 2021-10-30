from tkinter import *#imports tkinter
import random#imports random package

root = Tk()#creates window
root.title("Number Sorter")#sets name of window
root.geometry("400x400")#sets size of window

random_number_list = Label(root)#creates random number label
random_number_sorted_list = Label(root)#creates sorted number label

def randomlist():#function
    randomlist = random.sample(range(10,50),15)#generates random numbers
    random_number_list["text"] = "random numbers: "+ str(randomlist)#sets randomnumberlist to randomlist
    randomlist.sort()#sorts random numbers
    random_number_sorted_list["text"] = "sorted numbers: "+ str(randomlist)#sets  sortedlist to randomlist

btn = Button(root,text="generate numbers", command=randomlist)#creates button
btn.place(relx=0.5,rely =0.4,anchor=CENTER)#sets button location
random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)#sets randomnumberlist location
random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)#sets randombumbersortedlist location
root.mainloop() #ends program