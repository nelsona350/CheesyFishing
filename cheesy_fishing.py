from tkinter import ttk, Label, PhotoImage, Button
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import numpy as np

class App:
    def __init__(self, root):

        root.title("CHEESY FISHING")
        width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d" % (width, height))
        root.state('zoomed')
        
        self.bg = PhotoImage(file="pond1.png",master=root)
        
        self.carp = Image.open("carp2.jfif").resize((400, 400))
        self.bass = Image.open("bass1.jfif").resize((400, 400))
        self.bluegill = Image.open("bluegill.png").resize((400, 400))
        self.catfish = Image.open("catfish.jfif").resize((400, 400))
        self.mosa = Image.open("mosa.jpg").resize((400, 400))
        
        self.carp1 = ImageTk.PhotoImage(self.carp)
        self.bass1 = ImageTk.PhotoImage(self.bass)
        self.bluegill1 = ImageTk.PhotoImage(self.bluegill)
        self.catfish1 = ImageTk.PhotoImage(self.catfish)
        self.mosa1 = ImageTk.PhotoImage(self.mosa)
        
        self.label1 = Label(root, image=self.bg)
        self.label1.place(x=0, y=0)
        self.label1.bind('<Button-1>', self.onClick)
        
        self.pointList = [(270,270,"mystery"),(1050,410,"mystery"),
                          (465,250,"carp"),(650,165,"carp"),
                          (815,140,"carp"),(900,470,"carp"),
                          (535,420,"cat"),(730,460,"cat"),
                          (460,585,"blue"),(910,615,"blue"),
                          (400,400,"bass"),(880,285,"bass")]
        
        self.radius = 30
        
    def onClick(self, event):
        #print('Clicked canvas at: ', event.x, event.y, event.widget)
        # self.fishWindow = tk.Toplevel(root)
        # self.fishWindow.wm_title("Catch")
        # self.fishWindow.grab_set()
        # label1 = Label(self.fishWindow, text="x " + str(event.x) + " y " + str(event.y))
        # label1.grid(row=0, column=0)
        
        xClick = event.x
        yClick = event.y

        for (x,y,fish) in self.pointList:
        
            distance = np.sqrt((xClick-x)*(xClick-x) + (yClick-y)*(yClick-y))
        
            if distance < self.radius:
                if fish == "mystery":
                    self.caughtmystery()
                elif fish == "carp":
                    self.caughtcarp()
                elif fish == "cat":
                    self.caughtcatfish()
                elif fish == "blue":
                     self.caughtbluegill()
                elif fish == "bass":
                     self.caughtbass()
                     
                break

    def caughtcarp(self):
        self.fishWindow = tk.Toplevel(root)
        self.fishWindow.wm_title("Catch")
        self.fishWindow.grab_set()
        weight = np.round(18*np.random.lognormal(mean=0.0, sigma=0.5, size=None))
        label1 = Label(self.fishWindow, text="You caught a " + str(weight) + " pound carp!")
        label1.grid(row=0, column=0)
        label2 = Label(self.fishWindow, image=self.carp1)
        label2.grid(row=1, column=0)
        
    def caughtbass(self):
        self.fishWindow = tk.Toplevel(root)
        self.fishWindow.wm_title("Catch")
        self.fishWindow.grab_set()
        weight = np.round(10*np.random.lognormal(mean=0.0, sigma=0.3, size=None))
        label1 = Label(self.fishWindow, text="You caught a " + str(weight) + " pound bass!")
        label1.grid(row=0, column=0)
        label2 = Label(self.fishWindow, image=self.bass1)
        label2.grid(row=1, column=0)        

        
    def caughtbluegill(self):
        self.fishWindow = tk.Toplevel(root)
        self.fishWindow.wm_title("Catch")
        self.fishWindow.grab_set()
        weight = np.round(2*np.random.lognormal(mean=0.0, sigma=0.3, size=None))
        label1 = Label(self.fishWindow, text="You caught a " + str(weight) + " pound bluegill!")
        label1.grid(row=0, column=0)
        label2 = Label(self.fishWindow, image=self.bluegill1)
        label2.grid(row=1, column=0)
                
    def caughtcatfish(self):
        self.fishWindow = tk.Toplevel(root)
        self.fishWindow.wm_title("Catch")
        self.fishWindow.grab_set()
        weight = np.round(20*np.random.lognormal(mean=0.0, sigma=0.65, size=None))
        label1 = Label(self.fishWindow, text="You caught a " + str(weight) + " pound catfish!")
        label1.grid(row=0, column=0)
        label2 = Label(self.fishWindow, image=self.catfish1)
        label2.grid(row=1, column=0)
                
    def caughtmystery(self):
        self.fishWindow = tk.Toplevel(root)
        self.fishWindow.wm_title("Catch")
        self.fishWindow.grab_set()
        weight = np.round(20*np.random.lognormal(mean=0.0, sigma=1.0, size=None))
        weight = weight + np.round(np.random.normal(10000.0,3000.0),0)
        label1 = Label(self.fishWindow, text="You caught a " + str(weight) + " pound mosasaurus!")
        #label1 = Label(self.fishWindow, text="You caught nothing!")
        label1.grid(row=0, column=0)
        label2 = Label(self.fishWindow, image=self.mosa1)
        label2.grid(row=1, column=0)
                
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()