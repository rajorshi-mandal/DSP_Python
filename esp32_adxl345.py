import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Serial port configuration (change the port and baud rate as per your ESP32 setup)
SERIAL_PORT = '/dev/ttyACM0'  # Change to the appropriate serial port (e.g., '/dev/ttyUSB0' on Linux)
BAUD_RATE = 9600

# Initialize serial communication
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Create lists to store data
x_values = []
y_values = []
z_values = []

# Create a function to update the plot
def update_plot(frame):
    try:
        # Read a line from the serial port and split it into x, y, and z values
        line = ser.readline().decode().strip().split(',')
        if len(line) == 3:
            x, y, z = map(float, line)
            x_values.append(x)
            y_values.append(y)
            z_values.append(z)
            # Plot the data
            plt.cla()  # Clear the previous plot
            plt.plot(x_values, label='X')
            plt.plot(y_values, label='Y')
            plt.plot(z_values, label='Z')
            plt.xlabel('Time')
            plt.ylabel('Acceleration (m/s^2)')
            plt.legend()
            plt.title('ADXL345 Acceleration Data')
    except ValueError:
        pass

# Set up the plot
plt.ion()  # Turn on interactive mode for live plotting
fig, ax = plt.subplots()
plt.title('Real-time Acceleration Data from ADXL345')

# Create an animation to continuously update the plot
animation = FuncAnimation(fig, update_plot, interval=100)

try:
    # Display the animation and block until the user closes the plot
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)  # Adjust the top margin to show the title
    plt.show()
except KeyboardInterrupt:
    ser.close()  # Close the serial port on Ctrl+C

