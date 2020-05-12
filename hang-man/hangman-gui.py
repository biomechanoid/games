import tkinter as tk
import hangman


class App(tk.Frame):
    ent_name = None
    user_name = None
    ent_value = None
    hangman = None
    canvas = None
    frm = None
    rounds = None
    cords = [
        (450, 300, 450, 50),
        (450, 50, 250, 50),
        (450, 100, 400, 50),
        (250, 50, 250, 100),
        (220, 100, 280, 160),
        (250, 160, 250, 220),
        (250, 220, 280, 285),
        (250, 220, 220, 285),
        (250, 180, 210, 200),
        (250, 180, 290, 200),
        (235, 120, 240, 125),
        (260, 120, 265, 125),
        (235, 140, 265, 140)
    ]

    def __init__(self, master=None, rounds=10):
        super().__init__(master)
        self.game_message = tk.StringVar()
        self.master = master
        self.hangman = hangman
        self.rounds = rounds
        self.pack(fill="both", expand=True)
        self.welcome()

    def clear_event(self, event):
        if not self.user_name:
            self.user_name = event.widget.master.ent_name.get()
        self.game_message.set("")
        self.clear()

    def clear(self):
        self.destroy()
        if self.frm:
            self.frm.destroy()
        self.game()

    def welcome(self):
        lbl_greeting = tk.Label(master=self, text="Hang Man", height=5, font=('Arial Bold', 20))
        lbl_greeting.pack()

        self.ent_name = tk.Entry(master=self, width=25, font=('Arial', 12))
        self.ent_name.insert(0, "Player1")
        self.ent_name.pack()

        btn_start = tk.Button(master=self, text="Start", bg="gray", fg="white", padx=20, pady=10,
                              font=('Arial Bold', 12))
        btn_start.bind("<Button-1>", self.clear_event)
        btn_start.pack()

    def game(self):
        self.hangman.init_game()
        self.frm = tk.Frame(master=root)

        tk.Label(master=self.frm, text="Hang Man: Hi " + self.user_name, height=2).grid(row=0, column=2)
        self.display_message()
        self.canvas = tk.Canvas(master=self.frm, width=595, height=300, bg='gray')
        self.canvas.grid(row=1, column=0, rowspan=4, columnspan=3)

        self.render_character_boxes()

        tk.Label(master=self.frm, text='Type character: ', font=('Arial Bold', 12)).grid(row=15, column=0, sticky='E')
        self.ent_value = tk.Entry(master=self.frm, font=('Arial', 16))
        self.ent_value.grid(row=15, column=1)

        self.btn_submit = tk.Button(master=self.frm, text="Submit", padx=20, pady=10, bg='gray', font=('Arial', 12))
        self.btn_submit.grid(row=20, column=1)
        self.btn_submit.bind("<Button-1>", self.process_guess)

        self.new_game_button()

        self.frm.pack(fill="both", expand=True)

    def new_game_button(self):
        btn_proc = tk.Button(master=self.frm, text="New Game", padx=15, pady=5, bg='gray', font=('Arial', 12))
        btn_proc.grid(row=20, column=2)
        btn_proc.bind("<Button-1>", self.clear_event)
        return btn_proc

    def render_character_boxes(self):
        lbl_frame = tk.LabelFrame(master=self.frm)
        lbl_frame.grid(row=10, column=0, columnspan=3)
        state = self.hangman.get_state()['user_string']
        for key in state:
            if state[key] != '':
                char = state[key]
            else:
                char = '_'

            tk.Label(master=lbl_frame, text=char, padx=5, pady=5, font=("Arial", 32), borderwidth=1,
                     relief="solid").grid(row=3, column=key)

    def process_guess(self, event):
        if len(self.ent_value.get()) > 0:
            print('test', self.hangman.guess_character(self.ent_value.get()[0]))
            self.ent_value.delete(0, tk.END)
            self.ent_value.select_clear()
            if list(self.hangman.get_state()['secret'].upper()) == list(self.hangman.get_state()['user_string'].values()):
                self.game_message.set("Well Done")
                self.btn_submit["state"] = tk.DISABLED
                self.ent_value["state"] = tk.DISABLED
            if self.process_game_results():
                if self.hangman.get_state()['status']:
                    self.render_character_boxes()
                else:
                    key = self.hangman.get_state()['round']
                    print(key)
                    if key <= 3:
                        self.canvas.create_line(self.cords[key], width=5.0, fill="blue")
                    elif key == 4:
                        self.canvas.create_oval(self.cords[key], width=4.0)
                    elif 5 <= key <= 9:
                        self.canvas.create_line(self.cords[key], width=4.0)
                    elif 10 <= key <= 11:
                        self.canvas.create_rectangle(self.cords[key], fill="black")
                    else:
                        self.canvas.create_line(self.cords[key], width=4.0)
                        self.btn_submit["state"] = tk.DISABLED
                        self.ent_value["state"] = tk.DISABLED
                        self.game_message.set("Game Over")

    def process_game_results(self, result=True):
        if self.hangman.get_state()['round'] == self.rounds:
            self.clear()
            result = False
        return result

    def display_message(self):
        tk.Label(master=self.frm, text='', padx=5, pady=5, font=("Arial Bold", 20), textvariable=self.game_message).grid(row=0, column=1)

root = tk.Tk()
root.geometry("600x500")
root.title("Hang Man")

app = App(master=root, rounds=13)
root.mainloop()
