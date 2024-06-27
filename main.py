import gooeypie as gp

# Special characters to check against in the password
special_characters = "!@#$%^&*()-+?_=,<>/'"
import pyperclip

# Load common words from the common_words text file
def load_common_words(file_path):
    with open(file_path, 'r') as file:
        common_words = file.read().splitlines()
    return common_words

# Check if the password is in the list of common words
def is_common_word(word, common_words):
    return word in common_words

# Toggle the visibility of the password
def toggle_mask(event):
    secret.toggle()

# Load common words
common_words = load_common_words('common_words.txt')

# Function to handle password evaluation and feedback
def on_text_change(event):
    text = secret.text
    print(text)
    s = text
    score = 0

    # Check if the password is a common word
    if is_common_word(text, common_words):
        label.text = "Common password/word. ☆"
        label.font_weight = 'bold'
    else:
        label.text = "Not a common password/word. ★"
        score += 1
        label.font_weight = 'normal'

    # Check for numeric, alphabetic, and alphanumeric content
    if text.isdigit():
        label_num.text = "It is just numbers, try to put some letters in it as well. ☆"
        label_num.font_weight = 'bold'
    elif text.isalpha():
        label_num.text = "Try to have a combination of letters and numbers. ☆"
        label_num.font_weight = 'bold'
    elif any(c.isdigit() for c in text) and any(c.isalpha() for c in text):
        label_num.text = "It has a combination of letters and numbers, good. ★"
        score += 1
        label_num.font_weight = 'normal'
    else:
        label_num.text = "Try to have a combination of letters and numbers. ☆"
        label_num.font_weight = 'bold'

    # Check password length
    if len(text) == 0:
        label_length.text = "Nothing entered"    
    if len(text) >= 1:
        label_length.text = "It is less than 10 letters long, try making it longer. ☆"
        label_length.font_weight = 'bold'
    if len(text) >= 10:
        label_length.text = "It is 10 or more letters long, try making it a bit longer.☆"
        label_length.font_weight = 'bold'
    if len(text) >= 15:
        label_length.text = "It is 15 or more letters long, thats a good length. ★"
        score += 1
        label_length.font_weight = 'normal'

    # Check for special characters
    if any(c in special_characters for c in s):
        label_special.text = "Your password has special characters in it ★"
        score += 1
        label_special.font_weight = 'normal'
    else:
        label_special.text = "Try to include some special characters in it (e.g. !, #, $) ☆"
        label_special.font_weight = 'bold'

    # Check for spaces
    if ' ' in text:
        label_space.text = "Having a space in it is good ★"
        score += 1
        label_space.font_weight = 'normal'
    else:
        label_space.text = "Try putting a space in it ☆"
        label_space.font_weight = 'bold'

    # Display score in the form of stars
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

# Copy password to clipboard
def copy_password(event):
    pyperclip.copy(secret.text)
    app.alert('Success', 'Password copied to clipboard')

# Open the About window
def open_about_window(event):
    about_window.show()

# Open the Help window
def open_help_window(event):
    help_window.show()

# Confirm before exiting the application
def check_exit():
    ok_to_exit = app.confirm_yesno(None, 'Are you sure you want to close?', 'question')
    return ok_to_exit

# Open the Password Checker window
def open_password_checker(event):
    password_checker.show()

# Create main application
app = gp.GooeyPieApp('Password Checker')

# Set application icon
app.set_icon('fees.PNG')

# Main Window setup
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
# Creates the syles within the main window
main_title.font_name = 'Segoe UI Black'
main_title.color = 'Blue'
main_label1.color = 'Royal Blue'
main_label2.color = 'Royal Blue'
main_label3.color = 'Royal Blue'
main_label1.font_weight = 'bold'
main_label2.font_weight = 'bold'
main_label3.font_weight = 'bold'

# Create the structure of the Main Window
main_window.set_grid(5, 3)
main_window.add(main_title, 1, 2, align ='center')
main_window.add(main_label1, 2, 2, align ='center')
main_window.add(main_label2, 3, 2, align ='center')
main_window.add(main_label3, 4, 2, align ='center')
main_window.add(main_button, 5, 2, align ='center')
main_window.add(about_btn, 5, 3, align='center')
main_window.add(help_btn, 5, 1, align='center')

# Password Checker Window setup
password_checker = gp.Window(app, 'Password Checker')
question = gp.Label(password_checker, "Type in your password")

secret = gp.Secret(password_checker)
secret.width = 50

check = gp.Checkbox(password_checker, 'Reveal Password')
check.add_event_listener('change', toggle_mask)

#Used in conjunction with previous code to make the related text either bold or normal.
label = gp.StyleLabel(password_checker, '...')
label_length = gp.StyleLabel(password_checker, '...')
label_num = gp.StyleLabel(password_checker, '...')
label_special = gp.StyleLabel(password_checker, '...')
label_space = gp.StyleLabel(password_checker, '...')
label_score = gp.StyleLabel(password_checker, '...')

enter_btn = gp.Button(password_checker, 'Enter', on_text_change)
copy_button = gp.Button(password_checker, 'Copy?', copy_password)

# Create the structure of the password page
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

# About Window setup
about_window = gp.Window(app, 'About')
about_window.width = 300
about_message = gp.Label(about_window, 'Created by Finlay Punch for my Year 11 SEN Task 2 asessment. Made to solve the common cybersecurity issue of having a bad password')
about_window.set_grid(1, 1)
about_window.add(about_message, 1, 1)

# Help Window setup
help_window = gp.Window(app, 'Help')
help_message1 = gp.Label(help_window, '1. Type your password of choice into the text box in the password checker menu.')
help_message2 = gp.Label(help_window, '2. Click the enter button.')
help_message3 = gp.Label(help_window, '3. Five lines of text will appear, telling you what your password is, or isnt laking in.')
help_message4 = gp.Label(help_window, '4. The star at the bottom of the screen are your score, 5 is best.')
help_message5 = gp.Label(help_window, '5. You can copy you password at any given time.')

# Create the structure of the help window
help_window.set_grid(5, 1)
help_window.add(help_message1, 1, 1)
help_window.add(help_message2, 2, 1)
help_window.add(help_message3, 3, 1)
help_window.add(help_message4, 4, 1)
help_window.add(help_message5, 5, 1)

# Set up close confirmation
app.on_close(check_exit)

# Show main window and hide password checker initially
main_window.show()
password_checker.hide()

# Run the application
app.run()