from random import uniform
from tkinter import INSERT
from tkinter import END

class ButtonFunc:
    """ a container to hold all the functions for the buttons """
    def __init__(self):
        """ initalize all variables """
        self.readyList = []
        self.blockedList = []
        self.endList = []
        
        self.counter = 1
        self.currentProcess = self._generateProcess(-1)
        
    def _increaseCounter(self):
        """ increases the counter for processes """
        self.counter += 1
        
    def _generateProcess(self, id):
        """ will return a process """
        process = {
            'id' : '',
            'name' : 'Process',
            'priority' : ''
        }
        
        process['id'] = id
        process['priority'] = int(uniform(1, 10))
        
        return process
    
    def _formattedOutput(self, process):
        """ return the neatly formatted info inside of Process """
        return (f"{process['id']} {process['name']} {process['priority']} \n")

# ----------------------------------------------------------------------------

    def clicked(self, txt_box):
        """ test click func """
        mssg = "Process 1"
        txt_box.insert(0, mssg)
        
    def onAddProcess(self, ready_box, running_box):
        """ 
        create process on button click, update the running process and the 
        ready_box
        """
        ready_box.configure(state = 'normal')
        running_box.configure(state = 'normal')
        ready_box.delete('1.0', END)
        
        self.readyList.append(self._generateProcess(self.counter))
        
        tempValue = 0
        # tempProcess = generateProcess(-1)
        
        for process in self.readyList:
            if process['priority'] > tempValue:
                tempValue = process['priority']
                self.currentProcess = process
                
        
        if running_box.get() == "":
            running_box.insert(
                INSERT, self._formattedOutput(self.currentProcess))
            for i in range(len(self.readyList)):
                if self.readyList[i]['id'] == self.currentProcess['id']:
                    del self.readyList[i]
                    break
        else:
            for process in self.readyList:
                # ready_box.configure(state = 'normal')
                ready_box.insert(INSERT, self._formattedOutput(process))
                
        ready_box.configure(state = 'disabled')
        running_box.configure(state = 'disabled')
        self._increaseCounter()