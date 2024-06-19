import gooeypie as gp
special_characters = "!@#$%^&*()-+?_=,<>/'"

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
    s = text
    score = 0

    if is_common_word(text, common_words):
        label.text = "Common password/word"
    else:
        label.text = "Not a common password/word"
        score += 1

    if text.isdigit():
        label_num.text = "Don't make it just numbers"
    elif text.isalpha():
        label_num.text = "Try to have a combination of letters and numbers"
    elif any(c.isdigit() for c in text) and any(c.isalpha() for c in text):
        label_num.text = "It has a combination of letters and numbers, good"
        score += 1
    else:
        label_num.text = "Try to have a combination of letters and numbers"

    if len(text) == 0:
        label_length.text = "Nothing"    
    if len(text) >= 1:
        label_length.text = "Too short"
    if len(text) >= 10:
        label_length.text = "Decent length"
    if len(text) >= 15:
        label_length.text = "Good length"
        score += 1

    if any(c in special_characters for c in s):
        label_special.text = "Your password has special characters in it"
        score += 1
    else:
        label_special.text = "Try to include some special characters in it (e.g. !, #, $)"

    if ' ' in text:
        label_space.text = "Having a space in it is good"
        score += 1
    else:
        label_space.text = "Try putting a space in it"

    if score == 0:
        label_score.text = "☆☆☆☆☆"
    elif score == 1:
        label_score.text = "★☆☆☆☆"
    elif score == 2:
        label_score.text = "★★☆☆☆"
    elif score == 3:
        label_score.text = "★★★☆☆"
    elif score == 4:
        label_score.text = "★★★★☆"
    elif score == 5:
        label_score.text = "★★★★★"

    print(score)


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
label_special = gp.Label(app, '...')
label_space = gp.Label(app, '...')
label_score = gp.Label(app, '...')

about_btn = gp.Button(app, '?', open_about_window)
about_btn.width = 5

enter_btn = gp.Button(app, 'Enter', on_text_change)

app.set_grid(9, 2)
app.add(question, 1, 1)
app.add(secret, 2, 1)
app.add(enter_btn, 2, 2, align='center')
app.add(check, 3, 1)
app.add(label, 4, 1, align='center')
app.add(label_length, 5, 1, align='center')
app.add(label_num, 6, 1, align='center')
app.add(label_special, 7, 1, align='center')
app.add(label_space, 8, 1, align='center')
app.add(label_score, 9, 1, align='center')
app.add(about_btn, 6, 2, align='center')

about_window = gp.Window(app, 'About')
about_window.width = 300
about_message = gp.Label(about_window, 'About: ')
about_window.set_grid(1, 1)
about_window.add(about_message, 1, 1)

app.on_close(check_exit)

app.run()