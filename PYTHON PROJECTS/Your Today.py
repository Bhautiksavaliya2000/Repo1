from win10toast import ToastNotifier
import webbrowser
import tkinter
from datetime import datetime
import time



day = datetime.today().strftime('%A')
toast = ToastNotifier()
timetable = {'Monday':{'09:45':"first lecture: CN (NSV)\nCheck whatsapp for link",'10:45':"Second lecture: ADA (GJS)",'11:45':"It's recess time",
                       '12:25':"third lecture: CPDP (mathur sir)\nCheck whatsapp for link",'13:25':"last one: SE(lab) PVB"},
             'Tuesday':{'15:15':"first lecture: CS lab (TPB)",'10:45':"Second lecture: ADA (GJS)",'11:45':"It's recess time",
                       '12:25':"last lecture: SE (PVB)"},
             'Wednesday':{'09:45':"first lecture: ADA (GJS)",'10:45':"Second lecture: CN (NSV)\nCheck whatsapp for link",'11:45':"It's recess time",
                       '12:25':"third lecture: PE (DHP)\nCheck whatsapp for link",'13:25':"last one: SE (PVB)"},   
             'Thursday':{'09:45':"first lecture: CN (KNU)\nCheck whatsapp for link",'10:45':"Second lecture: CPDP (mathur sir)\nCheck whatsapp for link",
                       '11:45':"It's recess time",'12:25':"third lecture: CN lab (NSV)\nCheck whatsapp for link",'13:25':"last one: SE (PVB)"},
             'Friday': {'09:45':"first lecture: ADA lab (GJS)",'09:45':"Second lecture: CN (KNU)\nCheck whatsapp for link",'11:45':"It's recess time",
                       '12:25':"third lecture: PE (DHP)\nCheck whatsapp for link",'13:25':"last one: CS (HMP)"},
             'Saturday': {'09:53':"first lecture: ADA (GJS)",'10:45':"Second lecture: PE (DHP)\nCheck whatsapp for link",'11:45':"It's recess time",
                       '12:25':"last lecture: CS (TPB)"}                   
                       
            }
links = {'Monday':{'09:45':"https://meet.google.com/pmh-nxuu-ztd?pli=1&authuser=1",'13:25':"https://meet.google.com/xhs-ydbh-ajs?pli=1&authuser=1"},
         'Tuesday':{'09:45':"https://meet.google.com/qks-spzg-aup?pli=1&authuser=1",'10:45':"https://meet.google.com/pmh-nxuu-ztd?pli=1&authuser=1",
                   '12:25':"https://meet.google.com/xhs-ydbh-ajs?pli=1&authuser=1"},
         'Wednesday':{'09:45':"https://meet.google.com/pmh-nxuu-ztd?pli=1&authuser=1",'13:25':"https://meet.google.com/xhs-ydbh-ajs?pli=1&authuser=1"},
         'Thursday':{'09:45':"https://meet.google.com/xhs-ydbh-ajs?pli=1&authuser=1"},
         'Friday':{'09:45':"https://meet.google.com/msb-sack-mpj?pli=1&authuser=1",'13:25':"https://meet.google.com/zmd-ucej-odp?pli=1&authuser=1"},
         'Saturday':{'09:53':"https://meet.google.com/pmh-nxuu-ztd?pli=1&authuser=1",'12:25':"https://meet.google.com/qks-spzg-aup?pli=1&authuser=1"}
        }


def openlink(day,currenttime):
    try:
        webbrowser.open(links[day][currenttime])
    except Exception as e:
        pass
        
def show_notification(day,currenttime):
    toast.show_toast( title="Notification", msg=timetable[day][currenttime],
        icon_path=None, duration=10, threaded=False, callback_on_click=openlink(day,currenttime))




ans = input("Do you want to start now? (y/n) :")
if ans == 'Y' or ans=='y':
    currenttime = time.strftime("%H:%M")
    timeinterval_list = ['09:45','10:45','11:45','12:25','13:25']
    print("Your today is started....")

    for lec_time in timeinterval_list:
        if lec_time<currenttime:
            pass
        else:
            while currenttime != lec_time:
                time.sleep(1)
                currenttime = time.strftime("%H:%M")
            show_notification(day,currenttime)
        
else:
    print("Ok do it later! No issue. :) ")

