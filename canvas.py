import Tkinter
import tkMessageBox


class DemoApp(object):
    
    def __init__(self):
        self.top = Tkinter.Tk()
        self.C = Tkinter.Canvas(self.top, bg="blue", height=250, width=300)
        self.coord = 50, 50, 60, 60
        self.arc = self.C.create_line(self.coord, fill="red")
        self.top.bind("<Key>", self.key)
        self.C.pack()

    def key(self, event):
        print "pressed", repr(event.char)
        if event.char == 'w':
            newcoord = self.coord[0], self.coord[1] - 5, self.coord[2], self.coord[3] - 5
        elif event.char == 's':
            newcoord = self.coord[0], self.coord[1] + 5, self.coord[2], self.coord[3] + 5
        elif event.char == 'a':
            newcoord = self.coord[0] - 5 , self.coord[1], self.coord[2] - 5, self.coord[3]
        elif event.char == 'd':
            newcoord = self.coord[0] + 5, self.coord[1], self.coord[2] + 5, self.coord[3]
        else:
            return
        self.C.coords(self.arc, newcoord)
        self.coord = newcoord

    def scheduled_task(self):
        


# def callback(event):
#     frame.focus_set()
#     print "clicked at", event.x, event.y

# frame = Tkinter.Frame(top, width=100, height=100)
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.pack()
ap = DemoApp()
ap.top.mainloop()
