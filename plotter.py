#!/usr/bin/python3

class Plotter:
    def __init__(self,canvas,width,height,steps):
        self.w = canvas
        self.x = width
        self.y = height
        self.steps = steps
        self.xlabels = []
        self.ylabels = []
        
        self.makeGrid()
        
    def makeCross(self,x,y):
        self.w.create_line(x-5,y-5,x+5,y+6)
        self.w.create_line(x+5,y-6,x-5,y+5)
        
    def generateLabelsList(self):
        amountx = int(((self.x/self.steps)/2)-1)
        amounty = int(((self.y/self.steps)/2)-1)
        labelsx = []
        labelsy = []
        
        for i in range(amountx*2):
            if i == 0:
                labelsx.append("-"+str(amountx))
            elif i < amountx:
                labelsx.append("-"+str(amountx-i))
            elif i == amountx:
                labelsx.append(str(int(i/i)))
            else:
                labelsx.append(str(int(i-3)))
                
            
        for i in range(amounty*2):
            if i == 0:
                labelsy.append(str(amounty))
            elif i < amounty:
                labelsy.append(str(amounty-i))
            elif i == amounty:
                labelsy.append("-"+str(int(i/i)))
            else:
                labelsy.append("-"+str(int(i-3)))
                
            
        self.xlabels = labelsx
        self.ylabels = labelsy
        
        
    def makeGrid(self):
        # X-/Y-Axis
        self.w.create_line(0,self.x/2,self.y,self.y/2) #X
        self.w.create_line(self.x/2,0,self.y/2,self.y) #Y
    
        # Axis labels
        self.w.create_text((self.x/2)+10,20,text="Y",fill="purple")
        self.w.create_text(self.x-10,(self.y/2)+20,text="X",fill="purple")
    
        # Axis strikes and labels
        self.generateLabelsList()
        i = self.steps
        label = 0
        while (i<=self.x-self.steps):
            if i != self.x/2:
                # Grid
                self.w.create_line(0,i,self.x,i,fill="gray")
                self.w.create_line(i,0,i,self.y,fill="gray")
            
                # Labels
                self.w.create_text(i,(self.y/2)+10,text=self.xlabels[label]) #X
                self.w.create_text((self.x/2)-10,i,text=self.ylabels[label]) #Y
            
            else:
                label=label-1
        
            self.w.create_line(i,(self.y/2)-5,i,(self.y/2)+5) #X
            self.w.create_line((self.x/2)-5,i,(self.x/2)+5,i) #Y
            
            i=i+self.steps
            label=label+1
