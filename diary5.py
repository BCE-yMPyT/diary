'''
Fully worked program for inserting notes to DIARY (C:\Python31\scripts\DIARY)
with friendly interface.
'''
#============IMPORTING WORK STUFF================================================
from tkinter import *                   # importing all stuff from tkinter
from tkinter import messagebox          # importing messagebox
from tkinter import colorchooser        # importing colorchooser
from tkinter.colorchooser import *      # importing colorchooser stuff

#===========CREATING MAIN WINDOW=================================================
root = Tk()                             # creating main window
root.title("Python Diary")              # window title
root.geometry("800x350+550+300")        # window size and place (right lowest corner)

#===========CREATING CHOISE CELLS=================================================
var0 = IntVar()
Checkbutton(root, text='Не проставлять автодату',
            variable = var0).grid(row=1, sticky = W)
var1 = IntVar()
Checkbutton(root, text='Режим пригорания',
            variable = var1).grid(row=2, sticky = W)
'''
var2 = IntVar()
Checkbutton(root, text='Пока не придумал',
            variable = var1).grid(row=1, column=5)
'''

#============CREATING EVENTS=====================================================
#-----------[creating event for Ok button]---------------------------------------
def left_click(event):                  # event handler
    messagebox.showinfo("Diary Python", 'Note has been added')
                                        # show finish event
#-inserting note to diary--------------------------------------------------------
    new_diary = open('DIARY.txt', 'a')  # open file DIARY.txt for write session
    import datetime                     # importing time module
    now = datetime.datetime.now()
    now_time = now.strftime("%d-%m-%Y %H:%M:%S")
                                        # variable which include now time                                            
    new_note = message_entry.get('1.0', END+'-1c')
                                        # variable which include note for diary
    if var1.get() == 1:
        new_note = new_note.upper()
    if var0.get() == 1:
        c_note = '\n' + '\n' + new_note
    if var0.get() == 0:
        c_note = '\n' + '\n' + now_time + '\n' + new_note
                                        # completed note after client settings
    new_diary.write(c_note)             # write note to diary
    new_diary.close()                   # close diary
#-finish inserting---------------------------------------------------------------
    root.destroy()                      # destroy main window
    root.quit()                         # quit programm
    
#-----------[creating event for DIARY button]------------------------------------
def left_click4(event):
    def deicon_main_win(event):
        root.deiconify()
        read_diary.destroy()
    def search_note(event):
        message=win_for_search.get()
        win_for_all_lines.update()
        win_for_all_lines.focus()
        win_for_all_lines.lastfind = message
            
        if message in win_for_all_lines.get('1.0', 'end-1c'):
            # чувствителен к регистру символов.
            where = win_for_all_lines.search(message, '1.0', END)
            if not where:
                messagebox.showerror('Searching the key', 'Key not found')         
            else:
                if len(message) == 0:
                    messagebox.showerror('Searching the key', 'Key field is empty')
                pastkey = where + '+%dc' % len(message)
                win_for_all_lines.tag_remove(SEL, '1.0', END)
                win_for_all_lines.tag_add(SEL, where, pastkey)
                win_for_all_lines.mark_set(INSERT, pastkey)
                win_for_all_lines.see(where)
                print(len(message))
                print('sucsess!')
                
            read_diary.mainloop()       
    #--------------------------
    root.withdraw()                         # hide main window
    read_diary = Tk()                       # creating main window
    read_diary.title("DIARY")               # window title
    read_diary.geometry("880x630+0+0")
                                            # window size and place (right lowest corner)
    #--------------------------
    win_for_all_lines = Text(read_diary, height=25, width=75, font='arial 14')
    win_for_all_lines.place(relx=.5, rely=.455, anchor='c')
    #--------------------------
    scrollbar = Scrollbar(read_diary)
    scrollbar.pack(side=RIGHT, fill = Y)
    scrollbar['command'] = win_for_all_lines.yview
    win_for_all_lines['yscrollcommand'] = scrollbar.set
    
    #--------creating ENTER WINDOW for note searching----------------
    win_for_search = Entry(read_diary, width=20, bd=15, font='arial 14')
    win_for_search.place(relx=.03, rely=.905, anchor='nw')
    
    #----creating FIND button------------------------------------
    FIND_but = Button(read_diary, text = "FIND", width=7, height=1, bg='aquamarine',
                        fg='black', font = 'arial 14')
                                        # FIND button
    FIND_but.bind('<Button-1>', search_note)
                                        # attach event to FIND button
    FIND_but.place(relx=.38, rely=.92, anchor='n')
                                        # FIND button place
    
    #----------------------------------------------------------------
    read_diary_file=open('DIARY.txt', 'r')  # read the DIARY file
    for i in read_diary_file:
        win_for_all_lines.insert(END, i)
    read_diary_file.close()
    #--------------------------
    OK_but = Button(read_diary, text = "OK", width=6, height=1, bg='aquamarine',
                        fg='black', font = 'arial 14')
                                        # OK button
    OK_but.bind('<Button-1>', deicon_main_win)
                                        # attach event to OK button
    OK_but.place(relx=.5, rely=.92, anchor='n')
                                        # OK button place
    #-------------------------                                   
    read_diary.mainloop()
