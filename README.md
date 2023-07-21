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

Assuming you have a PCAP file named example.pcap containing network traffic, here's an example of what the script output might look like:
```bash    
    [+] Source: 192.168.1.100 ----> Dst: 216.58.205.110
    [+] Source: Mountain View, USA ----> Dst: Mountain View, USA
    [+] Source: 192.168.1.101 ----> Dst: 151.101.65.69
    [+] Source: San Francisco, USA ----> Dst: San Francisco, USA
    [+] Source: 192.168.1.102 ----> Dst: 8.8.8.8
    [+] Source: New York, USA ----> Dst: Mountain View, USA
```

## getPDFMetadata.py

This Python script allows you to extract metadata from a PDF file.

#### Prerequisites

Make sure you have the following dependencies installed:

- PyPDF2

#### Usage

Run the script with the following command:

```
python getPDFMetadata.py -f <PDF file name>
```

Replace `<PDF file name>` with the path to your desired PDF file.

**Note:** The PDF file should be accessible and readable by the script.

#### Example

To extract metadata from a PDF file named `example.pdf`, run the following command:

```
python getPDFMetadata.py -f example.pdf
```

Result:
```bash
    [*] Metadata of the PDF:  example.pdf
    [+]Author:BeRoot00
    [+]Title:Example Document
    [+]Subject:Sample PDF with Metadata
    [+]Creator:Microsoft® Word 2019
    [+]Producer:Adobe Acrobat Pro 2020
    [+]CreationDate:2023-05-15T09:30:00Z
    [+]ModDate:2023-07-18T14:22:00Z
    [+]Keywords:example, metadata, PDF
    [+]Trapped:False
    [+]Company:Example Inc.
```


## volatilityResult.py

This Python script allows you to execute a Volatility plugin on a memory image using the Volatility framework. It utilizes the `subprocess` module to run the Volatility command-line tool and captures the output to a specified file.

#### Prerequisites

Make sure you have the following requirements met before running the script:

- Python 3.x installed
- [Volatility](https://www.volatilityfoundation.org/) framework installed and accessible via the command-line

#### Usage

Modify the following variables in the script to fit your needs:

- `plugin_name`: Specify the name of the Volatility plugin you want to execute.
- `image_path`: Provide the path to the memory image file you want to analyze.
- `output_file`: Specify the path where you want to save the output.

```python
# Specify the Volatility plugin to execute
plugin_name = 'plugin_name'

# Specify the path to the memory image
image_path = '/pathToMemory/image.raw'

# Specify the output file path
output_file = '/pathToOutput/file.txt'

# Run the Volatility plugin
run_volatility_plugin(plugin_name, image_path, output_file)
```

Once you have set the required parameters, run the script using a Python interpreter. The script will execute the specified Volatility plugin and store the output in the specified output file.

Example of output file content:
```bash
    Volatility Foundation Volatility Framework 2.6.1
    Offset(P)          Name                    PID   PPID PDB        Time created                   Time exited   
    ------------------ -------------------- ------ ------ ---------- ------------------------------ ------------------------------
    0x000000001f3c4040 System                    4      0 0x00000000 2021-09-12 10:12:48 UTC+0000 
    0x000000001f6a7b70 smss.exe                316      4 0x00000000 2021-09-12 10:12:48 UTC+0000 
    0x000000001f6e9290 csrss.exe               416    408 0x00000000 2021-09-12 10:12:48 UTC+0000 
    0x000000001f6f7b30 wininit.exe             460    408 0x00000000 2021-09-12 10:12:49 UTC+0000 
    0x000000001f6ff040 csrss.exe               468    460 0x00000000 2021-09-12 10:12:49 UTC+0000
    0x000000001f705040 services.exe            504    460 0x00000000 2021-09-12 10:12:49 UTC+0000    
    0x000000001f707040 lsass.exe               512    460 0x00000000 2021-09-12 10:12:49 UTC+0000 
    0x000000001f70c040 lsm.exe                 520    460 0x00000000 2021-09-12 10:12:49 UTC+0000  
    0x000000001f70e040 svchost.exe             564    504 0x00000000 2021-09-12 10:12:49 UTC+0000  
    0x000000001f713040 svchost.exe             624    504 0x00000000 2021-09-12 10:12:50 UTC+0000
    0x000000001f71b040 fontdrvhost.exe         676    504 0x00000000 2021-09-12 10:12:50 UTC+0000                                 
```

Note: Make sure you have the necessary permissions to read the memory image and write to the output file.

