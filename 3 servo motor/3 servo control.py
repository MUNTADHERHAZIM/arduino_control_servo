import serial
import tkinter as tk

# Define the serial port (change this to match your Arduino's port)
ser = serial.Serial('COM3', 9600, timeout=1)

def set_servo_positions():
    position1 = servo1_slider.get()
    position2 = servo2_slider.get()
    position3 = servo3_slider.get()
    
    ser.write(f"{position1} {position2} {position3}".encode())
    
    feedback_label.config(text=f'Set Positions: Servo 1={position1}, Servo 2={position2}, Servo 3={position3}')

# Create the main window
window = tk.Tk()
window.title("Servo Motor Control")

# Create servo sliders
servo1_slider = tk.Scale(window, from_=0, to=180, orient=tk.HORIZONTAL, label="Servo 1 Position")
servo1_slider.pack()

servo2_slider = tk.Scale(window, from_=0, to=180, orient=tk.HORIZONTAL, label="Servo 2 Position")
servo2_slider.pack()

servo3_slider = tk.Scale(window, from_=0, to=180, orient=tk.HORIZONTAL, label="Servo 3 Position")
servo3_slider.pack()

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