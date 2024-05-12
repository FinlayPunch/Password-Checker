import gooeypie as gp


def say_hello(event):
    hello_lbl.text = 'Hello Gooey Pie!'

def check_exit():
    ok_to_exit = app.confirm_yesno(None, 'Are you sure you want to close?', 'question')
    return ok_to_exit

app = gp.GooeyPieApp('Hello')
app.width = 250
app.title = 'Password Checker'


hello_btn = gp.Button(app, 'Say Hello', say_hello)
hello_lbl = gp.Label(app, '')

app.set_grid(2, 1)

app.add(hello_btn, 1, 1, align='center')
app.add(hello_lbl, 2, 1, align='center')

app.on_close(check_exit)

app.run()