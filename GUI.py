import tkinter
from tkinter import *
from tkinter import ttk

import tkinter as tk
from Toto3 import*
from tkinter.ttk import Combobox, Progressbar
import time

main_root = Tk()
main_root.title("Path Entry")
main_root.geometry("400x175")

container1 = Frame(main_root)
container1.pack()

label_path = Label(container1, text="Please enter Path")
label_path.grid(row=1, column=1, padx=10, pady=15)

entry_path = Entry(container1,width=50)
entry_path.grid(row=2, column=1, pady=15)


loading_root = Tk()
loading_root.title("Loading")
loading_root.geometry("300x200")

container2 = Frame(loading_root)
container2.pack()

label_load = Label(container2, text="Loading...")
label_load.grid(row=1, column=1, padx=10, pady=15)
label_done=Label(container2, text="Done")

root="ay betngan"

progress = Progressbar(container2, orient=HORIZONTAL, length=100, mode='determinate')
loading_root.withdraw()


word_root = Tk()
word_root.title("Word Entry")
word_root.geometry("250x200")

container3 = Frame(word_root)
container3.pack()

label_word = Label(container3, text="Please enter Word")
label_word.grid(row=1, column=1, padx=10, pady=15)

entry_word = Entry(container3)
entry_word.grid(row=2, column=1, pady=15)

word_root.withdraw()

show_root = Tk()
show_root.title("Result")
show_root.geometry("250x250")

container4 = Frame(show_root)
container4.pack()

label_result = Label(container4, text="Results :")
label_result.pack(side=TOP)
scroll=Scrollbar(container4,orient=VERTICAL)
scroll.pack(side=RIGHT,fill=Y)

#label_temp = Label(container4, text="...................")
#label_temp.grid(row=2, column=1, padx=10, pady=15)
label_temp = Label(container4, text=" ")
label_temp.pack(side=LEFT)
label_temp = Label(container4, text=" ")
label_temp.pack(side=LEFT)

mylist = Listbox(container4, yscrollcommand=scroll.set)

results_list=[]

show_root.withdraw()

chosen_path=StringVar()
chosen_word=StringVar()

no_of_files=0
percentage = 0

flag=0


def take_path():
    global entry_path
    global chosen_path

    chosen_path.set(entry_path.get())
    print(chosen_path.get())

def loading():
    global no_of_files
    global loading_root
    global container2
    global main_root
    global percentage
    global progress
    global label_done
    global root
    global chosen_path


    #bar()
    #progress = Progressbar(container2, orient=HORIZONTAL,length=100, mode='determinate')
    #btn_ok = Button(container2, text="    OK    ", command=bar)
    #btn_ok.grid(row=3, column=1, pady=15)

    loading_root.update()
    loading_root.deiconify()

    btn_ok_load = Button(container2, text="    OK    ",relief="sunken")
    btn_ok_load.grid(row=3, column=1, pady=15)

    root = Parse(chosen_path.get(),progress,loading_root,percentage)

    #while percentage <= 100:
    #percentage=calculate_perc()
    #progress['value'] = percentage
    #loading_root.update_idletasks()
    #percentage+=1 # httzbt lma el function bta3tha t5ls
        #time.sleep(1)
        # print(percentage)
    #progress.grid(row=2, column=1, padx=10, pady=15)
    #label_load.destroy()
    #label_done.grid(row=1, column=1, padx=10, pady=15)

    btn_ok_load = Button(container2, text="    OK    ",relief="raised",command=enter_word)
    btn_ok_load.grid(row=3, column=1, pady=15)


def enter_word():
    global word_root
    global container3
    global loading_root
    global show_root
    global results_list
    global mylist

    mylist.delete(0,'end')
    results_list.clear()
    loading_root.withdraw()

    show_root.withdraw()

    btn_word_ok = Button(container3, text="    OK    ",command=lambda:[take_word(),show()])
    btn_word_ok.grid(row=3, column=1, pady=15)

    word_root.update()
    word_root.deiconify()


def take_word():
    global chosen_word
    global entry_word
    global word_root
    global container3
    global root
    global results_list

    chosen_word.set(entry_word.get())
    print(chosen_word.get())
    results_list=search(root,chosen_word.get())
    entry_word.delete(0,'end')
    word_root.withdraw()

def show():
    global show_root
    global container4
    global results_list
    global scroll
    global mylist
    global flag

    col=1
    r=2

    for line in range(len(results_list)):
        mylist.insert(END,str(results_list[line]))

    mylist.pack(side=RIGHT, fill=BOTH)
    scroll.config(command=mylist.yview)

    if flag==0:
        btn_ok_load = Button(container4, text=" Re-enter a word  ", relief="raised", command=enter_word)
        btn_ok_load.pack(side=BOTTOM)
        flag=1

    show_root.update()
    show_root.deiconify()




def bar():
    global container2
    global progress
    global loading_root
    global percentage
    while percentage <= 10000:
        progress['value'] = percentage /100
        loading_root.update_idletasks()
        percentage+=1 # httzbt lma el function bta3tha t5ls
        # time.sleep(1)
        print(percentage)
        progress.grid(row=2, column=1, padx=10, pady=15)

def quit_root():
    global main_root
    main_root.withdraw()

btn_size_ok = Button(container1, text="    OK    ",command=lambda:[take_path(),loading(),quit_root()])
btn_size_ok.grid(row=3, column=1, pady=15)

main_root.mainloop()


