// constants won't change. They're used here to set pin numbers:
const int buttonPin = 24;     // the number of the pushbutton pin

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status

float temperature = 0.0;
float speed_value = 0.0;
float battery = 0.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void loop() {
  delay(500);
  if (temperature <= 40 - 1) {
    temperature += 5;
  }
  else if (temperature >= 40) {
    temperature = 0;
  }

  if (speed_value <= 220 - 1) {
    speed_value += 20;
  }
  else if (speed_value >= 220) {
    speed_value = 0;
  }

  if (battery <= 140 - 1) {
    battery += 10;
  }
  else if (battery >= 140) {
    battery = 0;
  }

  // put your main code here, to run repeatedly:
  //  Serial.println( (String) "DATA,TIME,25,100,135,0.25"); // Works

  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    Serial.print("DATA");
    Serial.print(",");
    Serial.print("TIME");
    Serial.print(",");
    Serial.print(temperature);
    Serial.print(",");
    Serial.print(speed_value);
    Serial.print(",");
    Serial.print(battery);
    Serial.print(",");
    Serial.println(0.25);
  } else {
    // do nothing
  }

  //  Serial.print(100);
  //  Serial.print(",");
  //
  //  Serial.print(100);
  //  Serial.print(",");

  //  Serial.print(temperature);
  //  Serial.print(",");
  //
  //  // Simulate the speed from the GPS shield
  //  Serial.print(speed_value);
  //  Serial.print(",");
  //
  //  // Simulate the battery level
  //  Serial.print(battery);
  //  Serial.print(",");
  //
  //  Serial.println(100);
  
  delay(500);
}
