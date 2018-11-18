
// Pin numbers
//# define current_sensor_1 15
//# define current_sensor_2 11
//# define current_sensor_3 12
//# define current_sensor_4 13
//# define current_sensor_5 14
//# define voltage_sensor 15
//# define temperature_sensor_1 16

// constants won't change. They're used here to set pin numbers:
const int buttonPin = 7;     // the number of the pushbutton pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

float temperature_value = 0.0;
float speed_value = 0.0;
float battery_value = 0.0;
float current_value_1 = 0.0;
float current_value_2 = 0.0;
float current_value_3 = 0.0;
float current_value_4 = 0.0;
float current_value_5 = 0.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(500);

  if (temperature_value <= 40 - 1) {
    temperature_value += 5;
  }
  else if (temperature_value >= 40) {
    temperature_value = 0;
  }

  if (speed_value <= 220 - 1) {
    speed_value += 20;
  }
  else if (speed_value >= 220) {
    speed_value = 0;
  }

  if (battery_value <= 140 - 1) {
    battery_value += 10;
  }
  else if (battery_value >= 140) {
    battery_value = 0;
  }

  // put your main code here, to run repeatedly:
  //  Serial.println( (String) "DATA,TIME,25,100,135,0.25"); // Works

  float current_value_1 = 0.10;
  float current_value_2 = 0.20;
  float current_value_3 = 0.30;
  float current_value_4 = 0.40;
  float current_value_5 = 0.50;

  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    Serial.print("DATA");
    Serial.print(",");
    Serial.print("TIME");
    Serial.print(",");
    Serial.print(temperature_value);
    Serial.print(",");
    Serial.print(speed_value);
    Serial.print(",");
    Serial.print(battery_value);
    Serial.print(",");
    Serial.print(current_value_1);
    Serial.print(",");
    Serial.print(current_value_2);
    Serial.print(",");
    Serial.print(current_value_3);
    Serial.print(",");
    Serial.print(current_value_4);
    Serial.print(",");
    Serial.println(current_value_5);
  } else {
    // do nothing
  }
  delay(500);
}
