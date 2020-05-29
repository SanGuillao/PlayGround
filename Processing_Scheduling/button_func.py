from copy import deepcopy
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
        
        self.flag = False
        
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
        
    def _updateRunning(self, ready_box, running_box):
        """ 
        update the process running and the list of processes in the ready box 
        """
        
        tempValue = 0
        # tempProcess = generateProcess(-1)
        
        if running_box.get() == "" and len(self.readyList) > 0:
            for process in self.readyList:
                if process['priority'] > tempValue:
                    tempValue = process['priority']
                    self.currentProcess = process
                    
            running_box.insert(
                INSERT, self._formattedOutput(self.currentProcess))
            for i in range(len(self.readyList)):
                if self.readyList[i]['id'] == self.currentProcess['id']:
                    del self.readyList[i]
                    break
            
        for process in self.readyList:
            # ready_box.configure(state = 'normal')
            ready_box.insert(INSERT, self._formattedOutput(process))
        
        #print(self._formattedOutput(self.currentProcess))

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
        # enable the txt boxes
        ready_box.configure(state = 'normal')
        running_box.configure(state = 'normal')
        ready_box.delete('1.0', END)
        
        # create the new process, add it to the ready list
        self.readyList.append(self._generateProcess(self.counter))
        
        # update the currently running process
        self._updateRunning(ready_box, running_box)
        
        # disable txt boxes
        ready_box.configure(state = 'disabled')
        running_box.configure(state = 'disabled')
        
        # increase the count of created processes
        self._increaseCounter()
        
    def onBlock(self, ready_box, running_box, blocked_box):
        """ 
        send current process to the blocked list, grab the next process from 
        the readyList, update the proper txt boxes 
        """
        # enable txt boxes for editing
        ready_box.configure(state = 'normal')
        running_box.configure(state = 'normal')
        blocked_box.configure(state = 'normal')
        
        # delete the contents in the txt boxes
        blocked_box.delete('1.0', END)
        ready_box.delete('1.0', END)
        running_box.delete('0', END)
        
        # check to see if the current process is already in the blocked list
        if self.currentProcess not in self.blockedList:
            tempProcess = deepcopy(self.currentProcess)
            #print(self._formattedOutput(tempProcess))
            
            # add the process to the blocked list
            self.blockedList.append(tempProcess)   
        
        # update the blocked box
        for process in self.blockedList:
            blocked_box.insert(INSERT, self._formattedOutput(process))
        
        # if there are any other processes in the ready list
        if self.readyList:
            # update the running process
            self._updateRunning(ready_box, running_box)
        
        # disable txt boxes 
        ready_box.configure(state = 'disabled')
        running_box.configure(state = 'disabled')
        blocked_box.configure(state = 'disabled')
        
    def onTimeSlice(self, ready_box, running_box):
        """ """
    
    def onSend(self, ready_box, blocked_box):
        """ """
    
    def onTerminate(self, running_box, ready_box, terminated_box):
        """ """