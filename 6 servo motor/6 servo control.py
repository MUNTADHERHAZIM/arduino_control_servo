import serial
import tkinter as tk

# Define the serial port (change this to match your Arduino's port)
ser = serial.Serial('COM3', 9600, timeout=1)

def set_servo_positions():
    positions = [servo_sliders[i].get() for i in range(6)]
    
    # Send servo positions separated by spaces and followed by a newline character
    position_str = ' '.join(map(str, positions)) + '\n'
    ser.write(position_str.encode())
    
    feedback_label.config(text=f'Set Positions: {positions}')

# Create the main window
window = tk.Tk()
window.title("Servo Motor Control")

# Create servo sliders
servo_sliders = []
for i in range(6):
    servo_slider = tk.Scale(window, from_=0, to=180, orient=tk.HORIZONTAL, label=f"Servo {i+1} Position")
    servo_slider.pack()
    servo_sliders.append(servo_slider)

# Create a button to set the servo positions
set_position_button = tk.Button(window, text="Set Positions", command=set_servo_positions)
set_position_button.pack()

# Create a label to display feedback
feedback_label = tk.Label(window, text="")
feedback_label.pack()

# Start the Tkinter main loop
window.mainloop()

# Close the serial port when the application is closed
ser.close()
