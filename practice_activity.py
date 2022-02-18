from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
root = Tk()
root.minsize(650,650)
root.maxsize(650,650)
open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
label_file_name = Label(root, text="File name")
label_file_name.place(relx=0.28,rely=0.03,anchor= CENTER)
input_file_name = Entry(root)
input_file_name.place(relx=0.46,rely=0.03, anchor= CENTER)
my_text= Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor= CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title = " Open Text File",
                                            filetypes = (("Text FIles", "*.text"),))
    print(text_file)
    name = os.path.basenname(text_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END, formated_name)
    root.title(formated_name)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    my_text.insert(END, paragraph)
    text_file.close()
    paragraph = text_file.read
    my_text.insert(END, paragraph)
    text_file.close()

def save():
    input_name = input_file_name.get()
    file = open(input_name+".txt", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_file_name.delte(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Update", "Success")

def closeWinddow():
    root.destroy

open_button=Button(root, image=open_img, text="Clear Input field", command=openFile)
open_button.place(relx=0.5,rely=0.55,anchor=CENTER)

save_button=Button(root, text="Clear Textarea", command=clearTextarea)
save_button.place(relx=0.455,rely=0.7,anchor= CENTER)

exit_button=Button(root, text="Add data to input feild", command=addData)
exit_button.place(relx=0.7,rely=0.7,anchor= CENTER)

root.mainloop()

# def clearInputField():
#     input_file_name.delete(0, END)

# def clearTextarea():
#     my_text.delete(1.0, END)

# def addData():
#     input_file_name.insert(END, "myfile")

