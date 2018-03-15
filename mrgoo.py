#!/usr/bin/env/python
import webbrowser
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def main():
        root = Tk(className="mrgoo")

        label_sn = Label(root, text="here normal search")
        label_sn.pack(side="top")
        normal_search = ttk.Entry(root, width=30)
        normal_search.pack(side="top")
        cb_ns = ttk.Checkbutton(root)
        cb_ns.pack(side="top", fill="none", expand=False, padx=4, pady=4)
        state_ns = StringVar()
        state_ns.set("off")
        cb_ns.config(variable=state_ns, onvalue="on", offvalue="off")
        
        label_coma_sn = Label(root, text="-------------------------------------")
        label_coma_sn.pack(side="top")
        
        label_ft = Label(root, text="here file type")
        label_ft.pack(side="top")
        file_type = ttk.Entry(root, width=30)
        file_type.pack(side="top")
        cb_ft = ttk.Checkbutton(root)
        cb_ft.pack(side="top", fill="none", expand=False, padx=4, pady=4)
        state_ft = StringVar()
        state_ft.set("off")
        cb_ft.config(variable=state_ft, onvalue="on", offvalue="off")
        
        label_coma_ft = Label(root, text="-------------------------------------")
        label_coma_ft.pack(side="top")

        label_in = Label(root, text="here in text")
        label_in.pack(side="top") 
        in_text = ttk.Entry(root, width=30)
        in_text.pack(side="top")
        cb_in = ttk.Checkbutton(root)
        cb_in.pack(side="top", fill="none", expand=False, padx=4, pady=4)
        state_in = StringVar()
        state_in.set("off")
        cb_in.config(variable=state_in, onvalue="on", offvalue="off")
        
        label_coma_in = Label(root, text="-------------------------------------")
        label_coma_in.pack(side="top")

        label_site = Label(root, text="here website")
        label_site.pack(side="top")
        site = ttk.Entry(root, width=30)
        site.pack(side="top")
        cb_site = ttk.Checkbutton(root)
        cb_site.pack(side="top", fill="none", expand=False, padx=4, pady=4)
        state_site = StringVar()
        state_site.set("off")
        cb_site.config(variable=state_site, onvalue="on", offvalue="off")
        
        label_coma_site = Label(root, text="-------------------------------------")
        label_coma_site.pack(side="top")
        
        label_inurl = Label(root, text="here in url")
        label_inurl.pack(side="top")
        inurl = ttk.Entry(root, width=30)
        inurl.pack(side="top")
        cb_inurl = ttk.Checkbutton(root)
        cb_inurl.pack(side="top", fill="none", expand=False, padx=4, pady=4)
        state_inurl = StringVar()
        state_inurl.set("off")
        cb_inurl.config(variable=state_inurl, onvalue="on", offvalue="off")
        
        label_coma_inurl = Label(root, text="-------------------------------------")
        label_coma_inurl.pack(side="top")

        label_intitle = Label(root, text="here in title")
        label_intitle.pack(side="top")
        intitle = ttk.Entry(root, width=30)
        intitle.pack(side="top")
        cb_intitle = ttk.Checkbutton(root)
        cb_intitle.pack(side="top", fill="none", expand=False, padx=4, pady=4)
        state_intitle = StringVar()
        state_intitle.set("off")
        cb_intitle.config(variable=state_intitle, onvalue="on", offvalue="off")
        
        but = ttk.Button(root, text="Get search")
        but.pack()

        menu = Menu(root)
        root.config(menu=menu)
        
        MainMenu = Menu(menu)
        menu.add_cascade(label="Main", menu=MainMenu)
        
        ModMenu = Menu(menu)
        menu.add_cascade(label="Mods", menu=ModMenu)

        
        def search():
                google_url = ("https://www.google.co.il/search?q=")
                webbrowser.open(google_url + str(text_search))

        def on_off():
                global text_search
                if state_ns.get() == "on":
                        text_search = ('{}'.format(normal_search.get()))
                elif state_ns.get() == "off":
                        text_search = ("")
                if state_ft.get() == "on":
                        text_search += (' filetype:{}'.format(file_type.get()))
                if state_in.get() == "on": 
                        text_search += (' intext:{}'.format(in_text.get()))
                if state_site.get() == "on":
                        text_search += (' site:{}'.format(site.get()))
                if state_inurl.get() == "on":
                        text_search += (" inurl:{}".format(inurl.get()))
                if state_intitle.get() == "on":
                        text_search += (' intitle:{}'.format(intitle.get()))
                search()
        def Abut():
               tkinter.messagebox.showinfo(title="Abut", message="coded by mosa salman\ninstagram @laser01\ngithub @laser010")
        def SqlInjection():
            inurl.delete(0,END)
            inurl.insert(0,".php?*=")
            state_inurl.set("on")

            normal_search.delete(0,END)
            normal_search.insert(0,"-mysql.com")
            state_ns.set("on")

            in_text.delete(0,END)
            in_text.insert(0,"(You have an error in your SQL syntax)")
            state_in.set("on")

            file_type.delete(0,END)
            file_type.insert(0,"php")
            state_ft.set("on")

            intitle.delete(0,END)
            intitle.insert(0,"")
            state_intitle.set("off")
            
            site.delete(0,END)
            site.insert(0,"")
            state_site.set("off")
            return
        
        def DatabasePassword():
            inurl.delete(0,END)
            inurl.insert(0,"config/parameters.yml")
            state_inurl.set("on")

            normal_search.delete(0,END)
            normal_search.insert(0,"-github.com")
            state_ns.set("on")

            file_type.delete(0,END)
            file_type.insert(0,"yml")
            state_ft.set("on")

            in_text.delete(0,END)
            in_text.insert(0,"database_password")
            state_in.set("on")

            intitle.delete(0,END)
            intitle.insert(0,"")
            state_intitle.set("off")
            
            site.delete(0,END)
            site.insert(0,"")
            state_site.set("off")
            return

        def SysInfoTools():
            file_type.delete(0,END)
            file_type.insert(0,"txt")
            state_ft.set("on")

            in_text.delete(0,END)
            in_text.insert(0,"(random's system information tool)")
            state_in.set("on")

            intitle.delete(0,END)
            intitle.insert(0,"")
            state_intitle.set("off")
            
            site.delete(0,END)
            site.insert(0,"")
            state_site.set("off")
            
            normal_search.delete(0,END)
            normal_search.insert(0,"")
            state_ns.set("off")

            inurl.delete(0,END)
            inurl.insert(0,"")
            state_inurl.set("off")
            return
                

        but.config(command=lambda: on_off())
        ModMenu.add_command(label="sql injection", command=lambda: SqlInjection())
        ModMenu.add_command(label="Database password", command=lambda: DatabasePassword())
        ModMenu.add_command(label="Sys info tools", command=lambda: SysInfoTools())
        MainMenu.add_command(label="Abut", command=lambda: Abut())
        root.geometry("200x555+250+250")
        root.mainloop()


if __name__ == "__main__":
        main()
