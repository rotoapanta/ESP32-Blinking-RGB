# <p align="center">ESP32 RGB Blinking

<p align="center">This project is based on an ESP32-S2 general-purpose development board with micropython that allows the rgb led to blink.</p>

##

![Python Version](https://img.shields.io/pypi/pyversions/3)
[![GitHub issues](https://img.shields.io/github/issues/rotoapanta/ESP32-Blinking-RGB-Led
)](https://github.com/rotoapanta/ESP32-Blinking-RGB-Led/issues)
![GitHub repo size](https://img.shields.io/github/repo-size/rotoapanta/ESP32-Blinking-RGB-Led
)
![GitHub last commit](https://img.shields.io/github/last-commit/rotoapanta/ESP32-Blinking-RGB-Led
)
![GitHub commit merge status](https://img.shields.io/github/commit-status/rotoapanta/prueba2/main/6a500cc65d)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Discord](https://img.shields.io/discord/996422496842694726)
[![Discord Invite](https://img.shields.io/badge/discord-join%20now-green)](https://discord.gg/pSAp2qXe)
![GitHub forks](https://img.shields.io/github/forks/rotoapanta/ESP32-Blinking-RGB-Led?style=social)

# Contents

  * [Getting started](#getting-started)
    * [Getting started with MicroPython on the ESP32](#getting-started-with-micropython-on-the-esp32)
    * [Requirements](#requirements)
    * [Description of Components](#description-of-components)
    * [Power Supply Options](#power-supply-options)
    * [Pin Layout](#pin-layout)
  * [Instructions](#instructions)
  * [Environment Variables](#environment-variables)
  * [Running Tests](#running-tests)
  * [Usage/Examples](#usage-examples)
  * [Feedback](#feedback)
  * [Support](#support)
  * [License](#license)
  * [Autors](#autors)
  * [Links](#links)

# Getting started

## Getting started with MicroPython on the ESP32

Using MicroPython is a great way to get the most of your ESP32 board. And vice versa, the ESP32 chip is a great platform for using MicroPython. This tutorial will guide you through setting up MicroPython, getting a prompt, using WebREPL, connecting to the network and communicating with the Internet, using the hardware peripherals, and controlling some external components.

Let’s get started!
 
## Requirements

  * [ESP32 - working on this board](https://docs.espressif.com/projects/esp-idf/en/latest/esp32s2/hw-reference/esp32s2/user-guide-saola-1-v1.2.html)
  * [MicroPython for ESP32](http://micropython.org/download#esp32)
  * [Datasheet ESP32-S2-WROOM-I](https://www.espressif.com/sites/default/files/documentation/esp32-s2-wroom_esp32-s2-wroom-i_datasheet_en.pdf)
  * ESP32-S2-Saola-1
  * USB 2.0 cable (Standard-A to Micro-B)
  * Computer running Thonny on Windows, Linux or macOS (in this case macOS is used)

## Description of Components

![esp32-s2-saola-1-v1 2](https://user-images.githubusercontent.com/16738424/187048221-2b4044f2-b21a-4bbe-9c9f-85ab6a8721bb.png)

## Power Supply Options

There are three mutually exclusive ways to provide power to the board:

  * Micro-USB port, default power supply
  * 5V and GND pin headers
  * 3V3 and GND pin headers

**_It is recommended to use the first option: Micro-USB Port._**

## Pin Layout
![esp32-s2-saola1-pinout](https://user-images.githubusercontent.com/16738424/187049261-8ccb55c8-75af-4fb4-b2c2-04de95fb5af5.jpg)

# Instructions

* Install MicroPython on the ESP32, you can use [this tutorial](https://lemariva.com/blog/2017/10/micropython-getting-started);


* Identificar el GPIO del LED RGB

* Create the main.py
* Modify the `main.py` file if you want to:
  * The code line
  ```python
  ws2812_chain =  WS2812(ledNumber=ledNumber, brightness=100)
  ```

## Changelog

* Revision: 1.1 - Code cleaned and added support for Amazon Echo (2nd Generation) using [this info](https://github.com/kakopappa/arduino-esp8266-alexa-multiple-wemo-switch/issues/22).
* Revision: 1.0 - Initial commit

## Environment Variables

To run this project, you will need to add the following environment variables to your guralpSoH file

`IP_EQUIPMENT = 'XXX.XXX.XXX.XX'`

## Running Tests

To run tests, run the following command

```bash
  npm run test
```

## Usage/Examples

```javascript
import Component from 'my-project'

function App() {
  return <Component />
}
```

## Feedback

If you have any feedback, please reach out to us at robertocarlos.toapanta@gmail.com

## Support

For support, email robertocarlos.toapanta@gmail.com or join our Discord channel.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Autors
- [@rotoapanta](https://github.com/rotoapanta)

More Info:
---------
* [MicroPython for ESP32](http://micropython.org/download#esp32)
* [MicroPython Tutorial](https://lemariva.com/blog/2017/10/micropython-getting-started)
* [NeoPixeles](https://learn.adafruit.com/esenciales-para-circuitpython/neopixeles-circuitpython)
* [Espressif IoT Development Framework](https://github.com/espressif/esp-idf)

## Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roberto-carlos-toapanta-g/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/rotoapanta)
