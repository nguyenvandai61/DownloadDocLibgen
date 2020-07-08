from tkinter import *
import scrape
import tkinter.scrolledtext as tkscrolled

bookLink = None

def submit():
    global var, bookLink
    topic = Entry.get(E1)
    ns = Entry.get(E2)
    if ns != "":
        ns = int(ns)
    else:
        ns = 3
    print("Topic "+topic)
    print(var.get())
    bookLink = scrape.scrape_and_run(topic, ns, var.get())

    initBook()
    
def initBook():
    global bookLink
    bookList = ""
    books = zip(bookLink.nameArr, bookLink.sizeArr)
    for name, size in books:
        bookList+= name +"\t"
        bookList+= size
        bookList+= "\n"
    TKScrollTXT.delete(1.0, END)
    TKScrollTXT.insert(1.0, bookList)

def download():
    topic = Entry.get(E1)
    scrape.download(bookLink, topic)
    print("Download xong!")
    L4.config(text = "Download xong!")
if __name__ == '__main__':
    top = Tk()
    L1 = Label(top, text="Input topic: ")
    L1.grid(row=1, column=0)

    E1 = Entry(top, bd=5)
    E1.grid(row=1, column=1, columnspan=4)
    
    L2 = Label(top, text="Number of books: ")
    L2.grid(row=2, column=0)

    E2 = Entry(top, bd=4)
    E2.grid(row=2, column=1,columnspan=4 )


    L3 = Label(top, text="Sort: ")
    L3.grid(row=3, column=0)

    var = StringVar()
    RB11 = Radiobutton(top, text="Title", variable= var, value="title", command="sort")
    RB12 = Radiobutton(top, text="Authors", variable= var, value="authors", command="sort")
    RB13 = Radiobutton(top, text="Publisher", variable= var, value="publisher", command="sort")
    RB14 = Radiobutton(top, text="Year", variable= var, value="year", command="sort")
    RB15 = Radiobutton(top, text="Page", variable= var, value="page", command="sort")
    RB16 = Radiobutton(top, text="Language", variable= var, value="language", command="sort")
    RB17 = Radiobutton(top, text="Size", variable= var, value="size", command="sort")
    RB18 = Radiobutton(top, text="Extension", variable= var, value="extension", command="sort")

    RB11.grid(row=3, column=1)
    RB12.grid(row=3, column=2)
    RB13.grid(row=3, column=3)
    RB14.grid(row=3, column=4)
    RB15.grid(row=4, column=1)
    RB16.grid(row=4, column=2)
    RB17.grid(row=4, column=3)
    RB18.grid(row=4, column=4)


    B = Button(top, text="Submit", command=submit)
    B.grid(row=4, column=7)
    B = Button(top, text="Download", command=download)
    B.grid(row=4, column=8)
    
    L4 = Label(top)
    L4.grid(row=5, column=2, columnspan=3)

    default_text = 'Ten sach se download hien o day!'
    width, height = 20,10
    TKScrollTXT = tkscrolled.ScrolledText(top)

    # set default text if desired
    TKScrollTXT.insert(1.0, default_text)
    TKScrollTXT.grid(row=6, column=0, columnspan=9)


    top.title("App tai sach")
    top.mainloop()