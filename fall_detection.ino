
#include <Arduino_LSM9DS1.h>
#include <TensorFlowLite.h>

// Set the input and output tensor sizes
constexpr int kTensorSize = 6;  // 3 axes * 2 bytes per axis
constexpr int kNumResults = 2;  // "fall" or "not fall"

// Define the input and output tensor arrays
float input_tensor_data[kTensorSize];
float output_tensor_data[kNumResults];

// Load the TFLite model
const tflite::Model* model = tflite::GetModel(falldetection_tflite);
tflite::MicroInterpreter interpreter(model->operator(), tflite::MicroOpResolver<5>::Get(), tensor_arena, kTensorArenaSize, error_reporter);
interpreter.AllocateTensors();

// Get pointers to the input and output tensors
TfLiteTensor* input_tensor = interpreter.input(0);
TfLiteTensor* output_tensor = interpreter.output(0);

void setup() {
  // Initialize the serial monitor
  Serial.begin(9600);

  // Initialize the accelerometer
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}

void loop() {
  // Read the accelerometer data
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(input_tensor_data[0], input_tensor_data[1], input_tensor_data[2]);

    // Run the inference on the input tensor
    interpreter.Invoke();

    // Get the output tensor values
    float fall_probability = output_tensor_data[0];
    float not_fall_probability = output_tensor_data[1];

    // Print the results on the serial monitor
    Serial.print("Fall probability: ");
    Serial.print(fall_probability);
    Serial.print(", Not fall probability: ");
    Serial.println(not_fall_probability);
  }
}
