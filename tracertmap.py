import tkinter as tk
import tkintermapview
import requests
from requests import get
import re

BUTTONWIDTH = 30
BUTTONHEIGHT = 2

# Extract IP list from the raw output of tracert -4d
def extract_ips():
    ip_list = []
    with open("trace.txt", 'r') as file:
        pattern = ('\\[?(\\d+\\.\\d+\\.\\d+\\.\\d+)\\]?')
        pattern2 = ('^(\\s*\\d+)')
        lines = file.readlines()
        for line in lines:
            # Match lines that start with a number (hop number)
            if re.search(pattern2, line):
                # Extract the IP address (inside brackets or not)
                match = re.search(pattern, line)
                if match:
                    ip_list.append(match.group(1))
    return ip_list

# Request IP informaiton from IPAPI
def getLocationData(ip_string):
    # URL for location lookup
    url = 'http://ip-api.com/batch?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,isp,org,query'
    data =  f'[{ip_string}]'
    response = requests.post(url, data=data)
    return(response.json())

# Create a string that is accepted by IP API
def makeAPIString(raw_IP_List):
    templist = []
    device_ip = get('https://api.ipify.org').content.decode('utf8')
    templist.append(f'"{'{}'.format(device_ip)}"')
    for ip in raw_IP_List:
        templist.append(f'"{ip.strip()}"')
    return(','.join(templist))

# generate IP data from trace.txt
data =  getLocationData(makeAPIString(extract_ips()))

# Create a list containing only IP's that are successful
success = []
for location in data:
    if location["status"]=='success':
        success.append(location)

# create tkinter window
window = tk.Tk()
window.geometry(f"{700}x{500}")
window.title("Traceroute Map")
window.configure(background='gray')

# create map widget
map_widget = tkintermapview.TkinterMapView(window, width=500, height=500, corner_radius=5)
map_widget.place(relx=.7, rely=.5, anchor=tk.CENTER)
map_widget.set_position(success[0]['lat'],success[0]['lon'])
map_widget.set_zoom(15)

# view marker command
def view_marker(index):
    map_widget.set_position(success[index]['lat'],success[index]['lon'])
    map_widget.set_zoom(15)

# create buttons
y_offset = 5
hop_number = 0
buttons = []
for i in range(0,len(success)):
    pad_char = ' '
    button = tk.Button(window,text=(f" {'Hop':<4}{str(i+1):{pad_char}<2}{str(success[i]['org']).strip():{pad_char}>20}"),height=BUTTONHEIGHT,width=BUTTONWIDTH,command=lambda index=i :view_marker(index))
    button.place(x=5,y=y_offset)
    buttons.append(button)
    y_offset+=40



# create paths between IPs with first two successful resolutions. 
path = map_widget.set_path([(success[0]['lat'],success[0]['lon']),(success[1]['lat'],success[1]['lon'])])

# create map markers and path for each IP 
markers = []
for location in success:
    if location["status"]=='success':
        markers.append(map_widget.set_marker(location['lat'],location['lon'],text=location['query'],marker_color_circle = 'darkgrey',marker_color_outside = 'grey')) 
        path.add_position(location['lat'],location['lon'])
# Color starting point green
markers[0].marker_color_circle = 'darkgreen'
markers[0].marker_color_outside = 'green'
# Color end point red
markers[-1].marker_color_circle = 'darkred'
markers[-1].marker_color_outside = 'red'

window.mainloop()