#!/usr/bin/python3

class Plotter:
    def __init__(self,canvas,width,height):
        self.w = canvas
        self.x = width
        self.y = height
        self.makeGrid()
        
    def makeCross(self,x,y):
        self.w.create_line(x-5,y-5,x+5,y+6)
        self.w.create_line(x+5,y-6,x-5,y+5)
        
    def makeGrid(self):
        # X-/Y-Axis
        self.w.create_line(0,self.x/2,self.y,self.y/2) #X
        self.w.create_line(self.x/2,0,self.y/2,self.y) #Y
    
        # Axis labels
        self.w.create_text((self.x/2)+10,20,text="Y",fill="purple")
        self.w.create_text(self.x-10,(self.y/2)+20,text="X",fill="purple")
    
        # Axis strikes and labels
        i = 50
        label = 0
        labely = self.y-50 # reverse i
        labels=("-4","-3","-2","-1","1","2","3","4")
        while (i<=self.x-50):
            if i != self.x/2:
                # Grid
                self.w.create_line(0,i,self.x,i,fill="gray")
                self.w.create_line(i,0,i,self.y,fill="gray")
            
                # Labels
                self.w.create_text(i,(self.y/2)+10,text=labels[label]) #X
                self.w.create_text((self.x/2)-10,labely,text=labels[label]) #Y
            
            else:
                label=label-1
        
            self.w.create_line(i,(self.y/2)-5,i,(self.y/2)+5) #X
            self.w.create_line((self.x/2)-5,i,(self.x/2)+5,i) #Y
                        
        
            label=label+1
            i=i+50
            labely=labely-50
