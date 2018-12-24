# Project Ideas for a tachometer

## Bill of Materials

|       Name        | Quantity | Cost of 1 item | Total Cost | Product Link | Have you bough this item? |
| :---------------: | :------: | :------------: | :--------: | :----------: | :-----------------------: |
|    Hall sensor    |    1     |                |            |              |            yes            |
| neodymium magnet  |    1     |                |            |              |            yes            |
| IR Sensor Modules |    1     |                |            |              |            yes            |

---

> For the speed sensor, use a Hall sensor and 2 magnets, and connect the Hall sensor to one of the Arduino inputs that provides an interrupt. It's easier to measure the RPM using an interrupt.

Brief Description of Sensor modules:

- A Hall sensor is a device which can detect the presence of a magnet based on its polarity. We stick a small piece of magnet on the wheel and place the hall sensor near it in such a way that every time the wheel rotates the hall sensor detects it. We then use the help of timers and Interrupts on our PIC Microcontroller to calculate the time taken for one complete rotation of the wheel.

Note: Hall sensor have polarities, so make sure which pole it is detecting and place it accordingly.
Also make sure you use a Pull-up resistor with the output pin of the hall sensor.

- second
- third

---

**Digital Speedometer By Narendra Wadhwani**

[electronicsforu](https://electronicsforu.com/electronics-projects/hardware-diy/digital-speedometer)

Description :
This digital speedometer displays the speed of the vehicle in kmph. An opaque disc is mounted on the spindle attached to the front wheel of the vehicle. The disc has ten equidistant holes on its periphery. On one side of the disc an infrared LED is fixed and on the opposite side of the disc, in line with the IR LED, a phototransistor is mounted. IC LM324 is wired as a comparator.

**Digital Speedometer and Odometer Circuit using PIC Microcontroller By Aswinth Raj Jul 27, 2017**

[Circuit Digest](https://circuitdigest.com/microcontroller-projects/digital-speedometer-odometer-circuit-using-pic16f877a)

Description :
Measuring the speed/rpm of a Vehicle or a motor has always been a fascinating project for us to try. So, in this project we are going to build one using the Industrial ready PIC microcontrollers. We will use a piece of magnet and a Hall Sensor to measure the speed. There are other ways/sensors to measure the speed but, using a hall sensor is cheap and also can be used on any type of motor/Vehicle. By doing this project we will also enhance our skills in learning PIC16F877A since the project involves the use of Interrupts and Timers. At, the end of this project you will be able to calculate the speed and distances covered by any rotating object and display them on a 16x2 LCD screen. Lets start with this Digital Speedometer and Odometer Circuit with PIC.

**Arduino Tachometer with Magnetic Hall Sensor**

[Using a Hall Effect Sensor (A3144) to Measure Rotations from a Fan](https://engineersportal.com/blog/2018/10/3/arduino-tachometer-using-a-hall-effect-sensor-to-measure-rotations-from-a-fan)

Description :

In engineering, a tachometer is a useful tool for calculating the rotational motion of a part. Tachometers read out revolutions per minute (RPM), which tells the user how often a rotating part completes one full rotation. RPM readings are used in the automotive, aerospace, and manufacturing fields. Tachometers are important for determining relationships between fuel consumption and motor speed, safety of moving parts, and even wind speed indicators. Some tachometers are laser-based, but they can be material and color-dependent and even inaccurate under specific lighting conditions. In this experiment and tutorial, I will demonstrate how to build an inexpensive,reliable hall effect tachometer that attaches a neodymium magnet to a rotating shaft of a DC fan. The speed of fans is important because they are proportional to the amount of cooling supplied to a system, and without an accurate depiction of fan speed - cooling systems can malfunction, resulting in large loss of mechanical and industrial equipment.

- [How can I determine the rpm of a wheel that's spinning really fast?](https://physics.stackexchange.com/questions/353795/how-can-i-determine-the-rpm-of-a-wheel-thats-spinning-really-fast?newreg=7558a06958ee4828b47d5781f32262a5)

---

# All Web Links for tachometer :

- [Arduino Bike Speedometer With 128 X 64 Graphics LCD: 5 Steps (with Pictures)](https://www.instructables.com/id/Arduino-Bike-Speedometer-With-128-X-64-Graphics-LC/)
- [Digital Multimeter for Your Car: 5 Steps](https://www.instructables.com/id/Digital-multimeter-for-your-car/)
- [LED Speedometer: 3 Steps](https://www.instructables.com/id/LED-Speedometer/)
- [DIY SPEEDOMETER AND ODOMETER: 6 Steps (with Pictures)](https://www.instructables.com/id/DIY-SPEEDOMETER-AND-ODOMETER/)
- [How do speedometers work? - Explain that Stuff](https://www.explainthatstuff.com/how-speedometer-works.html)
- [How Hall effect sensors work - Explain that Stuff](https://www.explainthatstuff.com/hall-effect-sensors.html)
- [Arduino suitable for motorcycle hour-meter/electric tach drive/speedometer?](https://forum.arduino.cc/index.php?topic=138333.0)
- [Arduino Based Analog Speedometer Using IR Sensor](https://circuitdigest.com/microcontroller-projects/arduino-analog-speedometer-using-ir-sensor)
- [Infrared Tachometer Using Arduino: 4 Steps (with Pictures)](https://www.instructables.com/id/Infrared-Tachometer-using-Arduino/)
- [Add an Arduino-based Optical Tachometer to a CNC Router: 34 Steps (with Pictures)](https://www.instructables.com/id/Add-an-Arduino-based-Optical-Tachometer-to-a-CNC-R/)
- [Measure RPM - Optical Tachometer : 10 Steps (with Pictures)](https://www.instructables.com/id/Measure-RPM-DIY-Portable-Digital-Tachometer/)
- [Arduino Tachometer - Using a Hall Effect Sensor (A3144) to Measure Rotations from a Fan — Engineer's Maker Portal](https://engineersportal.com/blog/2018/10/3/arduino-tachometer-using-a-hall-effect-sensor-to-measure-rotations-from-a-fan)
- [Arduino 5 Minute Tutorials: Lesson | RobotShop Community](https://www.robotshop.com/community/tutorials/show/arduino-5-minute-tutorials-lesson-7-accelerometers-gyros-imus)
- [Digital Speedometer and Odometer Circuit using PIC Microcontroller](https://circuitdigest.com/microcontroller-projects/digital-speedometer-odometer-circuit-using-pic16f877a)
- [(1) DIY bike speedometer Arduino - YouTube](https://www.youtube.com/watch?v=1ycA7TFV4t4)
- [Digital Speedometer | Detailed Project with Circuit Diagram](https://electronicsforu.com/electronics-projects/hardware-diy/digital-speedometer)
- [How can I determine the rpm of a wheel that's spinning really fast?](https://physics.stackexchange.com/questions/353795/how-can-i-determine-the-rpm-of-a-wheel-thats-spinning-really-fast?newreg=7558a06958ee4828b47d5781f32262a5)
