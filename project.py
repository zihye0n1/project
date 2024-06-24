import tkinter
import playsound
import tkinter.font
window = tkinter.Tk()
window.title('음악플레이어')

window.geometry('800x400+200+200')




def playmusic1():
    # pass
    playsound.playsound('sample1.mp3')

def playmusic2():
    # pass
    playsound.playsound('sample2.mp3')

    

def playmusic3():
    # pass
    playsound.playsound('sample3.mp3')

def playmusic4():
    # pass
    playsound.playsound('sample4.mp3')


btn = tkinter.Button(text='재생', command=playmusic1)
btn.place(x=130, y=220)
btn = tkinter.Button(text='재생', command=playmusic2)
btn.place(x=295, y=220)
btn = tkinter.Button(text='재생', command=playmusic3)
btn.place(x=475, y=220)
btn = tkinter.Button(text='재생', command=playmusic4)
btn.place(x=650, y=220)




image1=tkinter.PhotoImage(file='힙합.png')
image2=tkinter.PhotoImage(file='발라드.png')
image3=tkinter.PhotoImage(file='케이팝.png')
image4=tkinter.PhotoImage(file='밴드.png')
label1=tkinter.Label(window, image=image1)
label2=tkinter.Label(window, image=image2)
label3=tkinter.Label(window, image=image3)
label4=tkinter.Label(window, image=image4)
label1.place(x=80, y=100)
label2.place(x=250, y=100)
label3.place(x=430, y=100)
label4.place(x=600, y=100)


window.mainloop()





