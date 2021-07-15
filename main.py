import tkinter
import playground

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=400, height=400)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)








window.mainloop()

