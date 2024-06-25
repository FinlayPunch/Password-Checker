import gooeypie as gp
special_characters = "!@#$%^&*()-+?_=,<>/'"
import pyperclip

colors = ['ConflowerBlue', 'LimeGreen', 'Orchid', 'DarkSlateGray']
fonts = ['Avenir']
styles = ['italic', 'normal']

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

def copy_password(event):
    pyperclip.copy(secret.text)
    app.alert('Success', 'Password copied to clipboard')

def open_about_window(event):
    about_window.show()

def open_help_window(event):
    help_window.show()

def check_exit():
    ok_to_exit = app.confirm_yesno(None, 'Are you sure you want to close?', 'question')
    return ok_to_exit

def open_password_checker(event):
    password_checker.show()

app = gp.GooeyPieApp('Password Checker')

# Main Window

main_window = gp.Window(app, 'Main Window')
main_button = gp.Button(main_window, 'Open Password Checker', open_password_checker)
main_title = gp.StyleLabel(main_window, 'Welcome to FishFixer')
main_label1 = gp.StyleLabel(main_window, 'Click the help button for information about how to use the program')
main_label2 = gp.StyleLabel(main_window, 'Click the about button for some background information about the program')
main_label3 = gp.StyleLabel(main_window, 'Click the password checker button to get into the main program')

about_btn = gp.Button(main_window, 'About', open_about_window)
help_btn = gp.Button(main_window, 'Help', open_help_window)
about_btn.width = 6
main_title.font_size = 20
main_window.set_grid(5, 3)
main_window.add(main_title, 1, 2, align ='center')
main_window.add(main_label1, 2, 2, align ='center')
main_window.add(main_label2, 3, 2, align ='center')
main_window.add(main_label3, 4, 2, align ='center')
main_window.add(main_button, 5, 2, align ='center')
main_window.add(about_btn, 5, 3, align='center')
main_window.add(help_btn, 5, 1, align='center')

# Password Checker Window
password_checker = gp.Window(app, 'Password Checker')
question = gp.Label(password_checker, "Type in your password")

secret = gp.Secret(password_checker)
secret.width = 50

check = gp.Checkbox(password_checker, 'Reveal Password')
check.add_event_listener('change', toggle_mask)

label = gp.Label(password_checker, '...')
label_length = gp.Label(password_checker, '...')
label_num = gp.Label(password_checker, '...')
label_special = gp.Label(password_checker, '...')
label_space = gp.Label(password_checker, '...')
label_score = gp.Label(password_checker, '...')

enter_btn = gp.Button(password_checker, 'Enter', on_text_change)
copy_button = gp.Button(password_checker, 'Copy?', copy_password)

password_checker.set_grid(9, 3)
password_checker.add(question, 1, 1)
password_checker.add(secret, 2, 1)
password_checker.add(enter_btn, 2, 2, align='center')
password_checker.add(copy_button, 2, 3, align='center')
password_checker.add(check, 3, 1)
password_checker.add(label, 4, 1, align='center')
password_checker.add(label_length, 5, 1, align='center')
password_checker.add(label_num, 6, 1, align='center')
password_checker.add(label_special, 7, 1, align='center')
password_checker.add(label_space, 8, 1, align='center')
password_checker.add(label_score, 9, 1, align='center')
password_checker.add(about_btn, 6, 2, align='center')

# About Window
about_window = gp.Window(app, 'About')
about_window.width = 300
about_message = gp.Label(about_window, 'Created by Finlay Punch for my Year 11 SEN Task 2 asessment. Made to solve the common cybersecurity issue of having a bad password')
about_window.set_grid(1, 1)
about_window.add(about_message, 1, 1)

help_window = gp.Window(app, 'Help')
help_message1 = gp.Label(help_window, '1. Type your password of choice into the text box in the password checker menu.')
help_message2 = gp.Label(help_window, '2. Click the enter button.')
help_message3 = gp.Label(help_window, '3. Five lines of text will appear, telling you what your password is, or isnt laking in.')
help_message4 = gp.Label(help_window, '4. The star at the bottom of the screen are your score, 5 is best.')
help_message5 = gp.Label(help_window, '5. When you get a score of 5, you can copy your password to clipboard.')
help_window.set_grid(5, 1)
help_window.add(help_message1, 1, 1)
help_window.add(help_message2, 2, 1)
help_window.add(help_message3, 3, 1)
help_window.add(help_message4, 4, 1)
help_window.add(help_message5, 5, 1)

app.on_close(check_exit)

main_window.show()
password_checker.hide()  # Ensure the password checker window is hidden initially
app.run()