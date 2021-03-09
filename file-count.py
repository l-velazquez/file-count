#=======================================================================
#       Programmer: Luis F. Velázquez Sosa
#       GitHub: luisfernandojaviervelazquez
#       
#       Discription: Program will look at the recieving directory 
#       and see how many files have been sent and also tell you how
#       many files are left and the estimate time left in seconds
#


import os
import time
import statistics 

#the receving directory information
path, dirs, files = next(os.walk("/home/pi/file_receiver"))#this is the directory you want 

#the sending directory information
p,d,f = next(os.walk("/media/pi/file_sender"))

#this is to see the files recieved/total files 
print("File (recv)/(total left)")
print(len(files),"/",len(f))
#variable is for comparing to see if the files recieved has incresed 
file_count = len(files)
start = time.time()

#this is to save the time it takes to send the file and then finds the average to have a approx. time left
arr = []

while file_count < len(f):
    #updates the variables
    path, dirs, files = next(os.walk("/home/pi/mnt/gdrive/Extra/Photos/SONY-PICS/2020/9. Septiembre 2020"))
    #sleeps for a second to not take constant resources, number of seconds can be greater but the time it send
    #the file will become less accurate
    time.sleep(1)
    #if the file counted is less than the files in the directory being observered it will enter
    if file_count < len(files):
        
        #it will display the files recieved / and total files in the sending directory
        print(len(files),"/",len(f))
        
        #prints out the number of files left
        print("Files left:",len(f) - len(files))
        
        #updates the variable so it doesnt enter again in the if statment
        file_count = len(files)
        end = time.time()
        sec = round(end - start,1)
        
        #saves the amount of time it took to send the file and appends it to the array
        arr.append(sec)
        
        #print the time it took to send
        print("Est. time it took to send file",sec,"seconds")
        
        #print the aproximate time it will take to complete sending the files by 
        #taking the average times form the array and multiplying it by files left to send
        print("Approx. Time Left:",round(statistics.mean(arr) * (len(f) - len(files)),1),"seconds")
        
        #this is to restart the sending time recording
        start = time.time()
        



