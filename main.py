import gooeypie as gp

def load_common_words(file_path):
    with open(file_path, 'r') as file:
        common_words = file.read().splitlines()
    return common_words

def is_common_word(word, common_words):
    return word in common_words

def toggle_mask(event):
    secret.toggle()

common_words = load_common_words('common_words.txt')

def on_text_change(event):
    
    text = secret.text
    print(text)

    if is_common_word(text, common_words):
        label.text = "Common password/word"
    else:
        label.text = "Not a common password/word"

    if text.isdigit():
        label_num.text = "Don't make it just numbers"
    else:
        label_num.text = "A combination of letters and numbers is good"
        
    if text.isalpha():
        label_num.text = "Try to have a combination of letters and numbers"
    if len(text) == 0:
        label_length.text = "Nothing"    
    if len(text) >= 1:
        label_length.text = "Too short"
    if len(text) >= 10:
        label_length.text = "Decent length"
    if len(text) >= 15:
        label_length.text = "Good length"

def open_about_window(event):
    about_window.show()

def check_exit():
    ok_to_exit = app.confirm_yesno(None, 'Are you sure you want to close?', 'question')
    return ok_to_exit

app = gp.GooeyPieApp('Password Checker')

app.title = 'Password Checker'

question = gp.Label(app, "Type in your password")

secret = gp.Secret(app)
secret.width = 50

check = gp.Checkbox(app, 'Reveal Password')
check.add_event_listener('change', toggle_mask)

label = gp.Label(app, '...')
label_length = gp.Label(app, '...')
label_num = gp.Label(app, '...')

about_btn = gp.Button(app, '?', open_about_window)
about_btn.width = 5

enter_btn = gp.Button(app, 'Enter', on_text_change)

app.set_grid(6, 2)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(enter_btn, 2, 2, align='center')
app.add(check, 3, 1)
app.add(label, 4, 1, align='center')
app.add(label_length, 5, 1, align='center')
app.add(label_num, 6, 1, align='center')
app.add(about_btn, 6, 2, align='center')

about_window = gp.Window(app, 'About')
about_window.width = 300
about_message = gp.Label(about_window, 'About: ')
about_window.set_grid(1, 1)
about_window.add(about_message, 1, 1)

app.on_close(check_exit)

app.run()