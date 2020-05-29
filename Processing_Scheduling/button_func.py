from random import uniform
from tkinter import INSERT
from tkinter import END

def clicked(txt_box):
    """ test click func """
    mssg = "Process 1"
    txt_box.insert(0, mssg)
    
def generateProcess(id):
    """ will return a process """
    process = {
        'id' : '',
        'name' : 'Process',
        'priority' : ''
    }
    
    process['id'] = id
    process['priority'] = int(uniform(1, 10))
    
    return process
    
def formattedOutput(process):
    """ return the neatly formatted info inside of Process """
    return (f"{process['id']} {process['name']} {process['priority']} \n")
    
def onAddProcess(ready_box, readyList, running_box, currentProcess):
    """ 
    create process on button click, update the running process and the 
    ready_box
    """
    ready_box.configure(state = 'normal')
    running_box.configure(state = 'normal')
    ready_box.delete('1.0', END)
    
    readyList.append(generateProcess(len(readyList) + 2))
    
    tempValue = 0
    # tempProcess = generateProcess(-1)
    
    for process in readyList:
        if process['priority'] > tempValue:
            tempValue = process['priority']
            currentProcess = process
            
    
    if running_box.get() == "":
        running_box.insert(INSERT, formattedOutput(currentProcess))
        for i in range(len(readyList)):
            if readyList[i]['id'] == currentProcess['id']:
                del readyList[i]
                break
    else:
        for process in readyList:
            # ready_box.configure(state = 'normal')
            ready_box.insert(INSERT, formattedOutput(process))
            
    ready_box.configure(state = 'disabled')
    running_box.configure(state = 'disabled')