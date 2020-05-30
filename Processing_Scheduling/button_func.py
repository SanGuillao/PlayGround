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
        self.termList = []
        
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
            'priority' : '',
            'size' : ''
        }
        
        process['id'] = id
        process['priority'] = int(uniform(1, 10))
        process['size'] = int(uniform(5, 15))
        
        return process
    
    def _formattedOutput(self, process):
        """ return the neatly formatted info inside of Process """
        if process:
            return (f"Process ID: {process['id']} "
                f"| Priority: {process['priority']} \n")
        
    def _updateRunning(self, ready_box, running_box):
        """ 
        update the process running and the list of processes in the ready box 
        """
        # enable txt box
        running_box.configure(state = 'normal')
        
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
        
        # update the ready box
        self._updateReadyBox(ready_box)
        # disable the txt box
        running_box.configure(state = 'disabled')
    
    def _updateReadyBox(self, ready_box):
        """ update the ready box """
        # enable the txt box and delete old info
        ready_box.configure(state = 'normal')
        ready_box.delete('1.0', END)
        
        for process in self.readyList:
            ready_box.insert(INSERT, self._formattedOutput(process))
            
        # disable txt box
        ready_box.configure(state = 'disabled')
        
    def _updateBlockedBox(self, blocked_box):
        """ update the blocked box """
        # enable txt box, and delete old info
        blocked_box.configure(state = 'normal')
        blocked_box.delete('1.0', END)
        
        # update the blocked box
        for process in self.blockedList:
            blocked_box.insert(INSERT, self._formattedOutput(process))
        
        # disable txt box
        blocked_box.configure(state = 'disabled')
        
    def _updateTerminateBox(self, terminated_box):
        """ update the terminated box """
        # enable the txt box, delete any old info
        terminated_box.configure(state = 'normal')
        terminated_box.delete('1.0', END)
        
        # update the terminated box
        for process in self.termList:
            terminated_box.insert(INSERT, self._formattedOutput(process))
            
        # disable the txt box
        terminated_box.configure(state = 'disabled')

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
        # create the new process, add it to the ready list
        self.readyList.append(self._generateProcess(self.counter))
        
        # update the currently running process
        self._updateRunning(ready_box, running_box)
        
        # increase the count of created processes
        self._increaseCounter()
        
    def onBlock(self, ready_box, running_box, blocked_box):
        """ 
        send current process to the blocked list, grab the next process from 
        the readyList, update the proper txt boxes 
        """
        
        # delete the contents in the running txt box
        running_box.configure(state = 'normal')
        running_box.delete('0', END)
        
        # check to see if the current process is already in the blocked list
        if self.currentProcess not in self.blockedList and self.currentProcess:
            tempProcess = deepcopy(self.currentProcess)
            #print(self._formattedOutput(tempProcess))
            
            # add the process to the blocked list
            self.blockedList.append(tempProcess)   
        
        # update the blocked_box
        self._updateBlockedBox(blocked_box)
        
        # if there are any other processes in the ready list
        if self.readyList:
            # update the running process
            self._updateRunning(ready_box, running_box)
        
        # disable txt boxes 
        running_box.configure(state = 'disabled')
        
        
    def onTimeSlice(self, ready_box, running_box):
        """ 
        grab the next highest priority process from the ready list 
        and send the current process back into the ready list
        """
        # check to see if there is another process in ready list
        if self.readyList:
            # enable txt boxes for editing and delete the contents in running 
            # txt box
            running_box.configure(state = 'normal')
            running_box.delete('0', END)
            
            # copy the current process into a temp process
            tempProcess = deepcopy(self.currentProcess)
            
            # send the next highest priority process into current
            if self.readyList:
                self._updateRunning(ready_box, running_box)
                
            # put the temp process back into the ready list
            self.readyList.append(tempProcess)
            # update the ready box with the new process
            self._updateReadyBox(ready_box)
                
            
            # disable the txt boxes
            running_box.configure(state = 'disabled')
    
    def onSend(self, ready_box, blocked_box, running_box):
        """ 
        send the front most process in the blocked list back into the
        ready list
        """
        # check to see if there are any processes in the blocked list
        if self.blockedList:
            # send the first process in blocked list to the readyList
            # make sure to remove the process from blockedList
            self.readyList.append(self.blockedList.pop(0))
            
            # update all boxes
            if running_box.get() == "":
                self._updateRunning(ready_box, running_box)
            else:
                self._updateReadyBox(ready_box)
            
            self._updateBlockedBox(blocked_box)  
    
    def onTerminate(self, ready_box, running_box, terminated_box):
        """ 
        end the current process and send the next process in readyList
        into the current
        """
        
        # delete the contents in the running txt box
        running_box.configure(state = 'normal')
        running_box.delete('0', END)
        
        if self.currentProcess not in self.termList and self.currentProcess:
            tempProcess = deepcopy(self.currentProcess)
            
            self.termList.append(tempProcess)
            
        self._updateTerminateBox(terminated_box)
        
        if self.readyList:
            self._updateRunning(ready_box, running_box)
        else:
            del self.currentProcess
            self.currentProcess = None
        
        # disable txt boxes 
        running_box.configure(state = 'disabled')