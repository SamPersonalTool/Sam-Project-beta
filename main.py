#Libraries
import customtkinter as ctk
from PIL import Image
import mod_urlcheck, mod_filecheck
import webbrowser as wb

#Main App
class MainApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ###Window general settings:
        self._set_appearance_mode("dark")
        self.title("SAM: Your personal anti-malware system")
        self.iconbitmap("assets/app-icon.ico")
        self.toplevel_window = None
        #Getting screen resolution
        self.width_screen = self.winfo_screenwidth()
        self.height_screen = self.winfo_screenheight()
        #Coordinates calculation
        self.x = (self.width_screen - 400) // 2
        self.y = (self.height_screen - 400) // 2
        #Geometry definition
        self.geometry(f"400x400+{self.x}+{self.y}")
        self.resizable(False,False)
        #Background
        self.bg_image = ctk.CTkImage(dark_image=Image.open("assets/background.png"), size=(400,400))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        ###Window widgets:
        #Button for about us page
        self.btn = ctk.CTkButton(master=self, text="About Us", command=self.open_about_us)
        self.btn.configure(bg_color="black", fg_color="black", corner_radius=0, height=40, width=100)
        self.btn.configure(font=ctk.CTkFont(family="Roboto", size=12, weight="bold"))
        self.btn.place(relx=0, rely=0)
        #Button for URL checker
        self.btn1 = ctk.CTkButton(master=self, text="Link Checker", command=self.open_linkchecker)
        self.btn1.configure(corner_radius=10, bg_color="black", fg_color="black")
        self.btn1.configure(font=ctk.CTkFont(family="Roboto", size=12, weight="bold"))
        self.btn1.place(relx=0.5, rely=0.405, anchor="center")
        #Button for File checker
        self.btn2 = ctk.CTkButton(master=self, text="File Checker", command=self.open_filechecker)
        self.btn2.configure(corner_radius=10, bg_color="black", fg_color="black")
        self.btn2.configure(font=ctk.CTkFont(family="Roboto", size=12, weight="bold"))
        self.btn2.place(relx=0.5, rely=0.535, anchor="center")
        #Button for Exit
        self.btn3 = ctk.CTkButton(master=self, text="Exit", command=self.destroy)
        self.btn3.configure(bg_color="black", fg_color="black", corner_radius=10, border_width=2, border_color="white")
        self.btn3.configure(font=ctk.CTkFont(family="Roboto", size=12, weight="bold"))
        self.btn3.place(relx=0.5, rely=0.66, anchor="center")

    #Methods:
    def open_linkchecker(self):
        self.toplevel_window = LinkChecker(self)
        app.withdraw()
    def open_filechecker(self):
        self.toplevel_window = FileChecker(self)
        app.withdraw()
    def open_about_us(self):
        wb.open_new_tab("ContactUs.pdf")

