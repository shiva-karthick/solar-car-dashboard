float collect_gps();
float collect_temperature();
float collect_battery();

float speeed;
float temperature;
float battery;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  speeed = collect_gps();
  temperature = collect_temperature();
  battery = collect_battery();
  Serial.print(temperature);
  Serial.print(',');
  Serial.print(speeed);
  Serial.print(',');
  Serial.println(battery);
  delay(3000);
}

float collect_gps() {
  float speed_value = 220;
  return speed_value;
}

float collect_temperature() {
  float temperature = 30;
  return temperature;
}

float collect_battery() {
  float battery = 154;
  return battery;
}
