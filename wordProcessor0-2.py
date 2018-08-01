from guizero import App, TextBox, PushButton, yesno, MenuBar, warn
from tkinter import filedialog


def openFile():
    global data
    app.filename = filedialog.askopenfilename(initialdir="/", title = "Open", filetypes=(("text files", "*.txt"),("all files", "*.*")))
    warn("This File?", "Openning "+app.filename)
    theFile = open(app.filename, "r")
    data.value = theFile.read()
    app.title=app.filename
    theFile.close()
    #app.update()
    
def saveFile():
    global data
    app.filename = filedialog.asksaveasfilename(initialdir="/", title="Save as", filetypes = (("text files", "*.txt"),("all files", "*.*")))
    warn("This File?", "Saving as "+app.filename)
    print(data.value)
    theFile = open(app.filename, "w")
    theFile.write(data.value)
    app.title=app.filename
    theFile.close()

def encryptFile():
    warn("Error", "I don't know how to do that yet")
    
def decryptFile():
    warn("Error", "I don't know how to do that yet")


def closeHandler():
    global theFile
    if yesno("close", "Do you want to quit without saving?"):
        app.destroy()

app = App(title="untitled", height=600, width=600)
data = TextBox(app, height=600, width=600, multiline=True, scrollbar=True)
menubar = MenuBar(app, toplevel = ["File", "Encrypt"],
                  options=[
                      [["Open File", openFile], ["Save File", saveFile]],
                      [["Encrypt", encryptFile], ["Decrypt", decryptFile]]
                    ])
app.on_close(closeHandler)
app.display()