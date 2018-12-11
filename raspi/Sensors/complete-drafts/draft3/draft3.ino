/*
  Aim : To gather data such as temperature, speed, battery voltage and current.
      : Send data from solar car to the chase vehicle

      Changes from draft2:
      + Used hardware serial parsing instead of software serial parsing (Recommended in GPS datasheet)
      + Supports only Arduino Mega and Leonardo because cannot use interrupts 
*/

// ==================================DHT Sensor===================================
#include "DHT.h"
#define DHTPIN 31     // what digital pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302), AM2321

// Connect pin 1 (on the left) of the sensor to +5V
// NOTE: If using a board with 3.3V logic like an Arduino Due connect pin 1
// to 3.3V instead of 5V!
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

// Initialize DHT sensor.
// Note that older versions of this library took an optional third parameter to
// tweak the timings for faster processors.  This parameter is no longer needed
// as the current DHT reading algorithm adjusts itself to work on faster procs.
DHT dht(DHTPIN, DHTTYPE);
// ================================================================================


// ==================================GPS-Speed==================================
#include <Adafruit_GPS.h>

// what's the name of the hardware serial port?
#define GPSSerial Serial1

// Connect to the GPS on the hardware port
Adafruit_GPS GPS(&GPSSerial);

// Set GPSECHO to 'false' to turn off echoing the GPS data to the Serial console
// Set to 'true' if you want to debug and listen to the raw GPS sentences
#define GPSECHO false

uint32_t timer = millis();
// =============================================================================


// ==================================Battery==================================
# define battery_pin A8
// ===========================================================================

// ==================================Current==================================
# define current_pin_1 A9
# define current_pin_2 A10
# define current_pin_3 A11
# define current_pin_4 A12
# define current_pin_5 A13

// constants won't change. Used here to set a pin number:
const int current_power_supply_pin_1 =  24; // the number of the current_power_supply_pin_1 pin
const int current_power_supply_pin_2 =  26; // the number of the current_power_supply_pin_2 pin
const int current_power_supply_pin_3 =  28; // the number of the current_power_supply_pin_3 pin
const int current_power_supply_pin_4 =  30; // the number of the current_power_supply_pin_4 pin
const int current_power_supply_pin_5 =  32; // the number of the current_power_supply_pin_5 pin
// ===========================================================================

// lambda declarations
float collect_temperature();
float collect_speed();
float collect_battery();

float collect_current_sensor_1();
float collect_current_sensor_2();
float collect_current_sensor_3();
float collect_current_sensor_4();
float collect_current_sensor_5();

void setup() {
  Serial.begin(9600);

  // ============================DHT 22==============================================
  dht.begin();
  // ============================End of DHT 22=======================================


  // ============================Ultimate GPS shield==================================
  
  //while (!Serial);  // uncomment to have the sketch wait until Serial is ready

  // connect at 115200 so we can read the GPS fast enough and echo without dropping chars
  // also spit it out
  // Serial.begin(9600);
  // Serial.println("Adafruit GPS library basic test!");

  // 9600 NMEA is the default baud rate for Adafruit MTK GPS's- some use 4800
  GPS.begin(9600);
  // uncomment this line to turn on RMC (recommended minimum) and GGA (fix data) including altitude
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  // uncomment this line to turn on only the "minimum recommended" data
  //GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCONLY);
  // For parsing data, we don't suggest using anything but either RMC only or RMC+GGA since
  // the parser doesn't care about other sentences at this time
  // Set the update rate
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ); // 1 Hz update rate
  // For the parsing code to work nicely and have time to sort thru the data, and
  // print it out we don't suggest using anything higher than 1 Hz

  // Request updates on antenna status, comment out to keep quiet
  GPS.sendCommand(PGCMD_ANTENNA);

  delay(1000);

  // Ask for firmware version
  // GPSSerial.println(PMTK_Q_RELEASE);
  
  // =======================End of Ultimate GPS shield==================================

  // ===================Battery=========================================================

  // ===================End of Battery==================================================

  // ===================Current=========================================================
  // set the digital pin as output:
  pinMode(current_power_supply_pin_1, OUTPUT);
  pinMode(current_power_supply_pin_2, OUTPUT);
  pinMode(current_power_supply_pin_3, OUTPUT);
  pinMode(current_power_supply_pin_4, OUTPUT);
  pinMode(current_power_supply_pin_5, OUTPUT);
  // ===================End of Current=========================================================

}