#-----------[creating event for SETTINGS]----------------------------------------
def left_click2(event):
    def left_click3(event):
        
        settings.destroy()
    #=======CREATING WINDOW WHICH WILL CALL AFTER PUSHING settings BUTTON============
    settings = Tk()                         # creating main window
    settings.title("SETTINGS")              # window title
    settings.geometry("300x280+0+0")        # window size and place (right lowest corner)
    
        # ADDING CHECKBUTTONS (filling settings window)
    #--------------
    button_ctk = Button(settings, text = "Choose text color", width=15, height=1, bg='aquamarine',
                        fg='black', font = 'arial 14')
                                        # Choose text color button
    button_ctk.bind('<Button-1>', choose_text_color)
                                        # attach event to Choose text color button
    button_ctk.place(relx=.5, rely=.2, anchor='c')
    #--------------
    button_cbgk = Button(settings, text = "Choose back-ground color", width=25, height=1, bg='aquamarine',
                        fg='black', font = 'arial 14')
                                        # Choose back-ground color button
    button_cbgk.bind('<Button-1>', choose_bg_color)
                                        # attach event to Choose back-ground color button
    button_cbgk.place(relx=.5, rely=.5, anchor='c')

    #--------------
    button_SAVE = Button(settings, text = "SAVE", width=5, height=1, bg='aquamarine',
                        fg='black', font = 'arial 14')
                                        # SAVE button
    button_SAVE.bind('<Button-1>', left_click3)
                                        # attach event to SAVE button
    button_SAVE.place(relx=.5, rely=.8, anchor='c')
                                        # SAVE button packing
#-----------    
def choose_text_color(event):
    colorchooser.askcolor()
    fg_color = askcolor()
    fg_color = fg_color[1]
    if fg_color != None:
        message_entry.configure(fg=fg_color)
        message_entry.update()
#-----------
def choose_bg_color(event):
    colorchooser.askcolor()
    bg_color = askcolor()
    bg_color = bg_color[1]
    print(bg_color)
    print(type(bg_color))
    if bg_color != None:
        message_entry.configure(bg=bg_color)
        message_entry.update()

#=============ENTERING NOTE FOR DIARY============================================
startfont = 'courier'
startfg = 'black'
startbg = 'white'

message_entry = Text(root, height=10, width=70, wrap=WORD)
message_entry.config(font=startfont, bg=startbg, fg=startfg)
                                        # inputing text settings
message_entry.place(relx=.5, rely=.5, anchor='c')
                                        # inputing text place

#=============CREATING BUTTONS===================================================
#-------------show old notes buttons---------------------------------------------
read_diary_button = Button(root, text = "DIARY", width=8, height=1, bg='aquamarine',
                        fg='black', font = 'arial 14')
                                        # read diary button
read_diary_button.bind('<Button-1>', left_click4)
                                        # attach event to read diary button
read_diary_button.place(relx=.5, rely=.1, anchor='c')
                                        # read diary button place

#-------------finish message button----------------------------------------------
message_button = Button(root, text = "OK", width=6, height=1, bg='aquamarine',
                        fg='black', font = 'arial 14')
                                        # OK button

message_button.bind('<Button-1>', left_click)
                                        # attach event to OK button
message_button.place(relx=.7, rely=.9, anchor='c')
                                        # OK button place
#------------button for SETTINGS-------------------------------------------------
button_2 = Button(root, text = "SETTINGS", width=10, height=1, bg='aquamarine',
                        fg='black', font = 'arial 14')
                                        # SETTINGS button

button_2.bind('<Button-1>', left_click2)
                                        # attach event to SETTINGS button
button_2.place(relx=.3, rely=.9, anchor='c')
                                        # SETTINGS button place                                 

#--------FINISH FOR FULL LOOP----------------------------------------------------

root.mainloop()                         # breaking main loop
