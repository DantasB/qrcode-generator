# Qrcode-Generator

![demonstration](https://cdn.discordapp.com/attachments/539836407628169237/825422342938820618/unknown.png)

## Tabela de conteúdos

<!--ts-->
   * [About](#about)
   * [Requirements](#requirements)
   * [How to use](#how-to-use)
      * [CSV Structure](#csv-structure)
      * [Setting up Program](#program-setup)
   * [Technologies](#technologies)
<!--te-->

## About

This repository is a project used in a [LUDES](https://ludes.cos.ufrj.br/pt/ludes/) project, to help us with the qrcodes. So it's basically crawlling the [QRCode-Monkey](https://www.qrcode-monkey.com) page, defining a specific type of qrcode and them downloading it, organizing by folders.

## Requirements

To run this repository by yourself you will need to install python3 in your machine and them install all the requirements inside the [requirements](requirements.txt) file

## How to use

### CSV Structure

To run this code properly, you will need to have 2 specific columns [(URL and Category)](example.csv), that will be used to build the qrcodes. 

### Program Setup

```bash
# Clone this repository
$ git clone <https://github.com/DantasB/qrcode-generator>

# Access the project page on your terminal
$ cd qrcode-generator

# Install all the requirements
$ pip install -r requirements.txt

# Create a .env file
$ touch .env  

# Create the following parameters
 DIR_NAME #The directory path where the qrcodes will be stored
 CSV_FILENAME #The csv file path to get all the informations

# Execute the main program
$ python main.py

# Them it's just wait for the code run
```
![demonstration](https://cdn.discordapp.com/attachments/539836407628169237/825425540029612042/unknown.png)


## Technologies

* Python3
* Csv
* Aiohttp
