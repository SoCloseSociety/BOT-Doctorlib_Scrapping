Prerequisite - 
Your machine must be installed with python. To check, go to CMD any type -> py. It will show the Installed python version if python is already installed on your machine. 

***********************
1. Nord VPN required
2. Your machine need to able connect with nord through command line.
3. To to this add  nord vpn path to your environment variable path. Usually nord vpn path is - C:\Program Files\NordVPN\
![1](https://user-images.githubusercontent.com/31489330/190924798-25ab352d-bd9c-4a00-b25a-792b3ec4a689.png)
![2](https://user-images.githubusercontent.com/31489330/190925057-fe6d9e3a-a18c-4e31-adde-0086c0857d85.png)
![4](https://user-images.githubusercontent.com/31489330/190924811-998694c6-265c-4caa-accf-be50bb90a59a.png)
![6](https://user-images.githubusercontent.com/31489330/190924818-5f8caca6-c423-48b6-b0fc-df0ae7ce33ef.png)
![7](https://user-images.githubusercontent.com/31489330/190924821-d769c080-0185-4a1b-9a31-d38fa7d3410a.png)

Checking if we are  able  to  connect NordVPN through commandline
![9](https://user-images.githubusercontent.com/31489330/190924822-1769925d-3f9c-4fa3-b033-df113b07836b.gif)

Success!!!
For more information you can read - https://support.nordvpn.com/Connectivity/Windows/1350897482/Connect-to-NordVPN-app-on-Windows-using-the-Command-Prompt.htm
********************************************************************************************************************************************************************


Steps - 
1. Run requirements.txt  from cmd. Type this command in your project terminal -> pip install -r requirements.txt
2.  Enter specialization and Place. It  will ask in console. 
5. Run main.py

This  program will  generate  2  csv files. 
At first, it will go through search query and will collect profile  links.
It will clean & dump those  links on  'doctolib_profile_link.csv'

After that  it will automatically go to each profile link  & scrap data. 
It  will  save those  data  at 'doctolib_profile_details.csv' file.




