import gooeypie as gp

def toggle_mask(event):
    secret.toggle()

def on_text_change(event):
    text = secret.text
    print(text)
    if text == "Test":
        label.text = "1,2,3"

def check_exit():
    ok_to_exit = app.confirm_yesno(None, 'Are you sure you want to close?', 'question')
    return ok_to_exit

app = gp.GooeyPieApp('Password Checker')

app.title = 'Password Checker'

question = gp.Label(app, "Type in your password")

secret = gp.Secret(app)
secret.width = 50
secret.add_event_listener('change', on_text_change)

check = gp.Checkbox(app, 'Reveal Password')
check.add_event_listener('change', toggle_mask)

label = gp.Label(app, '...')
label_length = gp.Label(app, '...')

app.set_grid(4, 1)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(check, 3, 1)
app.add(label, 4, 1, align='center')

app.on_close(check_exit)

app.run()