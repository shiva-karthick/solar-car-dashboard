float temperature = 0.0;
float speed_value = 0.0;
float battery = 0.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  delay(1000);

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

  if (battery <= 134.4 - 1) {
    battery += 2;
  }
  else if (battery >= 134.4) {
    battery = 0;
  }


  // Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(",");

  // Simulate the speed from the GPS shield
  Serial.print(speed_value);
  Serial.print(",");

  // Simulate the battery level
  Serial.println(battery);
  delay(500);
}