#View for link checker tool
class LinkChecker(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ###Window general settings:
        self.title("SAM: LinkChecker Tool")
        self.after(200, lambda: self.iconbitmap("assets/app-icon.ico"))
        self.protocol("WM_DELETE_WINDOW", self.destroy_toplevelwindow)
        #Getting screen resolution and window size
        self.width_screen = self.winfo_screenwidth()
        self.height_screen = self.winfo_screenheight()
        self.width_window = 600
        self.height_window = 600
        #Coordinates calculation
        self.x = (self.width_screen - self.width_window) // 2
        self.y = (self.height_screen - self.height_window) // 2
        #Geometry definition
        self.geometry(f"{self.width_window}x{self.height_window}+{self.x}+{self.y}")
        self.resizable(False,False)
        #Background
        self.bg_image = ctk.CTkImage(dark_image=Image.open("assets/bg_toplevelwindow.png"), size=(600,600))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        ###Window widgets:
        #Entry
        self.entry_link = ctk.CTkEntry(master=self, placeholder_text="Copy your link here!", placeholder_text_color="white")
        self.entry_link.configure(corner_radius=10, bg_color="black", fg_color="black", text_color="white", width=400, height=30)
        self.entry_link.place(relx=0.5, rely=0.168, anchor="center")
        #Button for analyze
        self.btn2 = ctk.CTkButton(master=self, text="Go", command=self.send_link)
        self.btn2.configure(corner_radius=10, bg_color="black", fg_color="black", width=35, border_width=2, border_color="white")
        self.btn2.configure(font=ctk.CTkFont(family="Roboto", size=12, weight="bold"))
        self.btn2.place(relx=0.5, rely=0.265, anchor="center")
        #Button for Exit
        self.mb_icon = ctk.CTkImage(dark_image=Image.open("assets/back.png"), size=(30,30))
        self.btn3 = ctk.CTkButton(master=self, image=self.mb_icon, text="", command=self.destroy_toplevelwindow)
        self.btn3.configure(bg_color="black", fg_color="black", width=20, height=20)
        self.btn3.place(relx=0.92, rely=0)
        #Button for clean
        self.btn4 = ctk.CTkButton(master=self, text="Clean", command=self.clean_window)
        self.btn4.configure(corner_radius=10, bg_color="black", fg_color="black", width=35, border_width=2, border_color="white")
        self.btn4.configure(font=ctk.CTkFont(family="Roboto", size=12, weight="bold"))
        self.btn4.place(relx=0.8, rely=0.265, anchor="center")
        #Label for result
        self.result_label = ctk.CTkLabel(master=self, text="")
        self.result_label.configure(fg_color="black", bg_color="black")
        self.result_label.place(relx=0.5, rely=0.6, anchor="center")
    #Methods
    def send_link(self):
        self.my_link = self.entry_link.get()
        self.rest = mod_urlcheck.URLcm.analyze_url(self.my_link)
        self.result_label.configure(text=self.rest, padx=2, pady=2, corner_radius=10, text_color="white")
        self.result_label.configure(font=ctk.CTkFont(family="Roboto", size=12, weight="bold"))
        return self.rest
    def clean_window(self):
        self.entry_link.delete(0, ctk.END)
        self.result_label.configure(text="")
    def destroy_toplevelwindow(self):
        self.destroy()
        app.deiconify()

#View for file checker tool
class FileChecker(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ###Window general settings:
        self.title("SAM: FileChecker Tool")
        self.after(200, lambda: self.iconbitmap("assets/app-icon.ico"))
        self.protocol("WM_DELETE_WINDOW", self.destroy_toplevelwindow)
        #Getting screen resolution and window size
        self.width_screen = self.winfo_screenwidth()
        self.height_screen = self.winfo_screenheight()
        self.width_window = 600
        self.height_window = 600
        #Coordinates calculation
        self.x = (self.width_screen - self.width_window) // 2
        self.y = (self.height_screen - self.height_window) // 2
        #Geometry definition
        self.geometry(f"{self.width_window}x{self.height_window}+{self.x}+{self.y}")
        self.resizable(False,False)
        #Background
        self.bg_image = ctk.CTkImage(dark_image=Image.open("assets/bg_toplevelwindow2.png"), size=(600,600))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        ###Window widgets:
        #Entry
        self.entry_path = ctk.CTkEntry(master=self, placeholder_text="Path of your file!", placeholder_text_color="white")
        self.entry_path.configure(corner_radius=10, bg_color="black", fg_color="black", text_color="white", width=350, height=30)
        self.entry_path.place(relx=0.45, rely=0.168, anchor="center")
        #Button for search file & analyze
        self.upload_icon = ctk.CTkImage(dark_image=Image.open("assets/upload.png"), size=(30,30))
        self.btn = ctk.CTkButton(master=self, image=self.upload_icon, text="", command=self.open_send_file)
        self.btn.configure(bg_color="black", fg_color="black", width=20, height=20)
        self.btn.place(relx=0.79, rely=0.168, anchor="center")
        #Button for Exit
        self.mb_icon = ctk.CTkImage(dark_image=Image.open("assets/back.png"), size=(30,30))
        self.btn2 = ctk.CTkButton(master=self, image=self.mb_icon, text="", command=self.destroy_toplevelwindow)
        self.btn2.configure(bg_color="black", fg_color="black", width=20, height=20)
        self.btn2.place(relx=0.92, rely=0)
        #Button for clean
        self.btn3 = ctk.CTkButton(master=self, text="Clean", command=self.clean_window)
        self.btn3.configure(corner_radius=10, bg_color="black", fg_color="black", width=35, border_width=2, border_color="white")
        self.btn3.configure(font=ctk.CTkFont(family="Roboto", size=12, weight="bold"))
        self.btn3.place(relx=0.8, rely=0.265, anchor="center")
        #Label for result
        self.result_label = ctk.CTkLabel(master=self, text="")
        self.result_label.configure(fg_color="black")
        self.result_label.place(relx=0.5, rely=0.5, anchor="center")
    #Methods:
    def open_send_file(self):
        self.file_path = ctk.filedialog.askopenfilename()
        self.entry_path.configure(textvariable=f"{self.file_path}")
        self.entry_path.configure(placeholder_text=self.file_path)
        self.rest = mod_filecheck.FILEcm.validate_file(self.entry_path._textvariable)
        self.result_label.configure(text=self.rest, padx=5, pady=5, corner_radius=0, text_color="white")
        self.result_label.configure(font=ctk.CTkFont(family="Roboto", size=12, weight="bold"))
        return self.rest
    def clean_window(self):
        self.entry_path.delete(0, ctk.END)
        self.result_label.configure(text="")
    def destroy_toplevelwindow(self):
        self.destroy()
        app.deiconify()

app = MainApp()
app.mainloop()