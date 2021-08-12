from pypresence import Presence  # The simple rich presence client in pypresence
import time as timemodule
from datetime import datetime, timedelta
import pytz
import os

client_id = "774140182345023488"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client

RPC.connect()

timetable = []

#Sunday
timetable.append([])

#Monday
timetable.append(["Ten Minute Break", "Kannada 3rd Language", "Ten Minute Break", None, "Ten Minute Break", "Physics",
                  "Ten Minute Break", "Math", "Ten Minute Break", "Computer", "Ten Minute Break", "Math", "Twenty Minute Break", "Geography", "Ten Minute Break",
                  "Biology", "Ten Minute Break", "English Language"])

#Tuesday
timetable.append(["Ten Minute Break", "English Literature", "Ten Minute Break", "Physics", "Ten Minute Break", "Math", "Ten Minute Break",
                  "Geography", "Ten Minute Break", "History", "Ten Minute Break", "Computer", "Ten Minute Break", "English Language", "Twenty Minute Break", "Hindi", "Ten Minute Break", None])

#Wenesday
timetable.append(["Ten Minute Break", None, "Ten Minute Break", "History", "Ten Minute Break", "Math", "Ten Minute Break",
                  "Math", "Ten Minute Break", "Chemistry", "Ten Minute Break", "Biology", "Twenty Minute Break", "Hindi", "Ten Minute Break", "Physics", "Ten Minute Break", 
                  "Geography"])

#Thursday
timetable.append(["Ten Minute Break", "English Literature", "Ten Minute Break", "History", "Ten Minute Break", "Math", "Ten Minute Break", "Art", "Ten Minute Break",
                  "Chemistry", "Ten Minute Break", "Geography", "Twenty Minute Break", "Hindi", "Ten Minute Break", "Biology", "Ten Minute Break", None])

#Friday
timetable.append(["Ten Minute Break", "English Literature", "Ten Minute Break", "Physics", "Ten Minute Break",
                  None, "Ten Minute Break", "English Language", "Ten Minute Break", "Chemistry", "Ten Minute Break", "Math", "Twenty Minute Break", 
                  "Math", "Ten Minute Break", "Hindi", "Ten Minute Break", "Art"])

#Saturday
timetable.append([])


starttimes = [(8,0),(8,10),(8,40),(8,50),(9,20),(9,30),(10,00),(10,10),(10,40),(10,50),(11,20),(11,30),(12,0),(12,20),(12,30),(13,0),(13,10),(13,40)]

def time():
    tz = pytz.timezone('Asia/Calcutta')
    now = datetime.now(tz)

    time1 = int(now.strftime("%H"))
    time2 = int(now.strftime("%M"))
    time = (time1, time2)    

    return time

def cperiod():
    ctime = time()
    for a in range(18):
        try:
            hour1 = starttimes[a][0]
            hour2 = starttimes[a+1][0]
            minute1 = starttimes[a][1]
            minute2 = starttimes[a+1][1]
        except:
            return 19

        if ((hour1 * 60) + minute1) < ((ctime[0] * 60) + ctime[1]) and ((hour2 * 60) + minute2) > ((ctime[0] * 60) + ctime[1]):
            return a

def rtime():
    ctime = time()
    a = cperiod()
    end = (((starttimes[a + 1][0] * 60) + starttimes[a + 1][1]) - ((ctime[0] * 60) + ctime[1])) * 60
    return end  

async def ainput():
    a = input()
    return a
while True:
    tz = pytz.timezone('Asia/Calcutta')
    now = datetime.now(tz)


    day = int(now.strftime("%w"))


    period = cperiod()
    if period == 19:
        RPC.clear(os.getpid())
        timemodule.sleep(60)
    else:
        periodn = timetable[day][period]

        if periodn == None:
            RPC.clear(os.getpid())
        elif periodn == "Ten Minute Break" or periodn == "Twenty Minute Break":
            RPC.clear(os.getpid())
        else:
            
            if periodn == "English Literature" or periodn == "English Language":
                image = "english"
            else:
                image = periodn.lower()

            end = rtime()
            end = now + timedelta(seconds = end)
            end = end.timestamp()
            RPC.update(details=f"Class: {timetable[day][period]}", state="Devloped By Thulium#0069",
                        large_image=image, large_text = timetable[day][period],small_image="teams", small_text="Microsoft Teams", end=end)
            timemodule.sleep(60)





    
