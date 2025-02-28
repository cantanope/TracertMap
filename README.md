<!-- ABOUT THE PROJECT -->
## About Tracert Map

![Picture of a Tracert Map](https://github.com/cantanope/TraceMap/Images/MapWithTrace.jpg?raw=true)

*Tracert Map* is an educational tool to help visualize the path of packets sent via the internet. It utilises the output of tracert and IP-API to show rough locations for each hop (with a public IP) to a target destination. 

The locations provided can be very precise when IPs are very well known, but for most routers the location is a little off so take results as such. 

Currently the program only works in windows but I will be adding support for linux later. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- GETTING STARTED -->
## Getting Started (windows 10+)

If you are running windows 10 or later follow these steps to see your first Tracert Map.

### Prerequisites

You will neeed python3 and these modules:
* tkinter
  ```sh
  pip install tk
  ```
* tkintermapview
  ```sh
  pip3 install tkintermapview
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

   ```sh
   git clone https://github.com/cantanope/TracertMap.git
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Simply run `tracertmap.ps1` and enter your address to trace. The map will open up automatically once the tracert command has finished. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Future Features

- [ ] A side bar of IP addresses found in tracert
- [ ] The ability to click on IP addresses to fly to location
- [ ] collect device public IP and use as starting point. 
- [ ] Show private vs Public IP's in the list of IP's found
- [ ] Fix IP's that share a location stacking, show as list instead. 
- [ ] Add hop numbers next to name on markers.   
- [ ] Autoinstall script for dependencies and TraceMap

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing



If there is a feature you would like or you think would be useful, please feel free to fork this repo and create a pull request.

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact



Project Link: [https://github.com/cantanope/TracertMap](https://github.com/cantanope/TracertMap)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Thank you othneildrew for helping with this README](https://github.com/othneildrew/Best-README-Template/blob/main/README.md)


<p align="right">(<a href="#readme-top">back to top</a>)</p>
