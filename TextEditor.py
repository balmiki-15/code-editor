from tkinter import *
from tkinter import filedialog, filedialog, font, simpledialog
from tkinter.ttk import Combobox, Notebook

class TextEditor:
    # Creating a class Variable
    current_open_file = ""
    selectedTab = 1
    # defining open_file method
    def open_file(self):
        f = filedialog.askopenfile(initialdir='/', title='Select Files', filetypes=(("text files","*.txt"),("all files","*.*")))
        if f is None:
            return
        self.text_area.delete(1.0,END)
        for line in f:
            self.text_area.insert(END,line)
        self.current_open_file = f.name
        f.close()
    # defining save_as_file method
    def save_as_file(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension="*.txt")
        if f is None:
            return
        text2save = self.text_area.get(1.0,END)
        f.write(text2save)
        self.current_open_file = f.name
        f.close()
    # defining save_file method
    def save_file(self):
        if self.current_open_file =="":
            self.save_as_file()
        else:
            f = open(self.current_open_file, 'w+')
            f.write(self.text_area.get(1.0,END))
            f.close()

    # defining copy_text method
    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
    # defining cut_text method
    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first","sel.last")
    # defining paste_text method
    def paste_text(self):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())
    # defining Undo method
    def undo(self):
        self.text_area.edit_undo()
    # defining Redo method
    def redo(self):
        self.text_area.edit_redo()
    # defining add a new tab method
    def new(self):
        tab_no = str(self.selectedTab + 1)
        self.text_area = Text(self.tabControl, undo=True)
        self.tabControl.add(self.text_area, text='Tab '+tab_no)
        self.tabControl.pack(expand=1, fill="both")
        self.selectedTab = self.selectedTab + 1
    def close_file(self):
        res = simpledialog.askinteger("close Page","Type page no which you want to close")
        self.tabControl.hide(res-1)
    
    # defining method to change font and its size
    def changeFont(self, event):
        my_font = font.Font(family=self.font_variable.get(),size=self.size_variable.get())
        self.text_area.config(font=my_font)
    
    # defining  method

    # Initialising Constructor
    def __init__(self, master):
        # setting the title, geometry of TextPad
        self.master = master
        self.master.title("TextPad")
        self.master.geometry("700x450+420+100")

        # Creating  ToolBar
        self.tool_bar = Label(self.master)
        self.tool_bar.pack(side=TOP, fill=X)
        # Creating the combobox for toolBar
        font_families = list(font.families())
        self.font_variable = StringVar()
        self.fonts = Combobox(self.tool_bar, textvariable=self.font_variable)
        self.fonts['values'] = font_families
        self.fonts.current(font_families.index("Arial"))
        self.fonts.bind("<<ComboboxSelected>>",self.changeFont)
        self.fonts.pack(side=LEFT)
        # Creating size Box
        self.size_variable = IntVar()
        self.size_box = Combobox(self.tool_bar, textvariable=self.size_variable, width=5)
        self.size_box['values'] = list(range(8,96,2))
        self.size_box.current(4)
        self.size_box.bind("<<ComboboxSelected>>",self.changeFont)
        self.size_box.pack(side=LEFT)
        # Create Bold-icon button
        self.boldButton = Button(self.tool_bar, text='B', width=5)
        self.boldButton.pack(side=LEFT)
        # Create Italic-icon button
        self.italicButton = Button(self.tool_bar, text='I', width=5)
        self.italicButton.pack(side=LEFT)
        # Create italic-icon button
        self.underlineButton = Button(self.tool_bar, text='U', width=5)
        self.underlineButton.pack(side=LEFT)

        # Creating the tabControl
        self.tabControl = Notebook(self.master)
        # Creating Text Area
        # self.my_font = font.Font(family=self.font_variable, size=16)
        self.text_area = Text(self.tabControl, undo=True)
        self.tabControl.add(self.text_area, text='Tab 1')
        self.tabControl.pack(expand=1, fill="both")
        # self.text_area.pack(fill=BOTH, expand=1)
        self.text_area.focus_set()
        # Creating Menu Bar
        self.main_menu = Menu(tearoff=False)
        self.master.config(menu=self.main_menu)
        # Creating the File menu 
        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Close", command=self.close_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        # Creating Edit Menu
        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
      
root = Tk()
te = TextEditor(root)
root.title("TextPad")
root.geometry("700x450+420+100")
root.mainloop()

# tabControl = ttk.Notebook(root)
# tab1 = Text(tabControl)
# tab2 = Text(tabControl)
# tabControl.add(tab1, text='Tab 1')
# tabControl.add(tab2, text='Tab 2')
# tabControl.pack(expand=1, fill="both")