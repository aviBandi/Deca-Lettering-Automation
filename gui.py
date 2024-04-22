import PySimpleGUI as sg


def process_text(input_text):
    # Process the text (for demonstration, just echoing the input)
    processed_text = input_text

    # Update the output box with processed text
    window['-OUTPUT-'].update(processed_text)


# Define the layout of the GUI
layout = [
    [sg.Text("Enter text:")],
    [sg.Multiline(size=(50, 10), key='-INPUT-')],
    [sg.Button("Process Text", key='-PROCESS-')],
    [sg.Text("Output:")],
    [sg.Output(size=(50, 10), key='-OUTPUT-')],
]

# Create the GUI window
window = sg.Window("Text Processor", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == '-PROCESS-':
        input_text = values['-INPUT-']
        process_text(input_text)

# Close the window
window.close()
