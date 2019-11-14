# RPi_ADC0832_Temperature

Python library and example code to read temprature with Raspberry Pi, ADC0932 and Analog Temperature Sensor (from Sunfounder)

## Installation

To install and test this code run this commands on your Rasperry Pi :

```bash
git clone https://github.com/AxVultis/RPi_ADC0832_Temperature
cd RPi_ADC0832_Temperature
python3 read_temperature.py
```

## Wiring

GPIO18 --> ADC0832 CLK

GPIO27 --> ADC0832 IO

GPIO17 --> ADC0832 CS

GND --> ADC0832 GND | Analog sensor GND

3V3 --> ADC0832 VCC  | Analog sensor VCC

ADC0832 CH0 --> Analog sensor A0

## Links

Sunfounder test code for ADC0832 http://wiki.sunfounder.cc/images/a/a9/ADC0832_Test_Code_for_Raspberry_Pi.zip

Sunfounder test code for Analog Temperature Sensor https://www.sunfounder.com/learn/Sensor-Kit-v1-0-for-Raspberry-Pi/lesson-10-analog-temperature-sensor-sensor-kit-v1-0-for-pi.html
