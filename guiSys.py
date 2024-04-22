import PySimpleGUI as sg

# enuf for proof of concept to show kimbler how to use PySimpleGUI

# Define the function to process the input text
def process_input(input_text):
    # Your processing logic here
    # For demonstration purposes, let's just return the input text reversed
    return input_text[::-1]

# Define the layout
layout = [
    [sg.Text("Welcome to the Application!", font=("Helvetica", 14))],
    [sg.Text("Instructions:", font=("Helvetica", 12))],
    [sg.Text("1. Enter your input in the text box.", font=("Helvetica", 12))],
    [sg.Text("2. Click on the 'Process' button to run the code.", font=("Helvetica", 12))],
    [sg.Text("3. The output will be displayed below.", font=("Helvetica", 12))],
    [sg.Multiline(size=(60, 10), key="-INPUT-", font=("Helvetica", 12))],
    [sg.Button("Process", font=("Helvetica", 12)), sg.Button("Exit", font=("Helvetica", 12))],
    [sg.Text("Output:", font=("Helvetica", 12))],
    [sg.Output(size=(60, 10), font=("Helvetica", 12))]
]

# Create the window
window = sg.Window("PySimpleGUI Application", layout, resizable=True)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    if event == "Process":
        input_text = values["-INPUT-"]
        # Call the process_input function with the input text
        output_text = process_input(input_text)
        # Print the output to the Output element
        print(output_text)

# Close the window
window.close()
