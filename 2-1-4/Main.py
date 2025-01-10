#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")

# create empty frame
frame_login = tk.Frame(root)
frame_auth = tk.Frame(root)
frame_auth.grid(row="0", column="0", sticky="news")

frame_login.grid(row="0", column="0", sticky="news")
frame_auth.grid(row="0", column="0", sticky="news")


def login():
    frame_auth.tkraise()





lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()

ent_Username = tk.Entry(frame_login, bd=3)
ent_Username.pack(pady=10)


ent_username = tk.Entry(frame_login, bd=3)
ent_Username.pack()


lbl_username = tk.Label(frame_login, text='Password:')
lbl_username.pack()

ent_Username = tk.Entry(frame_login, bd=3)
ent_Username.pack(pady=5)

#login
button_login = tk.Button(frame_login, text="Login", command=login)
button_login.pack(pady=10)


lbl_authorized = tk.Label(frame_auth, text="Authorized Screen", font=('Times 14'))
lbl_authorized.pack(padx=50)

frame_login.tkraise()
root.mainloop()