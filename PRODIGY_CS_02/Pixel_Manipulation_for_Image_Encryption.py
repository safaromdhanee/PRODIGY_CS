from tkinter import *
from tkinter import filedialog # this library will let us choose witch image to encrypt or decrypt 

# creating our GUI application
root = Tk()#GUI instance
root.geometry("350x150") # dimensions of the GUI

def encrypt_image():
    File1 = filedialog.askopenfile(mode='r',filetypes=[('jpg file','*.jpg'),('png file','*.png')])
    if File1 is not None :

        file_name = File1.name
        key = key1.get(1.0,END)
        print(file_name,key)
        file_data = open(file_name, 'rb')#'rb' is to read the data in the byte format
        image = file_data.read()
        file_data.close()
        image = bytearray(image) #convert the data into bytearray so that we can perform the operations pixel -----> byte
        for index,values in enumerate(image): #enumerate is providing index to all the values 
             image[index] = values^int(key) #using XOR method witch provides an interchangeable values since tuples cannot be edited and we have a tuple with the index and the value associate to it so it won't be able to provide the index there but it can be provide on lists and strings 
        file_data1=open(file_name,'wb')
        file_data1.write(image)
        file_data1.close()



button1 = Button(root,text="choose the image to encrypt or decrypt",command=encrypt_image)
button1.place(x=70,y=10)
key1 = Text(root,height=1,width=37) #zone text where will the user type the key 
key1.place(x=30,y=50)

root.mainloop()#closing the mainloop for successfully bind up these components on our gui
