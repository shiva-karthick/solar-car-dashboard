/*    Lattepanda version
      1 GPS sensor -> leo_parsing.ino
      1 Temperature Sensor -> DHTtester.ino
      1 Battery Sensor
      5 Current Sensors
  Aim : To gather data such as temperature, speed, battery voltage and current.
      : Send data from solar car to the chase vehicle

*/

// ==================================DHT Sensor===================================
#include "DHT.h"
#define DHTPIN 2     // what digital pin we're connected to
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
// Test code for Adafruit GPS modules using MTK3329/MTK3339 driver
//
// This code shows how to listen to the GPS module in an interrupt
// which allows the program to have more 'freedom' - just parse
// when a new NMEA sentence is available! Then access data when
// desired.
//
// Tested and works great with the Adafruit Ultimate GPS module
// using MTK33x9 chipset
//    ------> http://www.adafruit.com/products/746
// Pick one up today at the Adafruit electronics shop
// and help support open source hardware & software! -ada

//This code is intended for use with Arduino Leonardo and other ATmega32U4-based Arduinos

#include <Adafruit_GPS.h>
#include <SoftwareSerial.h>

// Connect the GPS Power pin to 5V
// Connect the GPS Ground pin to ground
// If using software serial (sketch example default):
//   Connect the GPS TX (transmit) pin to Digital 8
//   Connect the GPS RX (receive) pin to Digital 7
// If using hardware serial:
//   Connect the GPS TX (transmit) pin to Arduino RX1 (Digital 0)
//   Connect the GPS RX (receive) pin to matching TX1 (Digital 1)

// If using software serial, keep these lines enabled
// (you can change the pin numbers to match your wiring):
SoftwareSerial mySerial(8, 7);
Adafruit_GPS GPS(&mySerial);

// If using hardware serial, comment
// out the above two lines and enable these two lines instead:
//Adafruit_GPS GPS(&Serial1);
//HardwareSerial mySerial = Serial1;

// Set GPSECHO to 'false' to turn off echoing the GPS data to the Serial console
// Set to 'true' if you want to debug and listen to the raw GPS sentences
#define GPSECHO  false


uint32_t timer = millis();
// =============================================================================


// ==================================Battery==================================
# define battery_pin A0
// ===========================================================================

// ==================================Current==================================
# define current_pin_1 A1
# define current_pin_2 A2
# define current_pin_3 A3
# define current_pin_4 A4
# define current_pin_5 A5
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
  Serial1.begin(9600);
  // ============================DHT 22==============================================
  dht.begin();
  // ============================End of DHT 22=======================================


  // ============================Ultimate GPS shield==================================

  // connect at 115200 so we can read the GPS fast enough and echo without dropping chars
  // also spit it out
  //  Serial.begin(115200);
  delay(5000);
  //  Serial.println("Adafruit GPS library basic test!");

  // 9600 NMEA is the default baud rate for Adafruit MTK GPS's- some use 4800
  GPS.begin(9600);

  // uncomment this line to turn on RMC (recommended minimum) and GGA (fix data) including altitude
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  // uncomment this line to turn on only the "minimum recommended" data
  //GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCONLY);
  // For parsing data, we don't suggest using anything but either RMC only or RMC+GGA since
  // the parser doesn't care about other sentences at this time

  // Set the update rate
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);   // 1 Hz update rate
  // For the parsing code to work nicely and have time to sort thru the data, and
  // print it out we don't suggest using anything higher than 1 Hz

  // Request updates on antenna status, comment out to keep quiet
  GPS.sendCommand(PGCMD_ANTENNA);

  delay(1000);
  // Ask for firmware version
  //  mySerial.println(PMTK_Q_RELEASE);

  // =======================End of Ultimate GPS shield==================================

  // ===================Battery=========================================================

  // ===================End of Battery==================================================

  // ===================Current=========================================================

  // ===================End of Current=========================================================

}

void loop() {
  delay(500);
  //  testing purposes
  //  float temperature_value = 25;
  float speedometer_value = 100;
  float battery_value = 75;
  float current_value_1 = 0.10;
  float current_value_2 = 0.20;
  float current_value_3 = 0.30;
  float current_value_4 = 0.40;
  float current_value_5 = 0.50;

  float temperature_value = collect_temperature();
  //  float speedometer_value = collect_speed();
  //  float battery_value = collect_battery();

  //  float current_value_1 = collect_current_sensor_1();
  //  float current_value_2 = collect_current_sensor_2();
  //  float current_value_3 = collect_current_sensor_3();
  //  float current_value_4 = collect_current_sensor_4();
  //  float current_value_5 = collect_current_sensor_5();

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

  Serial1.print("DATA");
  Serial1.print(",");
  Serial1.print("TIME");
  Serial1.print(",");
  Serial1.print(temperature_value);
  Serial1.print(",");
  Serial1.print(speedometer_value);
  Serial1.print(",");
  Serial1.print(battery_value);
  Serial1.print(",");
  Serial1.print(current_value_1);
  Serial1.print(",");
  Serial1.print(current_value_2);
  Serial1.print(",");
  Serial1.print(current_value_3);
  Serial1.print(",");
  Serial1.print(current_value_4);
  Serial1.print(",");
  Serial1.println(current_value_5);

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
  char c = GPS.read();
  // if you want to debug, this is a good time to do it!
  if ((c) && (GPSECHO))
    Serial.write(c);

  // if a sentence is received, we can check the checksum, parse it...
  if (GPS.newNMEAreceived()) {
    // a tricky thing here is if we print the NMEA sentence, or data
    // we end up not listening and catching other sentences!
    // so be very wary if using OUTPUT_ALLDATA and trytng to print out data
    //Serial.println(GPS.lastNMEA());   // this also sets the newNMEAreceived() flag to false

    if (!GPS.parse(GPS.lastNMEA()))   // this also sets the newNMEAreceived() flag to false
      return;  // we can fail to parse a sentence in which case we should just wait for another
  }

  // if millis() or timer wraps around, we'll just reset it
  if (timer > millis())  timer = millis();

  // approximately every 2 seconds or so, print out the current stats
  if (millis() - timer > 2000) {
    timer = millis(); // reset the timer

    //    Serial.print("\nTime: ");
    //    Serial.print(GPS.hour, DEC); Serial.print(':');
    //    Serial.print(GPS.minute, DEC); Serial.print(':');
    //    Serial.print(GPS.seconds, DEC); Serial.print('.');
    //    Serial.println(GPS.milliseconds);
    //    Serial.print("Date: ");
    //    Serial.print(GPS.day, DEC); Serial.print('/');
    //    Serial.print(GPS.month, DEC); Serial.print("/20");
    //    Serial.println(GPS.year, DEC);
    //    Serial.print("Fix: "); Serial.print((int)GPS.fix);
    //    Serial.print(" quality: "); Serial.println((int)GPS.fixquality);
    if (GPS.fix) {
      //      Serial.print("Location: ");
      //      Serial.print(GPS.latitude, 4); Serial.print(GPS.lat);
      //      Serial.print(", ");
      //      Serial.print(GPS.longitude, 4); Serial.println(GPS.lon);

      //      Serial.print("Speed (knots): ");
      return (GPS.speed * 1.852);
      //      Serial.print("Angle: "); Serial.println(GPS.angle);
      //      Serial.print("Altitude: "); Serial.println(GPS.altitude);
      //      Serial.print("Satellites: "); Serial.println((int)GPS.satellites);
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
