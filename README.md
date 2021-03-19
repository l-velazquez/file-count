Programer: Luis F. Velazquez Sosa
Program name: file-count.py

Hello,

Thank you for downloading this program. This was made because I 
was having a problem when I was sending files from my raspberry pi
to google drive using rclone as a mounted drive on the raspberry pi.
This program will look at the google drive directory that you chose
and will look for how many files are in that directory you specified.
The program will also tell you the amount of time it took to send
one file from the other. With this information it can calculate the 
time it will approximately take to send all the files. This isnt an 
accurate aproximation but is a neat feature that can be improved. 	
The time it takes to send the file also depends on you internet speed
which your ISP will allow to send data. The program will finish 
automaticly once the amount of files are equal in both directories. 


How to configure the code:

- Since there isnt a grafical interface yet you will have to enter
	the directory path for the recieving end and the sending directory
	
- Read the commented code in the file-count.py to know what is what
	
- To run this program you need to go to where you downloaded the code
	in the terminal. Here you will run:
```sh	
~$ python3.7 file-count.py
```
	
- Note I used python3.7 because in my machine default python is python 2
	
- This program only works will python 3+
	
- The raspberry pi I used is the Raspberry Pi 3B v1.2 2015
	
- Hopfully this script has worked any suggestions or comments you can 
	email me at luisfernandojavier.velazquez@upr.edu

