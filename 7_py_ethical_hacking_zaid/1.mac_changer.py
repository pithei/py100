'''
2021.01.17

getmac /v /FO csv
Get-NetAdapterAdvancedProperty -Name "*" -RegistryKeyword "*" -IncludeHidden
Set-NetAdapter -InterfaceDescription "B*2" -MacAddress "00-10-18-57-1B-0D"
netsh interface set interface Wi-Fi disable
netsh interface set interface Wi-Fi denable

Linux
ifconfig wlan0 down
ifconfig wlan0 hw ether 00:11:22:33:44:66
ifconfig wlan0 up
'''

import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:66"
# subprocess.call("COMMAND", shell = Ture)

#subprocess.call("ipconfig /all", shell=True)

subprocess.call("getmac -v", shell=True)

#print(data)
