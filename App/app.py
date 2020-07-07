from tkinter import *
import scrape


def download():
    topic = Entry.get(E1)
    n = Entry.get(E2)
    print("Topic "+topic)
    scrape.scrape_and_run(topic, n)
    print("Download xong!")

if __name__ == '__main__':
    top = Tk()
    L1 = Label(top, text="Input topic: ")
    L1.grid(row=1, column=0)

    E1 = Entry(top, bd=5)
    E1.grid(row=1, column=1)
    
    L2 = Label(top, text="Number of books: ")
    L2.grid(row=2, column=0)

    E2 = Entry(top, bd=5)
    E2.grid(row=2, column=1)


    B = Button(top, text="Submit", command=download)
    B.grid(row=3, column=1)


    top.mainloop()