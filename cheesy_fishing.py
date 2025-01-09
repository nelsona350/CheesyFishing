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
        
        self.bg = PhotoImage(file="images/pond1.png",master=root)
        
        self.carp = Image.open("images/carp2.jfif").resize((400, 400))
        self.bass = Image.open("images/bass1.jfif").resize((400, 400))
        self.bluegill = Image.open("images/bluegill.png").resize((400, 400))
        self.catfish = Image.open("images/catfish.jfif").resize((400, 400))
        self.mosa = Image.open("images/mosa.jpg").resize((400, 400))
        
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
        
        self.radius = 20
        
        with open("resources/records.txt", "r") as infile:
            try:
                fish,weight,angler = infile.readline().strip().split(',')
                self.carpRecord = [fish,weight,angler]
                fish,weight,angler = infile.readline().strip().split(',')
                self.bassRecord = [fish,weight,angler]
                fish,weight,angler = infile.readline().strip().split(',')
                self.bluegillRecord = [fish,weight,angler]
                fish,weight,angler = infile.readline().strip().split(',')
                self.catfishRecord = [fish,weight,angler]
                fish,weight,angler = infile.readline().strip().split(',')
                self.mosaRecord = [fish,weight,angler]
            except:
                weight = "0.0"
                angler = "Mr. Fisher"
                self.carpRecord = ["Carp",weight,angler]
                self.bassRecord = ["Bass",weight,angler]
                self.bluegillRecord = ["Bluegill",weight,angler]
                self.catfishRecord = ["Catfish",weight,angler]
                self.mosaRecord = ["Mosasaurus",weight,angler]
                
            
        self.button2 = Button(root, text="View Records", command=self.viewRecords)
        self.button2.place(x=10, y=10)
        
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
                
    def viewRecords(self):
        self.recordsWindow = tk.Toplevel(root)
        self.recordsWindow.wm_title("Catch")
        self.recordsWindow.grab_set()
        
        labels = []
        labels.append(Label(self.recordsWindow, text="Species"))
        labels[-1].grid(row=0, column=0)
        labels.append(Label(self.recordsWindow, text="Weight"))
        labels[-1].grid(row=0, column=1)
        labels.append(Label(self.recordsWindow, text="Angler"))
        labels[-1].grid(row=0, column=2)
        
        labels.append(Label(self.recordsWindow, text=self.carpRecord[0]))
        labels[-1].grid(row=1, column=0)
        labels.append(Label(self.recordsWindow, text=self.carpRecord[1]))
        labels[-1].grid(row=1, column=1)
        labels.append(Label(self.recordsWindow, text=self.carpRecord[2]))
        labels[-1].grid(row=1, column=2)
                
        labels.append(Label(self.recordsWindow, text=self.bassRecord[0]))
        labels[-1].grid(row=2, column=0)
        labels.append(Label(self.recordsWindow, text=self.bassRecord[1]))
        labels[-1].grid(row=2, column=1)
        labels.append(Label(self.recordsWindow, text=self.bassRecord[2]))
        labels[-1].grid(row=2, column=2)
                
        labels.append(Label(self.recordsWindow, text=self.bluegillRecord[0]))
        labels[-1].grid(row=3, column=0)
        labels.append(Label(self.recordsWindow, text=self.bluegillRecord[1]))
        labels[-1].grid(row=3, column=1)
        labels.append(Label(self.recordsWindow, text=self.bluegillRecord[2]))
        labels[-1].grid(row=3, column=2)
                
        labels.append(Label(self.recordsWindow, text=self.catfishRecord[0]))
        labels[-1].grid(row=4, column=0)
        labels.append(Label(self.recordsWindow, text=self.catfishRecord[1]))
        labels[-1].grid(row=4, column=1)
        labels.append(Label(self.recordsWindow, text=self.catfishRecord[2]))
        labels[-1].grid(row=4, column=2)
                
        labels.append(Label(self.recordsWindow, text=self.mosaRecord[0]))
        labels[-1].grid(row=5, column=0)
        labels.append(Label(self.recordsWindow, text=self.mosaRecord[1]))
        labels[-1].grid(row=5, column=1)
        labels.append(Label(self.recordsWindow, text=self.mosaRecord[2]))
        labels[-1].grid(row=5, column=2)
                


    def caughtcarp(self):
        self.fishWindow = tk.Toplevel(root)
        self.fishWindow.wm_title("Catch")
        self.fishWindow.grab_set()
        weight = np.round(18*np.random.lognormal(mean=0.0, sigma=0.5, size=None))
        label1 = Label(self.fishWindow, text="You caught a " + str(weight) + " pound carp!")
        label1.grid(row=0, column=0)
        label2 = Label(self.fishWindow, image=self.carp1)
        label2.grid(row=1, column=0)
        if weight > float(self.carpRecord[1]):
            self.carpRecord[1] = str(weight)
            with open("resources/records.txt", "w") as outfile:
                outfile.write(",".join(self.carpRecord)+"\n")
                outfile.write(",".join(self.bassRecord)+"\n")
                outfile.write(",".join(self.bluegillRecord)+"\n")
                outfile.write(",".join(self.catfishRecord)+"\n")
                outfile.write(",".join(self.mosaRecord)+"\n")
            
        
    def caughtbass(self):
        self.fishWindow = tk.Toplevel(root)
        self.fishWindow.wm_title("Catch")
        self.fishWindow.grab_set()
        weight = np.round(10*np.random.lognormal(mean=0.0, sigma=0.3, size=None))
        label1 = Label(self.fishWindow, text="You caught a " + str(weight) + " pound bass!")
        label1.grid(row=0, column=0)
        label2 = Label(self.fishWindow, image=self.bass1)
        label2.grid(row=1, column=0)        
        if weight > float(self.bassRecord[1]):
            self.bassRecord[1] = str(weight)
            with open("resources/records.txt", "w") as outfile:
                outfile.write(",".join(self.carpRecord)+"\n")
                outfile.write(",".join(self.bassRecord)+"\n")
                outfile.write(",".join(self.bluegillRecord)+"\n")
                outfile.write(",".join(self.catfishRecord)+"\n")
                outfile.write(",".join(self.mosaRecord)+"\n")

        
    def caughtbluegill(self):
        self.fishWindow = tk.Toplevel(root)
        self.fishWindow.wm_title("Catch")
        self.fishWindow.grab_set()
        weight = np.round(2*np.random.lognormal(mean=0.0, sigma=0.3, size=None))
        label1 = Label(self.fishWindow, text="You caught a " + str(weight) + " pound bluegill!")
        label1.grid(row=0, column=0)
        label2 = Label(self.fishWindow, image=self.bluegill1)
        label2.grid(row=1, column=0)
        if weight > float(self.bluegillRecord[1]):
            self.bluegillRecord[1] = str(weight)
            with open("resources/records.txt", "w") as outfile:
                outfile.write(",".join(self.carpRecord)+"\n")
                outfile.write(",".join(self.bassRecord)+"\n")
                outfile.write(",".join(self.bluegillRecord)+"\n")
                outfile.write(",".join(self.catfishRecord)+"\n")
                outfile.write(",".join(self.mosaRecord)+"\n")
                
    def caughtcatfish(self):
        self.fishWindow = tk.Toplevel(root)
        self.fishWindow.wm_title("Catch")
        self.fishWindow.grab_set()
        weight = np.round(20*np.random.lognormal(mean=0.0, sigma=0.65, size=None))
        label1 = Label(self.fishWindow, text="You caught a " + str(weight) + " pound catfish!")
        label1.grid(row=0, column=0)
        label2 = Label(self.fishWindow, image=self.catfish1)
        label2.grid(row=1, column=0)
        if weight > float(self.catfishRecord[1]):
            self.catfishRecord[1] = str(weight)
            with open("resources/records.txt", "w") as outfile:
                outfile.write(",".join(self.carpRecord)+"\n")
                outfile.write(",".join(self.bassRecord)+"\n")
                outfile.write(",".join(self.bluegillRecord)+"\n")
                outfile.write(",".join(self.catfishRecord)+"\n")
                outfile.write(",".join(self.mosaRecord)+"\n")
                
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
        if weight > float(self.mosaRecord[1]):
            self.mosaRecord[1] = str(weight)
            with open("resources/records.txt", "w") as outfile:
                outfile.write(",".join(self.carpRecord)+"\n")
                outfile.write(",".join(self.bassRecord)+"\n")
                outfile.write(",".join(self.bluegillRecord)+"\n")
                outfile.write(",".join(self.catfishRecord)+"\n")
                outfile.write(",".join(self.mosaRecord)+"\n")
                
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()