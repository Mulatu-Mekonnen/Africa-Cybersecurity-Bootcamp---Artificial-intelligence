import PySimpleGUI as sg
import random

# Function to generate a new random number between 0 and 15
def generate_new_number():
    return random.randint(0, 15)

# Generate the first random number
target_number = generate_new_number()

# Layout for the GUI
layout = [
    [sg.Text("Guess the Number Game", font=("Arial", 18))],
    [sg.Text("Guess a number between 0 and 15")],
    [sg.InputText("", key="guess", size=(5, 1), justification='center')],
    [sg.Button("Check Guess"), sg.Button("Replay Game", visible=False, key="replay")],
    [sg.Text("", size=(30, 1), key="result", font=("Arial", 14))],
]

# Create the window
window = sg.Window("Guess the Number", layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Check Guess":
        try:
            guess = int(values["guess"])

            if guess < target_number:
                result_text = f"Too low! The correct number was {target_number}. Try again."
            elif guess > target_number:
                result_text = f"Too high! The correct number was {target_number}. Try again."
            else:
                result_text = f"Correct! The number was {target_number}. You've guessed the number!"
                window["replay"].update(visible=True)  # Show the replay button after a correct guess
                window["Check Guess"].update(disabled=True)  # Disable the check button after correct guess

            window["result"].update(result_text)
        except ValueError:
            window["result"].update("Please enter a valid number.")

    elif event == "Replay Game":
        target_number = generate_new_number()  # Generate a new random number
        window["result"].update("")
        window["guess"].update("")
        window["Check Guess"].update(disabled=False)  # Enable the check button again
        window["replay"].update(visible=False)  # Hide the replay button

# Close the window
window.close()
