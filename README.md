# Forensic-scripts
This repository contains a collection of scripts that I have created for various Forensic projects . Each script is designed to perform a specific task and can be used independently or integrated into other projects.

## GeoFindIP.py

GeoFindIP is a Python script that utilizes the dpkt, socket, pygeoip, and optparse libraries to extract IP addresses from a packet capture (pcap) file and retrieve their geolocation information using the GeoLiteCity database.

#### Prerequisites
- Python 3.x
- dpkt library
- pygeoip library
- GeoLiteCity database (GeoLiteCity.dat)

Download the GeoLiteCity database from this repository or from the mbcc2006 github repository: https://github.com/mbcc2006/GeoLiteCity-data . And place the GeoLiteCity.dat file in the same directory as the script.

#### Usage

    python3 GeoFindIP.py -p <pcap file>

Replace <pcap file> with the path to your pcap file.

#### Output

The script will read the pcap file and display the source and destination IP addresses along with their corresponding geolocation information (city and country). If the IP address is not found in the GeoLiteCity database or is a private IP address, it will display a message indicating that the address is unregistered.

#### Disclaimer

The GeoLiteCity database used in this script is a free version provided by MaxMind. The accuracy of the geolocation data may vary, and it is recommended to use a licensed version or a more up-to-date geolocation service for production environments.

