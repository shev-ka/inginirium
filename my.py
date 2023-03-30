####################################################################### tkinter

#from tkinter import *
#def function1():
#    label.config(text = int(entry.get())*2)
#root = Tk()
#root.title('Приложение')
#root.geometry('500x300')
#label = Label(root, text = 'Надпись', font = 'consolas', background = 'cyan')
#entry = Entry(root, text = 'Строка ввода', bg = 'green', foreground = 'red')
#button = Button(root, text = 'Кнопка', bg = 'orange', fg = 'red', width = 10, 
#                activebackground = 'red', height = 5, command = function1)
#label.pack()
#entry.pack()
#button.pack()
#root.mainloop()

####################################################################### Canvas

#from tkinter import *
#i = 0
#k = 0
#def function1():
#    global k
#    if k%2 == 0:
#        canvas.config(bg = 'black')
#    else:
#        canvas.config(bg = 'purple')
#    k+=1 # k = k + 1

#def function2():
#    global i
#    if i%2 == 0:
#        canvas.itemconfig(polygon, fill = 'grey')
#    else:
#        canvas.itemconfig(polygon, fill = 'blue')
#    i+=1 

#root = Tk()
#root.title('Canvas')
#root.geometry('1200x800')
#canvas = Canvas(root, width = 800, height = 700, bg = 'purple')
#canvas.create_line(10, 15, 100, 450, fill = 'green', width = '6')
#canvas.create_oval(110, 60, 470, 220, fill = 'yellow', width = '8', 
#                   outline = 'pink', dash = 5)
#canvas.create_rectangle(80, 400, 450, 600, fill = 'red', width = '5', 
#                   outline = 'brown', activefill = 'white', activeoutline = 'orange')
#polygon = canvas.create_polygon(500, 380, 590, 440, 670, 410, 720, 220, 550, 600, 
#                                fill = 'blue', width = '6', outline = 'cyan')
#button1 = Button(root, text = 'Кнопка 1', bg = 'cyan', fg = 'red', width = 10, 
#                activebackground = 'red', height = 5, command = function1)
#button2 = Button(root, text = 'Кнопка 2', bg = 'blue', fg = 'red', width = 10, 
#                activebackground = 'red', height = 5, command = function2)
#button1.pack(side = RIGHT)
#button2.pack(side = RIGHT)
#canvas.pack()
#root.mainloop()

####################################################################### messagebox

#from tkinter import *
#from tkinter import messagebox
#def function1():
#    if int(entry.get())<1000:
#        messagebox.showerror('ошибка', 'всё плохо')
#    elif int(entry.get())<2000:
#        messagebox.showwarning('предупреждение', 'требуется ремонт')
#    else:
#        messagebox.showinfo('результат', int(entry.get()))
#root = Tk()
#root.title('Приложение')
#root.geometry('500x300')
#entry = Entry(root, text = 'Строка ввода', bg = 'green', foreground = 'red')
#button = Button(root, text = 'Кнопка', bg = 'orange', fg = 'red', width = 10, 
#                activebackground = 'red', height = 5, command = function1)
#entry.pack()
#button.pack()
#root.mainloop()

####################################################################### простой калькулятор

#from tkinter import *
#from tkinter import messagebox
#def function1():
#    messagebox.showinfo('результат', int(entry1.get())+int(entry2.get()))
#def function2():
#    messagebox.showinfo('результат', int(entry1.get())-int(entry2.get()))
#def function3():
#    messagebox.showinfo('результат', int(entry1.get())*int(entry2.get()))
#def function4():
#    messagebox.showinfo('результат', int(entry1.get())/int(entry2.get()))
#def function5():
#    messagebox.showinfo('результат', int(entry1.get())%int(entry2.get()))
#def function6():
#    messagebox.showinfo('результат', int(entry1.get())//int(entry2.get()))
#root = Tk()
#root.title('Приложение')
#root.geometry('500x300')
#entry1 = Entry(root, text = 'Строка ввода 1', foreground = 'red')
#entry2 = Entry(root, text = 'Строка ввода 2', foreground = 'red')
#button1 = Button(root, text = '+', bg = 'orange', fg = 'red', width = 10, 
#                activebackground = 'red', command = function1)
#button2 = Button(root, text = '-', bg = 'orange', fg = 'red', width = 10, 
#                activebackground = 'red', command = function2)
#button3 = Button(root, text = '*', bg = 'orange', fg = 'red', width = 10, 
#                activebackground = 'red', command = function3)
#button4 = Button(root, text = '/', bg = 'orange', fg = 'red', width = 10, 
#                activebackground = 'red', command = function4)
#button5 = Button(root, text = '%', bg = 'orange', fg = 'red', width = 10, 
#                activebackground = 'red', command = function5)
#button6 = Button(root, text = '//', bg = 'orange', fg = 'red', width = 10, 
#                activebackground = 'red', command = function6)
#entry1.pack()
#entry2.pack()
#button1.pack()
#button2.pack()
#button3.pack()
#button4.pack()
#button5.pack()
#button6.pack()
#root.mainloop()

