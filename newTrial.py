import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.player_selection_and_score()
        self.process_button()
        self.create_table()

    def player_selection_and_score(self):
        #self.player = StringVar() # forgot (), use `self`
        top = tk.LabelFrame(self.root)
        top.grid(column=0, row=0)

        self.player1_selection = ttk.Combobox(top, width=10, state='readonly') # , textvariable=player
        self.player1_selection["values"] = ("Player1", "Player2", "Player3")
        self.player1_selection.grid(column=1, row=0, sticky="w")
        self.player1_selection.current(0)

        self.player1_selection.bind("<<ComboboxSelected>>", self.on_combobox_select)

        #global player1_var # better use `self.`
        #player1_var = player1_selection.get() # useless

        self.player1_score_entry = tk.Spinbox(top, width=5, from_=0, to=10, command=self.on_spinbox_select)
        self.player1_score_entry.grid(column=4, row=0)

        #global player1_score_var # better use `self.`
        #player1_score_var = player1_score_entry.get() # useless

    def on_combobox_select(self, event):
        print("Combobox:", event.widget.get())

    def on_spinbox_select(self):
        print("Spinbox:", self.player1_score_entry.get())

    def process_button(self):
        bottom = tk.LabelFrame(self.root)
        bottom.grid(column=0, row=2)

        process_button = tk.Button(bottom, text="Process Result", command=self.data_entry)
        process_button.pack()

    def create_table(self):
        c.execute("CREATE TABLE IF NOT EXISTS fixtures (player1 TEXT, player1_score REAL)")

    def data_entry(self):
        player1_var = self.player1_selection.get()
        player1_score_var = self.player1_score_entry.get()

        # too many `?`
        c.execute("INSERT INTO fixtures (player1, player1_score) VALUES (?, ?)", (player1_var, player1_score_var))
        conn.commit()

#player1_var = GUI() # ??? something stupid
#player1_score_var = GUI() # ??? something stupid

# --- main ---

conn = sqlite3.connect("database.db")
c = conn.cursor()

gui = GUI()
gui.root.mainloop()

c.close() # first close `c` later `conn`
conn.close()