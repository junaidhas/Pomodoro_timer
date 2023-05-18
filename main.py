from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#95cd41"
YELLOW = "#f7f5dd"
DARKBLUE = "#16697a"
GOLD = "#ffd95a"
BROWN = "#C07F00"
FONT_NAME = "Cambria"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="TIMER")
    check_marks.config(text="")
    global reps
    reps =0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_time = WORK_MIN * 60
    short_breaktime =SHORT_BREAK_MIN * 60
    long_breaktime = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        count_down(long_breaktime)
        title_label.config(text="Long break",fg=RED)
    elif reps % 2 ==0:
        count_down(short_breaktime)
        title_label.config(text="Break",fg=DARKBLUE)
    else:
        count_down(work_time)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):


    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec <10:
        count_sec=f"0{count_sec}"

    canvas.itemconfig(timer_text,text =f"{count_min}:{count_sec}")
    print(count)
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks +="✔"
            check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100, bg=GOLD)




title_label = Label(text="Timer", fg=DARKBLUE, bg=GOLD, font=(FONT_NAME,45))
title_label.grid(row=0, column=1)

canvas = Canvas(width=200, height= 224, bg=GOLD, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image= tomato_img)
timer_text = canvas.create_text(100,140, text= "00:00", fill="white",font=(FONT_NAME, 40, "bold"))
canvas.grid(row=1,column=1)


start_button = Button(text="START", command= start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2,column=2)

check_marks = Label(fg=GREEN, bg=GOLD, font=20)
check_marks.grid(row=3, column=1)
window.mainloop()