####################################################################### игра

#from tkinter import *
#import random
#score, max_score = 0, 20
#size_x, size_y = 1200, 700
#def put():
#    global button
#    button = Button(root, text = 'Нажми меня', bg = 'cyan', fg = 'red', width = 10, 
#                activebackground = 'red', font = ('consolas', 25), command = click)
#    button.place(x = random.randint(100, size_x-100), y = random.randint(60, size_y-60))
#def click():
#    global score
#    score += 1
#    button.destroy()
#    if score >= max_score:
#        Label(text = 'Поздравляю,\nвы выиграли!', 
#              font = ('consolas', 35)).place(relx = 0.5, rely = 0.5, anchor = CENTER)
#    else:
#        put()
#root = Tk()
#root.title('Приложение')
##root.geometry(f'{size_x}x{size_y}')
#root.geometry('{}x{}'.format(size_x, size_y))
#root.resizable(False, False)
#put()
#root.mainloop()

####################################################################### сложный калькулятор

#from tkinter import *
#from tkinter import messagebox
#list = ['C', 'DEL', '*', '=', '1', '2', '3', '/', '4', '5', '6', '+', 
#        '7', '8', '9', '-', '(', '0', ')', 'X^2']
#def logic(symbol):
#    if symbol == "C":
#        label['text'] = '0'
#    elif symbol == "DEL":
#        label['text'] = label['text'][0:-1]
#        if label['text'] == '':
#            label['text'] = '0'
#    elif symbol == 'X^2':
#        label['text'] = str(eval(label['text'])**2)
#    elif symbol == '=':
#        if label['text'][-2] == '/' and label['text'][-1] == '0':
#            messagebox.showwarning('warning', 'division by zero')
#        else:
#            label['text'] = str(eval(label['text']))
#    else:
#        if label['text'] == '0':
#            label['text'] = ''
#        label['text'] += symbol
#root = Tk()
#root['bg'] = 'black'
#root.title('Сложный калькулятор')
#root.geometry('500x550')
#root.resizable(False, False)
#label = Label(text = '0', font = ('consolas', 21, 'bold'), bg = 'black', fg = 'white')
#label.place(x=10,y=50)
#x, y = 10, 120
#for lis in list:
#    com = lambda x=lis: logic(x)
#    Button(text = lis, bg = 'white', fg = 'black', 
#           font = ('consolas', 16), command = com).place(x=x, y=y, width = 115, height = 80)
#    x+=120
#    if x>400:
#        x = 10
#        y += 85
#root.mainloop()

####################################################################### csv

filename = 'c:/123/data.csv'

def read_from_file(filename):
    with open(filename, 'r') as file:
        columns = tuple(file.readline().split(';'))
        data = []
        for line in file:
            line = line.split(';')
            data.append((int(line[0]),line[1],line[2],int(line[3]),int(line[4]),int(line[5])))
    return columns, data

def print_data():
    m = max([len(i) for i in columns])
    for i in columns:
        print(str(i).ljust(m+1, " "), end = '')
    print()
    for line in data:
        for i in line:
            print(str(i).ljust(m+1, " "), end = '')
        print()
def write_to_file(filename):
    with open(filename, 'w') as file:
        file.write(';'.join(columns))
        for line in data:
            line = [str(i) for i in line]
            file.write(';'.join(line)+'\n')

def get_data():
    line = list(input().split())
    return (int(line[0]),line[1],line[2],int(line[3]),int(line[4]),int(line[5]))

def insert(line):
    if line not in data:
        data.append(line)

global columns, data
columns, data = read_from_file(filename)
print_data()
insert(get_data())
print_data()
write_to_file(filename)

#######################################################################


