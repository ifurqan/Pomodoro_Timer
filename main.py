from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_window = ""
# ---------------------------- TIMER RESET ------------------------------- #
def reset_function():
    check.config(text="")
    window.after_cancel(timer_window)
    title_label.config(text="Timer")
    canvas.itemconfig(timer,text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps +=1
    if reps % 8 == 0:
        title_label.config(text="Break",fg = RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        title_label.config(text="Break",fg = PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title_label.config(text="Work",fg = GREEN)
        count_down(WORK_MIN * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_min(input_time):
    minute = int(input_time/60)
    second = input_time % 60
    if minute < 10:
        minute = f"0{minute}"
    if second < 10:
        second = f"0{second}"
    return f"{minute}:{second}"
def count_down(input_time):
    if input_time>=0:
        canvas.itemconfig(timer,text=count_min(input_time))
        global timer_window
        timer_window = window.after(1000,count_down,input_time-1)
    else:
        start_timer()
        checkmark = ""
        for i in range(int(reps/2)):
            checkmark += "✓"
        check.config(text=checkmark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pomodoro Game")
window.config(padx=100,pady=50,bg=YELLOW)
title_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"))
title_label.config(bg=YELLOW)
title_label.grid(row=0,column=1)
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)
start = Button(text="START", highlightthickness=0,command=start_timer)
start.grid(row=2,column=0)
reset = Button(text="RESET",highlightthickness=0,command=reset_function)
reset.grid(row=2,column=2)
check = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,25,"bold"))
check.grid(row=3,column=1)
window.mainloop()
