from tkinter import *
from tkinter import ttk, messagebox
from randomword import RandomWord


words = RandomWord().get_random_word()

my_w = Tk()
my_w.geometry("600x400")  # Size of the window
my_w.title('Speed Typing Test')
my_w.after(1000, )

score = 0
answers = 0
timer = None
count = 60


def counting_points(list_word, answer_one):
    global score, answers
    if list_word == answer_one:
        score = score + 1
        answers += 1
        result_label.config(text=score)
    else:
        answers += 1


def scroll_word(event=None):
    word = words.pop(0)
    T.delete('1.0', END)
    T.insert(END, words[:5])

    text_response = text_answer.get("1.0", END)
    text_answer.delete('1.0', END)

    text_response = text_response.replace("\n", "")
    text_response = text_response.replace(" ", "")

    counting_points(word, text_response)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down():
    global count
    count -= 1
    if count == 0:
        time_count.config(text=f"{count}")
        count = 60
        termination()

    else:
        global timer
        timer = my_w.after(1000, count_down)
        time_count.config(text=f"{count}")


def initialization():
    global score, answers
    text_answer.config(state=NORMAL)
    btn_start.config(state=DISABLED)
    score = 0
    answers = 0
    result_label.config(text=score)
    count_down()


def termination():
    text_answer.delete('1.0', END)
    text_answer.config(state=DISABLED)
    btn_start.config(state=NORMAL)
    if answers > 0:
        avg = (score / answers) * 100
        messagebox.showinfo(title="Your Score!", message=f"You wrote {score} words in a minute\n"
                                                         f"On average, you wrote {avg:.1f}% of the words correctly.")


def reset():
    global count
    count = 1


T = Text(my_w, height=3, width=60)
T.place(x=60, y=150)
T.insert(END, words[:5])

text_answer = Text(my_w, height=3, width=60)
text_answer.place(x=60, y=230)
text_answer.config(state=DISABLED)

my_w.bind("<space>", scroll_word)

title_label = Label(my_w, text="Check your Speed Typing!", font="ariel 20 bold", anchor='e', fg='#8EC3B0')
title_label.place(x=120, y=30)

score_label = Label(my_w, text="Score:", font="ariel 13 bold", anchor='e')
score_label.place(x=60, y=100)

result_label = Label(my_w, text=score, font="ariel 13 bold", anchor='e')
result_label.place(x=125, y=100)

time_label = Label(my_w, text='Time:', font="ariel 13 bold", anchor='e')
time_label.place(x=460, y=100)

time_count = Label(my_w, text='60', font="ariel 13 bold", anchor='e')
time_count.place(x=520, y=100)

btn_start = Button(my_w, text="Start", bg='#E14D2A', fg='black', width=10,
               font='ariel 15 bold', relief=GROOVE, command=initialization)
btn_start.place(x=80, y=310)

btn_reset = Button(my_w, text="Reset", bg='#E14D2A', fg='black', width=10,
               font='ariel 15 bold', relief=GROOVE, command=reset)
btn_reset.place(x=240, y=310)

btn_exit = Button(my_w, text="Exit", bg='#E14D2A', fg='black', width=10,
               font='ariel 15 bold', relief=GROOVE, command=my_w.destroy)
btn_exit.place(x=400, y=310)

my_w.mainloop()
