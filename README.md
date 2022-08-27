# Esp32 RGB Blinking

# <p align="center">ESP32 RGB Blinking

<p align="center">This project is based on an ESP32-S2 general-purpose development board with micropython that allows the rgb led to blink.</p>

##

![Python Version](https://img.shields.io/pypi/pyversions/3)
[![GitHub issues](https://img.shields.io/github/issues/rotoapanta/esp32ledRGB)](https://github.com/rotoapanta/esp32ledRGB/issues)
![GitHub repo size](https://img.shields.io/github/repo-size/rotoapanta/esp32ledRGB)
![GitHub last commit](https://img.shields.io/github/last-commit/rotoapanta/esp32ledRGB)
![GitHub commit merge status](https://img.shields.io/github/commit-status/rotoapanta/prueba2/main/6a500cc65d)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Discord](https://img.shields.io/discord/996422496842694726)
[![Discord Invite](https://img.shields.io/badge/discord-join%20now-green)](https://discord.gg/pSAp2qXe)
![GitHub forks](https://img.shields.io/github/forks/rotoapanta/esp32ledRGB?style=social)

## Contents

  * [Getting started](#getting-started)
  * [Requirements](#requirements)
  * [Instructions](#instructions)
  * [Environment Variables](#environment-variables)
  * [Running Tests](#running-tests)
  * [Usage/Examples](#usage-examples)
  * [Feedback](#feedback)
  * [Support](#support)
  * [License](#license)
  * [Autors](#autors)
  * [Links](#links)

## Getting started

### Getting started with MicroPython on the ESP32

Using MicroPython is a great way to get the most of your ESP32 board. And vice versa, the ESP32 chip is a great platform for using MicroPython. This tutorial will guide you through setting up MicroPython, getting a prompt, using WebREPL, connecting to the network and communicating with the Internet, using the hardware peripherals, and controlling some external components.

Let’s get started!
 
## Requirements

* [ESP32 - working on this board](https://www.banggood.com/WeMos-WiFi-Bluetooth-Battery-ESP32-Development-Tool-p-1164436.html?p=QW0903761303201409LG)
* [MicroPython for ESP32](http://micropython.org/download#esp32)

## Instructions

* Install MicroPython on the ESP32, you can use [this tutorial](https://lemariva.com/blog/2017/10/micropython-getting-started);

![Image text](./images/1.png)

![Image text](./images/2.png)

![Image text](./images/Copia_3.png)


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
* [Universal Plug&Play](https://en.wikipedia.org/wiki/Universal_Plug_and_Play)
* [Node-red WEMO Emulator](http://flows.nodered.org/node/node-red-contrib-wemo-emulator)
* Chris(derossi) links:
  * [Amazon Echo & Home-Automation](http://www.makermusings.com/2015/07/13/amazon-echo-and-home-automation/)
  * [How to Make Amazon Echo Control Fake Wemo Devices](http://hackaday.com/2015/07/16/how-to-make-amazon-echo-control-fake-wemo-devices/)
  * [Virtual Wemo Code for Amazon Echo](http://www.makermusings.com/2015/07/18/virtual-wemo-code-for-amazon-echo)
  * [Home Automation with Amazon Echo Apps, Part 1](http://www.makermusings.com/2015/07/19/home-automation-with-amazon-echo-apps-part-1/)
* [Alexa Skills Kit](https://developer.amazon.com/appsandservices/solutions/alexa/alexa-skills-kit)
* [Flask-Ask: A New Python Framework for Rapid Alexa Alexa Skills Kit Development](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development)
* 

## Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/roberto-carlos-toapanta-g/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/rotoapanta)