void loop() {

  digitalWrite(current_power_supply_pin_1, HIGH);
  digitalWrite(current_power_supply_pin_2, HIGH);
  digitalWrite(current_power_supply_pin_3, HIGH);
  digitalWrite(current_power_supply_pin_4, HIGH);
  digitalWrite(current_power_supply_pin_5, HIGH);

  //  testing purposes
  //  float temperature_value = 25;
  //  float speedometer_value = 100;
  //  float battery_value = 75;
  //  float current_value_1 = 0.10;
  //  float current_value_2 = 0.20;
  //  float current_value_3 = 0.30;
  //  float current_value_4 = 0.40;
  //  float current_value_5 = 0.50;

  float temperature_value = collect_temperature();
  float speedometer_value = collect_speed();
  float battery_value = collect_battery();

  float current_value_1 = collect_current_sensor_1();
  float current_value_2 = collect_current_sensor_2();
  float current_value_3 = collect_current_sensor_3();
  float current_value_4 = collect_current_sensor_4();
  float current_value_5 = collect_current_sensor_5();

  Serial.print("DATA");
  Serial.print(",");
  Serial.print("TIME");
  Serial.print(",");
  Serial.print(temperature_value);
  Serial.print(",");
  Serial.print(speedometer_value);
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

}

float collect_temperature() {
  // Wait a few seconds between measurements.
  delay(250);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  // float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(t)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  return (t);
}

float collect_speed() {

  // read data from the GPS in the 'main loop'
  char c = GPS.read();
  // if you want to debug, this is a good time to do it!
  if (GPSECHO)
    if (c) Serial.print(c);
  // if a sentence is received, we can check the checksum, parse it...
  if (GPS.newNMEAreceived()) {
    // a tricky thing here is if we print the NMEA sentence, or data
    // we end up not listening and catching other sentences!
    // so be very wary if using OUTPUT_ALLDATA and trytng to print out data
    // Serial.println(GPS.lastNMEA()); // this also sets the newNMEAreceived() flag to false
    if (!GPS.parse(GPS.lastNMEA())) // this also sets the newNMEAreceived() flag to false
      return; // we can fail to parse a sentence in which case we should just wait for another
  }
  // if millis() or timer wraps around, we'll just reset it
  if (timer > millis()) timer = millis();

  // approximately every 2 seconds or so, print out the current stats
  if (millis() - timer > 2000) {
    timer = millis(); // reset the timer

    // Serial.print("\nTime: ");
    // Serial.print(GPS.hour, DEC); Serial.print(':');
    // Serial.print(GPS.minute, DEC); Serial.print(':');
    // Serial.print(GPS.seconds, DEC); Serial.print('.');
    // Serial.println(GPS.milliseconds);
    // Serial.print("Date: ");
    // Serial.print(GPS.day, DEC); Serial.print('/');
    // Serial.print(GPS.month, DEC); Serial.print("/20");
    // Serial.println(GPS.year, DEC);
    // Serial.print("Fix: "); Serial.print((int)GPS.fix);
    // Serial.print(" quality: "); Serial.println((int)GPS.fixquality);
    if (GPS.fix) {
      // Serial.print("Location: ");
      // Serial.print(GPS.latitude, 4); Serial.print(GPS.lat);
      // Serial.print(", ");
      // Serial.print(GPS.longitude, 4); Serial.println(GPS.lon);
      // Serial.print("Speed (knots): ");
      return (GPS.speed * 1.852);
      // Serial.print("Angle: "); Serial.println(GPS.angle);
      // Serial.print("Altitude: "); Serial.println(GPS.altitude);
      // Serial.print("Satellites: "); Serial.println((int)GPS.satellites);
    }
  }
}

float collect_battery() {
  // read the input on analog pin 0:
  //  float batteryValue = analogRead(batteryPin); // Read OUTPUT = 0 V to 5 V.
  //  float value = (batteryValue / 1023) * 5; //
  //  float realValue = value * 30;

  return (((analogRead(battery_pin) / 1023) * 5) * 30);
}

float collect_current_sensor_1() {
  delay(5);
  float output_voltage_value_1 = analogRead(current_pin_1) * (5.0 / 1023.0);
  float current_value_1 = (output_voltage_value_1 - (5.0 / 2.0)) / 0.037;
  return current_value_1;
}

float collect_current_sensor_2() {

}

float collect_current_sensor_3() {

}

float collect_current_sensor_4() {

}

float collect_current_sensor_5() {

}
