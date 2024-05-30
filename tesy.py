import gooeypie as gp

def toggle_mask(event):
    secret.toggle()

def on_text_change(event):
    text = secret.text
    print(text)
    if text == "Test":
        label.text = "1,2,3"
    if text == int:
        label_num.text = "Just a number"
    if len(text) <= 5:
        label_length.text = "Too short"
    if len(text) >= 10:
        label_length.text = "Better"
    if len(text) >= 15:
        label_length.text = "Good"

def check_exit():
    ok_to_exit = app.confirm_yesno(None, 'Are you sure you want to close?', 'question')
    return ok_to_exit

app = gp.GooeyPieApp('Password Checker')

app.title = 'Password Checker'

question = gp.Label(app, "Type in your password")

secret = gp.Secret(app)
secret.width = 50
secret.add_event_listener('change', on_text_change)

check = gp.ImageButton(app, 'images/eepy.png', None)
check.add_event_listener('change', toggle_mask)

label = gp.Label(app, '...')
label_length = gp.Label(app, '...')
label_num = gp.Label(app, '...')

app.set_grid(6, 2)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(check, 2, 2)
app.add(label, 4, 1, align='center')
app.add(label_length, 5, 1, align='center')
app.add(label_num, 6, 1, align='center')

app.on_close(check_exit)

app.run()