import tkinter as tk
from PIL import Image, ImageTk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CiviConquest")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.font_title = ("Helvetica", 24, "bold")
        self.font_text = ("Helvetica", 18)
        self.GREEN = "green"
        self.BLUE = "blue"

        self.player_image_tk = None
        self.ai_image_tk = None

        self.question_text = None
        self.yes_button = None
        self.no_button = None

        self.root.update()  # Update the GUI to ensure elements are displayed

    def load_images(self):
        player_image = Image.open("player_image.png")
        ai_image = Image.open("ai_image.png")

        player_image = player_image.resize((100, 100), Image.ANTIALIAS)
        ai_image = ai_image.resize((100, 100), Image.ANTIALIAS)

        self.player_image_tk = ImageTk.PhotoImage(player_image)
        self.ai_image_tk = ImageTk.PhotoImage(ai_image)

    def get_player_input(self, player):
        if self.yes_button is None:
            self.question_text = tk.Label(self.root, text="Build a structure?", font=self.font_text)
            self.question_text.pack()
            self.yes_button = tk.Button(self.root, text="Yes", command=self.handle_yes, font=self.font_text)
            self.no_button = tk.Button(self.root, text="No", command=self.handle_no, font=self.font_text)
            self.yes_button.pack()
            self.no_button.pack()

        self.player_input = None
        self.root.mainloop()

        return self.player_input

    def handle_yes(self):
        self.player_input = True
        self.root.quit()

    def handle_no(self):
        self.player_input = False
        self.root.quit()

    def draw(self, player_name, ai_name, territories_player, territories_ai):
        self.canvas.delete("all")  # Clear the canvas

        if self.player_image_tk is None or self.ai_image_tk is None:
            self.load_images()

        self.canvas.create_image(100, 100, image=self.player_image_tk, anchor=tk.NW)
        self.canvas.create_image(600, 100, image=self.ai_image_tk, anchor=tk.NW)

        territories_text_player = f"Territories: {territories_player}"
        territories_text_ai = f"Territories: {territories_ai}"

        self.canvas.create_text(100 + self.player_image_tk.width() / 2, 220, text=player_name, fill=self.GREEN, font=self.font_text, anchor=tk.CENTER)
        self.canvas.create_text(600 + self.ai_image_tk.width() / 2, 220, text=ai_name, fill=self.BLUE, font=self.font_text, anchor=tk.CENTER)
        self.canvas.create_text(100 + self.player_image_tk.width() / 2, 300, text=territories_text_player, fill=self.GREEN, font=self.font_text, anchor=tk.CENTER)
        self.canvas.create_text(600 + self.ai_image_tk.width() / 2, 300, text=territories_text_ai, fill=self.BLUE, font=self.font_text, anchor=tk.CENTER)

        self.root.update()

    def run(self):
        self.root.mainloop()

