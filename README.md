# Tracemyhop
## _Easy to use traceroute with IP Geolocation Service_
Tracemyhop is a software based on the use of traceroute tools and is relationated with a third-party geolocation service ip.
Main software strengths:
- Easy to  use and customization, developed in Python
- Third-party IP Geolocation Service already integrated 

## Features
- IP Geolocation Service 
- Various output format for geolocation
- Export report in various format 
- Easy config setup for enable or disable features


The basis of the program is based on the execution of traceroute program and with a captured output is possible
to analyze the different hop in the Internet and get a report about location, ISP, organization, timezone etc...
The third-party software that has been integrated is [IP-API](https://ip-api.com/) web api service, there is a limit for free plan. 
Is possible to config the API Key for enable your own pro plan to use.

## Installation
As a first step, check if you have _traceroute_ software with:
```sh
traceroute
```
If you got an error, try to install _traceroute_ with your package manager.

Clone this repository with and mark the program as executable:
```sh
git clone https://github.com/grecosamuel/tracemyhop.git
cd tracemyhop/
chmod +x tracemyhop.py
```


## Execution
1. Run traceroute script from the CLI:
    ```sh
    python3 tracemyhop.py
    ```
2. Type the IP or the domain of the target host, 
    <br>e.g.<br>
    ```sh
    Host target (ip address or domain): google.com
    ```
3. Wait until the trace is complete.

**Free Software**