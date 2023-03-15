# Fall detection Wearable With TinyML
This repository contains the necessary files for building a fall detection wearable device. It includes TensorFlow Lite models, a model.h5 file, and Arduino sketch files.

# Requirements
To build and use the fall detection wearable device, you will need the following:

An Arduino board (e.g., Arduino Uno, Nano, or Mega)
An accelerometer sensor (e.g., ADXL345 or MPU6050)
A computer with the Arduino IDE installed
A micro-USB cable
TensorFlow Lite Library installed in Arduino IDE
Python (optional)

#Installation

Clone this repository or download the zip file.
Open the Arduino IDE and install the TensorFlow Lite library.
Connect the accelerometer sensor to the Arduino board. Refer to the Arduino sketch files to determine the wiring configuration.
Upload the appropriate sketch file to the Arduino board. There are two sketch files in the repository: "Fall_Detection_Serial" and "Fall_Detection_BLE". The "Fall_Detection_Serial" sketch sends the fall detection results to the computer over serial communication. The "Fall_Detection_BLE" sketch sends the results to a Bluetooth Low Energy (BLE) module.
Open the appropriate Python script for visualizing the fall detection results on the computer. "Fall_Detection_Serial_Visualization.py" is used for the "Fall_Detection_Serial" sketch, while "Fall_Detection_BLE_Visualization.py" is used for the "Fall_Detection_BLE" sketch. Make sure to modify the serial port or BLE address in the Python script to match your setup.
Compile the TensorFlow Lite model using the provided script. The script is named "Compile_TFLite_Model.py". This script will generate a ".tflite" file that can be uploaded to the Arduino board.
Usage
To use the fall detection wearable device, follow these steps:

Wear the device in the desired location.
Turn on the device by pressing the reset button on the Arduino board.
Wait for the device to start sending fall detection results to the computer.
Monitor the fall detection results on the computer using the appropriate Python script.
Conclusion
With the files provided in this repository, you can easily build a fall detection wearable device using an Arduino board and an accelerometer sensor. By analyzing sensor data with machine learning algorithms, the device can accurately detect when a user has fallen down.
