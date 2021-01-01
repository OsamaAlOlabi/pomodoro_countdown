from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

count = 5
while True:
    time.sleep(1)
    count -= 1
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Productivity App")
window.config(padx=100, pady=50, bg=YELLOW)

# Creating Timer Label
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer_label.grid(column=1, row= 0)

# Creating Cheakmark Label
check_label = Label(text="✔", bg=YELLOW, font=(FONT_NAME, 15))
check_label.grid(column=1, row=3)

# Creating Start Button
start_button = Button(text="Start", font=(FONT_NAME))
start_button.grid(column=0, row=2)

# Creating Reset Button
reset_button = Button(text="Reset", font=(FONT_NAME))
reset_button.grid(column=2, row=2)


# Creating the canvas
canvas = Canvas(width=200 ,height=224, bg=YELLOW, highlightthickness= 0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 130, text="00.00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row= 1)


window.mainloop()