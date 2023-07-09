import psutil
from tkinter import *

checkr = False
checks = False
count = 0

def close_window():
    global checks
    checks = True
    app.destroy()

def close_window_recv():
    global checkr
    checkr = True
    app.destroy()

while True:
    counts = 0
    if checkr and checks:
        sent = network.bytes_sent
        recv = network.bytes_recv
        with open('bytes.txt', 'a+') as file:
            lines = file.readlines()

            for line in lines:
                check1 = line.strip().split("|")
                bytes_sent, sent_no = check1[0], int(check1[1])
                sent = (sent + sent_no) / 2
                if counts == 1:
                    recv = (recv + sent_no) / 2

                counts += 1

            file.seek(0)
            file.truncate()
            file.write("Sent|" + str(sent) + "\n")
            file.write("Recv|" + str(recv) + "\n")
            file.close()
        exit()

    count = 0
    network = psutil.net_io_counters()

    with open('bytes.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        check1 = line.strip().split("|")
        bytes_sent, sent_no = check1[0], int(check1[1])
        sent = network.bytes_sent

        if int(sent) >= int(sent_no):
            if not checks:
                app = Tk()
                app.geometry('400x200')
                app.title("Network Overload Sent")

                label_limit = Label(app, text="LIMIT", foreground="blue", font=("Arial", 12))
                label_limit.pack()

                limit = Label(app, text=sent_no, foreground="darkblue", font=("Arial", 16))
                limit.pack()

                label_sent = Label(app, text="SENT", foreground="green", font=("Arial", 12))
                label_sent.pack()

                used = Label(app, text=sent, foreground="darkgreen", font=("Arial", 16))
                used.pack()

                button_ok = Button(app, text="OK", command=close_window)
                button_ok.pack()

                app.mainloop()

        recv = network.bytes_recv
        
        if count == 1:
        
            if int(recv) >= int(sent_no):
                if not checkr:
                    print(55)
                    app = Tk()
                    app.geometry('400x200')
                    app.title("Network Overload Receive")

                    label_limit = Label(app, text="LIMIT", foreground="blue", font=("Arial", 12))
                    label_limit.pack()

                    limit = Label(app, text=sent_no, foreground="darkblue", font=("Arial", 16))
                    limit.pack()

                    label_sent = Label(app, text="RECV", foreground="green", font=("Arial", 12))
                    label_sent.pack()

                    used = Label(app, text=recv, foreground="darkgreen", font=("Arial", 16))
                    used.pack()

                    button_ok = Button(app, text="OK", command=close_window_recv)
                    button_ok.pack()

                    app.mainloop()

        count += 1
