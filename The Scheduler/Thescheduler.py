import subprocess
import pyautogui
import time 
import pandas as pd
from datetime import datetime
import csv
def mtruncateandadd():
    print("""1.Function of Recording
2.Function of Joining Meeting
3.Function of Ending the recording
4.All of the Functions""")
    sp=int(input("which functions mouse input do you want to change?"))
    var5=open("tinpr.csv","r+")
    var5.truncate(0)
    var5.close()
    tinp=int(input("Write the number of seconds you want to move your cursor to the asked location:"))
    tinpr = open("tinpr.csv","a",newline="")
    tinprwriter=csv.writer(tinpr)
    tinprwriter.writerow(['tinp'])
    list2=[tinp]
    tinprwriter.writerow(list2)
    tinpr.close()
    
    if sp==1:
        var=open("renp.csv","r+")
        var.truncate(0)
        var.close()
        recinputs()
    if sp==2:
        var1=open("menp.csv","r+")
        var1.truncate(0)
        var1.close()
        zoominputs()
    if sp==3:
        var2=open("eenp.csv","r+")
        var2.truncate(0)
        var2.close()
        endrecordinputs()
    if sp==4:
        var=open("renp.csv","r+")
        var.truncate(0)
        var.close()
        var1=open("menp.csv","r+")
        var1.truncate(0)
        var1.close()
        var2=open("eenp.csv","r+")
        var2.truncate(0)
        var2.close()
        recinputs()
        zoominputs()
        endrecordinputs()
    


def recinputs():
    tinpr = pd.read_csv('tinpr.csv')
    tinp=int(tinpr.loc[0,'tinp'])
    print("MOUSE SETUP For Recording Screen")
    print("Please move your Cursor to SPOTLIGHT SEARCH BUTTON")
    print("you have" , tinp ,"sec!!!")
    time.sleep(tinp)
    r11,r12=pyautogui.position() 
    pyautogui.click()
    time.sleep(2)
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("Please move your cursor to SPOTLIGHT SEARCH BOX")
    print("you have" , tinp ,"sec!!!")
    time.sleep(tinp)
    r21,r22=pyautogui.position() 
    time.sleep(2)
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("wait....")
    print("Don't move your Cursor.Leave it alone!!!")
    time.sleep(5)
    pyautogui.moveTo(x=r11,y=r12)
    pyautogui.click()
    time.sleep(2)
        
    pyautogui.moveTo(x=r21,y=r22)
    pyautogui.click()
    pyautogui.write("qtp")
    pyautogui.press('enter')

    time.sleep(2)

    pyautogui.moveTo(x=211,y=6)
    pyautogui.click()

    time.sleep(2)
    pyautogui.moveTo(x=232,y=75)
    pyautogui.click()
    time.sleep(3)
        
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("Please move your cursor to RECORD BUTTON")
    print("you have" , tinp ,"sec!!!")
    time.sleep(tinp)
    r51,r52=pyautogui.position() 
    pyautogui.press("esc")
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("wait....")
    print("Please move your cursor to CANCEL BUTTON")
    print("you have" , tinp ,"sec!!!")
    time.sleep(2)
    subprocess.call(["/usr/bin/open", "/System/Applications/QuickTime Player.app"])
    time.sleep(tinp) 
    r61,r62=pyautogui.position() 
    pyautogui.click()
    renp = open("renp.csv","a",newline="")
    renpwriter=csv.writer(renp)
    renpwriter.writerow(['r11','r12','r21','r22','r51','r52','r61','r62'])
    renplist=[r11,r12,r21,r22,r51,r52,r61,r62]
    renpwriter.writerow(renplist)
    renp.close()
def zoominputs():
    tinpr = pd.read_csv('tinpr.csv')
    tinp=int(tinpr.loc[0,'tinp'])
    print("MOUSE SETUP For JOINING MEETINGS")
    print("wait...")
    time.sleep(2)
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    time.sleep(10)
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("Please move your Cursor to HOME ICON IN ZOOM")
    print("you have" , tinp ,"sec!!!")
    time.sleep(3)
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    time.sleep(tinp)
    m11,m12=pyautogui.position() 
    time.sleep(2)
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("Please move your cursor to JOIN MEETING BUTTON")
    print("you have" , tinp ,"sec!!!")
    time.sleep(5)
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    time.sleep(tinp)
    m21,m22=pyautogui.position() 
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("wait....")
    print("Don't move your Cursor.Leave it alone!!!")
    time.sleep(4)
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    pyautogui.moveTo(x=m21,y=m22)
    pyautogui.click()
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("Please move your cursor to MEETING ID OR PERSONAL LINK NAME BOX")
    print("you have" , tinp ,"sec!!!")
    time.sleep(5)
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    time.sleep(tinp)
    m31,m32=pyautogui.position() 
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("wait....")
    print("Don't move your Cursor.Leave it alone!!!")
    time.sleep(4)
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    pyautogui.moveTo(x=m31,y=m32)
    pyautogui.click()
    with pyautogui.hold('command'):
        pyautogui.press('a')
    pyautogui.press('delete')
    time.sleep(1)
    pyautogui.write("5414851215")
    pyautogui.click()
    pyautogui.press('enter')
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("Please move your cursor to PASSWORD BOX")
    print("you have" , tinp ,"sec!!!")
    time.sleep(2)
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    time.sleep(5)
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    time.sleep(tinp)
    m41,m42=pyautogui.position() 
    subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    pyautogui.moveTo(x=m31,y=m32)
    pyautogui.click()
    pyautogui.press('esc')
    time.sleep(2)
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    menp = open("menp.csv","a",newline="")
    menpwriter=csv.writer(menp)
    menpwriter.writerow(['m11','m12','m21','m22','m31','m32','m41','m42'])
    menplist=[m11,m12,m21,m22,m31,m32,m41,m42]
    menpwriter.writerow(menplist)
    menp.close()
def endrecordinputs(): 
    tinpr = pd.read_csv('tinpr.csv')
    tinp=int(tinpr.loc[0,'tinp'])
    renp = pd.read_csv('renp.csv')
    r11=int(renp.loc[0,'r11'])
    r12=int(renp.loc[0,'r12'])
    r21=int(renp.loc[0,'r21'])
    r22=int(renp.loc[0,'r22'])
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("wait...")
    print("Don't move your Cursor.Leave it alone!!!")
    time.sleep(6)
    pyautogui.moveTo(x=r11,y=r12)
    pyautogui.click()
    pyautogui.moveTo(x=r21,y=r22)
    pyautogui.click()
    pyautogui.write("qtp")
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(x=211,y=6)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(x=232,y=75)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(x=100,y=100)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(x=r11,y=r12)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(x=r21,y=r22)
    pyautogui.click()
    pyautogui.write("qtp")
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(x=211,y=6)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(x=232,y=75)
    pyautogui.click()
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("Please move your cursor to END RECORDING BUTTON")
    print("you have" , tinp ,"sec!!!")
    time.sleep(tinp)
    e11,e12=pyautogui.position() 
    pyautogui.click()
    time.sleep(7)
    subprocess.call(["/usr/bin/open", "/System/Applications/Utilities/Terminal.app"])
    print("Your Inputs have Been Taken")
    eenp = open("eenp.csv","a",newline="")
    eenpwriter=csv.writer(eenp)
    eenpwriter.writerow(['e11','e12'])
    eenplist=[e11,e12]
    eenpwriter.writerow(eenplist)
    eenp.close()



        

        



def inputfordefaultwork():
    now = datetime.now().strftime("%H:%M:%S")
    print(now)
    n=int(input("Enter the number of meetings you want as your default:"))
    print("Please Enter Time in HH:MM:SS Format and in 24 Hour-Clock Time")
    rec=input("Enter the time you want to start the recording at:")
    erec=input("Enter the time you want to end the recording at:")
    dc = open("dctimings.csv","a",newline="")
    dcwriter=csv.writer(dc)
    dcwriter.writerow(['rec','erec','n'])
    list2=[rec,erec,n]
    dcwriter.writerow(list2)
    dc.close()

    for i in range(1,n+1):
        df = open("dtimings.csv","a",newline="")
        print("For Meeting",i)
        print("Time")
        print("Please Enter Time in HH:MM:SS Format and in 24 Hour-Clock Time")
        a=input("Enter the time you want to start the meeting at:")
        print(a)
        print('Meeting ID')
        b=int(input("Enter Meeting Id:"))
        print(b)
        c=input("Enter Meeting password:")
        print(c)
        dfwriter=csv.writer(df)
        dfwriter.writerow(['timing','meetingid','pswd'])
        list1=[a,b,c]
        dfwriter.writerow(list1)
        df.close()

def defaultwork():
    now = datetime.now().strftime("%H:%M:%S")
    print("Current Time:",now)
    dc = pd.read_csv('dctimings.csv')
    now = datetime.now().strftime("%H:%M:%S")
    print("current time",now)
    dc = pd.read_csv('dctimings.csv')
    meec=dc.loc[0,"rec"]
    print("rec timing",meec)
    now1=int(now[:2])
    now2=int(now[3:5])
    now3=int(now[6:9])
    mee1=int(meec[:2])
    mee2=int(meec[3:5])
    mee3=int(meec[6:9])
    diff1=abs(mee1-now1)
    diff2=abs(mee2-now2)
    diff3=abs(mee3-now3)
    rdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
    rdiffsec=abs(rdiffsec)
    print("rdiffsec=",rdiffsec)
    dc = pd.read_csv('dctimings.csv')
    n=dc.loc[0,'n']



    def torecordw(a):
        renp = pd.read_csv('renp.csv')
        r11=int(renp.loc[0,'r11'])
        r12=int(renp.loc[0,'r12'])
        r21=int(renp.loc[0,'r21'])
        r22=int(renp.loc[0,'r22'])
        r51=int(renp.loc[0,'r51'])
        r52=int(renp.loc[0,'r52'])
        r61=int(renp.loc[0,'r61'])
        r62=int(renp.loc[0,'r62'])
        pyautogui.moveTo(x=r11,y=r12)
        pyautogui.click()
    
        time.sleep(2)

        pyautogui.moveTo(x=r21,y=r22)
        pyautogui.click()
        pyautogui.write(a)
        pyautogui.press('enter')

        time.sleep(2)

        pyautogui.moveTo(x=211,y=6)
        pyautogui.click()

        time.sleep(2)

        pyautogui.moveTo(x=232,y=75)
        pyautogui.click()
    
        time.sleep(2)

        pyautogui.moveTo(x=r51,y=r52)
        pyautogui.click()

        time.sleep(5)

        pyautogui.moveTo(x=r61,y=r62)
        pyautogui.click()
        pyautogui.click()
    

        time.sleep(2)
    
        pyautogui.moveTo(x=0,y=578)
        pyautogui.click()
        
    
    dc = pd.read_csv('dctimings.csv')
    time.sleep(rdiffsec)

    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now in str(dc['rec']):
            row = dc.loc[dc['rec'] == now]
            rec= str(row.iloc[0,0])
                
    
            torecordw("qtp")
            time.sleep(1)
            print('rec started')
            break
        
    ski1=2
    for i in range(0,n):
        if i==0:
            print("i=0")
            dc = pd.read_csv('dctimings.csv')
            rec =dc.loc[0,"rec"]
            print("opening time",rec)
            df = pd.read_csv('dtimings.csv')
            meec = df.loc[0,"timing"]
            print("closing timing",meec)
            now1=int(rec[:2])
            now2=int(rec[3:5])
            now3=int(rec[6:9])
            mee1=int(meec[:2])
            mee2=int(meec[3:5])
            mee3=int(meec[6:9])
            diff1=abs(mee1-now1)
            diff2=abs(mee2-now2)
            diff3=abs(mee3-now3)
            mdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
            mdiffsec=abs(mdiffsec)
            print("mdiffsec=",mdiffsec)
        if i>=1 and i<=n-1:
            if i==1:
                print("i==1")
                df = pd.read_csv('dtimings.csv')
                meeo=df.loc[0,"timing"]
                print('opening timing',meeo)
                meec=df.loc[2,"timing"]
                print('closing timing',meec)
                mee4=int(meeo[:2])
                mee5=int(meeo[3:5])
                mee6=int(meeo[6:9])
                mee7=int(meec[:2])
                mee8=int(meec[3:5])
                mee9=int(meec[6:9])
                diff1=abs(mee7-mee4)
                diff2=abs(mee8-mee5)
                diff3=abs(mee9-mee6)
                mdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
                mdiffsec=abs(mdiffsec)
                print("mdiffsec=",mdiffsec)
                prev=meec
            if i>1 and i<=n-1:
                ski1=ski1+2
                df = pd.read_csv('dtimings.csv')
                print("i=",i)
                print('opening timing',prev)
                meeo=prev
                meec=df.loc[ski1,"timing"]
                print('closing timing',meec)
                mee4=int(meeo[:2])
                mee5=int(meeo[3:5])
                mee6=int(meeo[6:9])
                mee7=int(meec[:2])
                mee8=int(meec[3:5])
                mee9=int(meec[6:9])
                diff1=abs(mee7-mee4)
                diff2=abs(mee8-mee5)
                diff3=abs(mee9-mee6)
                mdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
                mdiffsec=abs(mdiffsec)
                print("mdiffsec=",mdiffsec)
                prev=meec
                
                
        def sign_in(meetingid, pswd):
            menp = pd.read_csv('menp.csv')
            m11=int(menp.loc[0,'m11'])
            m12=int(menp.loc[0,'m12'])
            m21=int(menp.loc[0,'m21'])
            m22=int(menp.loc[0,'m22'])
            m31=int(menp.loc[0,'m31'])
            m32=int(menp.loc[0,'m32'])
            m41=int(menp.loc[0,'m41'])
            m42=int(menp.loc[0,'m42'])
            subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
            
            time.sleep(10)
            pyautogui.moveTo(x=m11,y=m12)
            pyautogui.click()
            
            time.sleep(2)
            pyautogui.moveTo(x=m21,y=m22)
            pyautogui.click()
            
            
            pyautogui.moveTo(x=m31,y=m32)
            time.sleep(1)
            with pyautogui.hold('command'):
                pyautogui.press('a')
            pyautogui.press('delete')
            pyautogui.write(meetingid)
            pyautogui.press('enter')
            
            time.sleep(8)
            #Types the password and hits enter
            
            pyautogui.moveTo(x=m41,y=m42)
            pyautogui.click()
            pyautogui.write(pswd)
            pyautogui.press('enter')
            
            
            
            time.sleep(10)
            
            pyautogui.moveTo(x=0,y=578)
            pyautogui.click()
    


        df = pd.read_csv('dtimings.csv')

        time.sleep(mdiffsec)
        while True:
            # checking of the current time exists in our csv file
            now = datetime.now().strftime("%H:%M:%S")
            if now in str(df['timing']):
                row = df.loc[df['timing'] == now]
                meetingid = str(row.iloc[0,1])
                pswd = str(row.iloc[0,2])
    
                sign_in(meetingid,pswd)
                time.sleep(40)
                print('signed in')
                break
            
            
    now = datetime.now().strftime("%H:%M:%S")
    print("current time",now)
    meeo=prev
    print('opening timing',prev)
    dc = pd.read_csv('dctimings.csv')
    meec=dc.loc[0,"erec"]
    print('erec timing',meec)
    mee4=int(meeo[:2])
    mee5=int(meeo[3:5])
    mee6=int(meeo[6:9])
    mee7=int(meec[:2])
    mee8=int(meec[3:5])
    mee9=int(meec[6:9])
    diff1=abs(mee7-mee4)
    diff2=abs(mee8-mee5)
    diff3=abs(mee9-mee6)
    ediffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
    ediffsec=abs(ediffsec)
    print("ediffsec=",ediffsec)
    def endrecording():
        eenp = pd.read_csv('eenp.csv')
        e11=int(eenp.loc[0,'e11'])
        e12=int(eenp.loc[0,'e12'])
        pyautogui.press('esc')
        time.sleep(2)
        renp = pd.read_csv('renp.csv')
        r11=int(renp.loc[0,'r11'])
        r12=int(renp.loc[0,'r12'])
        r21=int(renp.loc[0,'r21'])
        r22=int(renp.loc[0,'r22'])
        pyautogui.moveTo(x=r11,y=r12)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(x=r21,y=r22)
        pyautogui.click()
        pyautogui.write("qtp")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.moveTo(x=211,y=6)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(x=232,y=75)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(x=e11,y=e12)
        pyautogui.click()
        pyautogui.click()
        
    dc = pd.read_csv('dctimings.csv')
    time.sleep(ediffsec)
    
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now in str(dc['erec']):
                row = dc.loc[dc['erec'] == now]
                erec= str(row.iloc[0,1])
                
    
                endrecording()
                time.sleep(1)
                print('rec ended')
                break
                
def truncateandadd():
    var=open("dctimings.csv","r+")
    var.truncate(0)
    var.close()
    var1=open("dtimings.csv","r+")
    var1.truncate(0)
    var1.close()
    inputfordefaultwork()
    
    
            
def inputwork():
    import subprocess
    import pyautogui
    import time 
    import pandas as pd
    from datetime import datetime
    import csv

    var=open("itimings.csv","r+")
    var.truncate(0)
    var.close()
    now = datetime.now().strftime("%H:%M:%S")
    print(now)
    n=int(input("Enter the number of meetings you have today:"))
    print("write only yes or no for the next ques...")
    rec=input("Enter the time you want to start the recording at:")
    erec=input("Enter the time you want to end the recording at:")
    

    for i in range(1,n+1):
        df = open("itimings.csv","a",newline="")
        print("For Meeting",i)
        print("Time")
        print("Please Enter Time in HH:MM:SS Format and in 24 Hour-Clock Time")
        a=input("Enter the time you want to start the meeting at:")
        print(a)
        print('Meeting ID')
        b=int(input("Enter Meeting Id:"))
        print(b)
        c=input("Enter Meeting password:")
        print(c)
        dfwriter=csv.writer(df)
        dfwriter.writerow(['timing','meetingid','pswd'])
        list1=[a,b,c]
        dfwriter.writerow(list1)
        df.close()
    now = datetime.now().strftime("%H:%M:%S")
    print("current time",now)
    meec=rec
    print("rec timing",meec)
    now1=int(now[:2])
    now2=int(now[3:5])
    now3=int(now[6:9])
    mee1=int(meec[:2])
    mee2=int(meec[3:5])
    mee3=int(meec[6:9])
    diff1=abs(mee1-now1)
    print(diff1)
    diff2=abs(mee2-now2)
    print(diff2)
    diff3=abs(mee3-now3)
    rdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
    rdiffsec=abs(rdiffsec)
    print("rdiffsec=",rdiffsec)



    def torecordw(a):
        renp = pd.read_csv('renp.csv')
        r11=int(renp.loc[0,'r11'])
        r12=int(renp.loc[0,'r12'])
        r21=int(renp.loc[0,'r21'])
        r22=int(renp.loc[0,'r22'])
        r51=int(renp.loc[0,'r51'])
        r52=int(renp.loc[0,'r52'])
        r61=int(renp.loc[0,'r61'])
        r62=int(renp.loc[0,'r62'])
        pyautogui.moveTo(x=r11,y=r12)
        pyautogui.click()
    
        time.sleep(2)

        pyautogui.moveTo(x=r21,y=r22)
        pyautogui.click()
        pyautogui.write(a)
        pyautogui.press('enter')

        time.sleep(2)

        pyautogui.moveTo(x=211,y=6)
        pyautogui.click()

        time.sleep(2)

        pyautogui.moveTo(x=232,y=75)
        pyautogui.click()

        time.sleep(2)

        pyautogui.moveTo(x=r51,y=r52)
        pyautogui.click()

        time.sleep(5)

        pyautogui.moveTo(x=r61,y=r62)
        pyautogui.click()
        pyautogui.click()
    

        time.sleep(2)
    
        pyautogui.moveTo(x=0,y=578)
        pyautogui.click()
    

    time.sleep(rdiffsec)
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == rec:
            torecordw('qtp')
            print("rec started")
            break
        
    ski1=2
    for i in range(0,n):
        if i==0:
            print("i=0")
            print("opening time",rec)
            df = pd.read_csv('itimings.csv')
            meec = df.loc[0,"timing"]
            print("closing timing",meec)
            now1=int(rec[:2])
            now2=int(rec[3:5])
            now3=int(rec[6:9])
            mee1=int(meec[:2])
            mee2=int(meec[3:5])
            mee3=int(meec[6:9])
            diff1=abs(mee1-now1)
            diff2=abs(mee2-now2)
            diff3=abs(mee3-now3)
            mdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
            mdiffsec=abs(mdiffsec)
            print("mdiffsec=",mdiffsec)
            prev=meec
        if i>=1 and i<=n-1:
            if i==1:
                print("i==1")
                df = pd.read_csv('itimings.csv')
                meeo=df.loc[0,"timing"]
                print('opening timing',meeo)
                meec=df.loc[2,"timing"]
                print('closing timing',meec)
                mee4=int(meeo[:2])
                mee5=int(meeo[3:5])
                mee6=int(meeo[6:9])
                mee7=int(meec[:2])
                mee8=int(meec[3:5])
                mee9=int(meec[6:9])
                diff1=abs(mee7-mee4)
                diff2=abs(mee8-mee5)
                diff3=abs(mee9-mee6)
                mdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
                mdiffsec=abs(mdiffsec)
                print("mdiffsec=",mdiffsec)
                prev=meec
            if i>1 and i<=n-1:
                ski1=ski1+2
                df = pd.read_csv('itimings.csv')
                print("i=",i)
                print('opening timing',prev)
                meeo=prev
                meec=df.loc[ski1,"timing"]
                print('closing timing',meec)
                mee4=int(meeo[:2])
                mee5=int(meeo[3:5])
                mee6=int(meeo[6:9])
                mee7=int(meec[:2])
                mee8=int(meec[3:5])
                mee9=int(meec[6:9])
                diff1=abs(mee7-mee4)
                diff2=abs(mee8-mee5)
                diff3=abs(mee9-mee6)
                mdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
                mdiffsec=abs(mdiffsec)
                print("mdiffsec=",mdiffsec)
                prev=meec

        def sign_in(meetingid,pswd):
            menp = pd.read_csv('menp.csv')
            m11=int(menp.loc[0,'m11'])
            m12=int(menp.loc[0,'m12'])
            m21=int(menp.loc[0,'m21'])
            m22=int(menp.loc[0,'m22'])
            m31=int(menp.loc[0,'m31'])
            m32=int(menp.loc[0,'m32'])
            m41=int(menp.loc[0,'m41'])
            m42=int(menp.loc[0,'m42'])
            subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    
    
            time.sleep(10)
        
            pyautogui.moveTo(x=m11,y=m12)
            pyautogui.click()
        
            time.sleep(2)
        
            pyautogui.moveTo(x=m21,y=m22)
            pyautogui.click()
    
   
            pyautogui.moveTo(x=m31,y=m32)
            time.sleep(1)
            pyautogui.press("delete")
            pyautogui.write(meetingid)
            pyautogui.press('enter')

            time.sleep(8)
            #Types the password and hits enter
    
            pyautogui.moveTo(x=m41,y=m42)
            pyautogui.click()
            pyautogui.write(pswd)
            pyautogui.press('enter')
    
    
            
        
    
            time.sleep(30)
    
            pyautogui.moveTo(x=0,y=578)
            pyautogui.click()
        
    
   
        df = pd.read_csv('itimings.csv')
        time.sleep(mdiffsec)
        while True:
            # checking of the current time exists in our csv file
            now = datetime.now().strftime("%H:%M:%S")
            if now in str(df['timing']):
                row = df.loc[df['timing'] == now]
                meetingid = str(row.iloc[0,1])
                pswd = str(row.iloc[0,2])
    
                sign_in(meetingid,pswd)
                time.sleep(40)
                print('signed in')
                break
            
            
    var=open("itimings.csv","r+")
    var.truncate(0)
    var.close()
    
    meeo=prev
    print('opening timing',prev)
    meec=erec
    print('erec timing',meec)
    mee4=int(meeo[:2])
    mee5=int(meeo[3:5])
    mee6=int(meeo[6:9])
    mee7=int(meec[:2])
    mee8=int(meec[3:5])
    mee9=int(meec[6:9])
    diff1=abs(mee7-mee4)
    diff2=abs(mee8-mee5)
    diff3=abs(mee9-mee6)
    ediffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
    ediffsec=abs(ediffsec)
    print("ediffsec=",ediffsec)

    def endrecording():
        eenp = pd.read_csv('eenp.csv')
        e11=int(eenp.loc[0,'e11'])
        e12=int(eenp.loc[0,'e12'])
        pyautogui.press('esc')
        time.sleep(2)
        renp = pd.read_csv('renp.csv')
        r11=int(renp.loc[0,'r11'])
        r12=int(renp.loc[0,'r12'])
        r21=int(renp.loc[0,'r21'])
        r22=int(renp.loc[0,'r22'])
        pyautogui.moveTo(x=r11,y=r12)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(x=r21,y=r22)
        pyautogui.click()
        pyautogui.write("qtp")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.moveTo(x=211,y=6)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(x=232,y=75)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(x=e11,y=e12)
        pyautogui.click()
        pyautogui.click()
    
    time.sleep(ediffsec)
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == erec:
            endrecording()
            print("rec ended")
            break
            
def r(): 
    var=open("dqtimings.csv","r+")
    var.truncate(0)
    var.close()
    rec=input("Enter the time you want to start the recording at:")
    dq = open("dqtimings.csv","a",newline="")
    dqwriter=csv.writer(dq)
    dqwriter.writerow(['rec','erec',"p"])
    list2=[rec,0,0]
    dqwriter.writerow(list2)
    dq.close()
    now = datetime.now().strftime("%H:%M:%S")
    print("current time",now)
    dq = pd.read_csv('dqtimings.csv')
    meec=dq.loc[0,"rec"]
    print("rec timing",meec)
    now1=int(now[:2])
    now2=int(now[3:5])
    now3=int(now[6:9])
    mee1=int(meec[:2])
    mee2=int(meec[3:5])
    mee3=int(meec[6:9])
    diff1=abs(mee1-now1)
    diff2=abs(mee2-now2)
    diff3=abs(mee3-now3)
    rdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
    rdiffsec=abs(rdiffsec)
    print("rdiffsec=",rdiffsec)

    def torecordw(a):
        renp = pd.read_csv('renp.csv')
        r11=int(renp.loc[0,'r11'])
        r12=int(renp.loc[0,'r12'])
        r21=int(renp.loc[0,'r21'])
        r22=int(renp.loc[0,'r22'])
        r51=int(renp.loc[0,'r51'])
        r52=int(renp.loc[0,'r52'])
        r61=int(renp.loc[0,'r61'])
        r62=int(renp.loc[0,'r62'])
        pyautogui.moveTo(x=r11,y=r12)
        pyautogui.click()
    
        time.sleep(2)

        pyautogui.moveTo(x=r21,y=r22)
        pyautogui.click()
        pyautogui.write(a)
        pyautogui.press('enter')

        time.sleep(2)

        pyautogui.moveTo(x=211,y=6)
        pyautogui.click()

        time.sleep(2)

        pyautogui.moveTo(x=232,y=75)
        pyautogui.click()
    
        time.sleep(2)

        pyautogui.moveTo(x=r51,y=r52)
        pyautogui.click()

        time.sleep(5)

        pyautogui.moveTo(x=r61,y=r62)
        pyautogui.click()
        pyautogui.click()
    

        time.sleep(2)
    
        pyautogui.moveTo(x=0,y=578)
        pyautogui.click()
        
    
    dq = pd.read_csv('dqtimings.csv')
    time.sleep(rdiffsec)

    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now in str(dq['rec']):
            row = dq.loc[dq['rec'] == now]
            erec= str(row.iloc[0,0])
                
    
            torecordw("qtp")
            time.sleep(1)
            print('rec started')
            break
            
    var=open("dqtimings.csv","r+")
    var.truncate(0)
    var.close()
            
def e():
    var=open("dptimings.csv","r+")
    var.truncate(0)
    var.close()
    erec=input("Enter the time you want to end the recording at:")
    dp = open("dptimings.csv","a",newline="")
    dpwriter=csv.writer(dp)
    dpwriter.writerow(['rec','erec',"p"])
    list2=[0,erec,0]
    dpwriter.writerow(list2)
    dp.close()
    now = datetime.now().strftime("%H:%M:%S")
    print('opening timing',now)
    dp = pd.read_csv('dptimings.csv')
    meec=dp.loc[0,"erec"]
    print('erec timing',meec)
    mee4=int(now[:2])
    mee5=int(now[3:5])
    mee6=int(now[6:9])
    mee7=int(meec[:2])
    mee8=int(meec[3:5])
    mee9=int(meec[6:9])
    diff1=abs(mee7-mee4)
    diff2=abs(mee8-mee5)
    diff3=abs(mee9-mee6)
    ediffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
    ediffsec=abs(ediffsec)
    print("ediffsec=",ediffsec)

    
    def endrecording():
        eenp = pd.read_csv('eenp.csv')
        e11=int(eenp.loc[0,'e11'])
        e12=int(eenp.loc[0,'e12'])
        pyautogui.press('esc')
        time.sleep(2)
        renp = pd.read_csv('renp.csv')
        r11=int(renp.loc[0,'r11'])
        r12=int(renp.loc[0,'r12'])
        r21=int(renp.loc[0,'r21'])
        r22=int(renp.loc[0,'r22'])
        pyautogui.moveTo(x=r11,y=r12)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(x=r21,y=r22)
        pyautogui.click()
        pyautogui.write("qtp")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.moveTo(x=211,y=6)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(x=232,y=75)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(x=e11,y=e12)
        pyautogui.click()
        pyautogui.click()
       
    dp = pd.read_csv('dptimings.csv')
    time.sleep(ediffsec)
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now in str(dp['erec']):
            row = dp.loc[dp['erec'] == now]
            erec= str(row.iloc[0,1])
                

            endrecording()
            time.sleep(1)
            print('rec ended')
            break
            
    var=open("dptimings.csv","r+")
    var.truncate(0)
    var.close()
                
def sande():
    var=open("dktimings.csv","r+")
    var.truncate(0)
    var.close()
    rec=input("Enter the time you want to start the recording at:")
    erec=input("Enter the time you want to end the recording at:")
    dk = open("dktimings.csv","a",newline="")
    dkwriter=csv.writer(dk)
    dkwriter.writerow(['rec','erec',"p"])
    list2=[rec,erec,0]
    dkwriter.writerow(list2)
    dk.close()
    now = datetime.now().strftime("%H:%M:%S")
    print("current time",now)
    dk = pd.read_csv('dktimings.csv')
    meec=dk.loc[0,"rec"]
    print("rec timing",meec)
    now1=int(now[:2])
    now2=int(now[3:5])
    now3=int(now[6:9])
    mee1=int(meec[:2])
    mee2=int(meec[3:5])
    mee3=int(meec[6:9])
    diff1=abs(mee1-now1)
    diff2=abs(mee2-now2)
    diff3=abs(mee3-now3)
    rdiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
    rdiffsec=abs(rdiffsec)
    print("rdiffsec=",rdiffsec)
    def torecordw(a):
        renp = pd.read_csv('renp.csv')
        r11=int(renp.loc[0,'r11'])
        r12=int(renp.loc[0,'r12'])
        r21=int(renp.loc[0,'r21'])
        r22=int(renp.loc[0,'r22'])
        r51=int(renp.loc[0,'r51'])
        r52=int(renp.loc[0,'r52'])
        r61=int(renp.loc[0,'r61'])
        r62=int(renp.loc[0,'r62'])
        pyautogui.moveTo(x=r11,y=r12)
        pyautogui.click()
    
        time.sleep(2)

        pyautogui.moveTo(x=r21,y=r22)
        pyautogui.click()
        pyautogui.write(a)
        pyautogui.press('enter')

        time.sleep(2)

        pyautogui.moveTo(x=211,y=6)
        pyautogui.click()

        time.sleep(2)

        pyautogui.moveTo(x=232,y=75)
        pyautogui.click()
    
        time.sleep(2)

        pyautogui.moveTo(x=r51,y=r52)
        pyautogui.click()

        time.sleep(5)

        pyautogui.moveTo(x=r61,y=r62)
        pyautogui.click()
        pyautogui.click()
    

        time.sleep(2)
    
        pyautogui.moveTo(x=0,y=578)
        pyautogui.click()
        
    
    dk = pd.read_csv('dktimings.csv')
    time.sleep(rdiffsec)
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now in str(dk['rec']):
            row = dk.loc[dk['rec'] == now]
            rec= str(row.iloc[0,0])
                
    
            torecordw("qtp")
            time.sleep(10)
            print('rec started')
            break
    dk = pd.read_csv('dktimings.csv')
    meeo=dk.loc[0,"rec"]
    print('opening timing',meeo)
    dk = pd.read_csv('dktimings.csv')
    meec=dk.loc[0,"erec"]
    print('erec timing',meec)
    mee4=int(meeo[:2])
    mee5=int(meeo[3:5])
    mee6=int(meeo[6:9])
    mee7=int(meec[:2])
    mee8=int(meec[3:5])
    mee9=int(meec[6:9])
    diff1=abs(mee7-mee4)
    diff2=abs(mee8-mee5)
    diff3=abs(mee9-mee6)
    ediffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
    ediffsec=abs(ediffsec)
    print("ediffsec=",ediffsec)        
    def endrecording():
        eenp = pd.read_csv('eenp.csv')
        e11=int(eenp.loc[0,'e11'])
        e12=int(eenp.loc[0,'e12'])
        pyautogui.press('esc')
        time.sleep(2)
        renp = pd.read_csv('renp.csv')
        r11=int(renp.loc[0,'r11'])
        r12=int(renp.loc[0,'r12'])
        r21=int(renp.loc[0,'r21'])
        r22=int(renp.loc[0,'r22'])
        pyautogui.moveTo(x=r11,y=r12)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(x=r21,y=r22)
        pyautogui.click()
        pyautogui.write("qtp")
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.moveTo(x=211,y=6)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(x=232,y=75)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(x=e11,y=e12)
        pyautogui.click()
        pyautogui.click()
        
    dk = pd.read_csv('dktimings.csv')
    time.sleep(ediffsec)
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now in str(dk['erec']):
                row = dk.loc[dk['erec'] == now]
                erec= str(row.iloc[0,1])
                
    
                endrecording()
                time.sleep(10)
                print('rec ended')
                break


    var=open("dktimings.csv","r+")
    var.truncate(0)
    var.close()
                
                
                
                
                
                
                
def jm():
    var=open("datimings.csv","r+")
    var.truncate(0)
    var.close()
    n=int(input("Enter the number of meetings do you want to join?:"))
    for i in range(1,n+1):
        da = open("datimings.csv","a",newline="")
        print("For Meeting",i)
        print("Time")
        print("Please Enter Time in HH:MM:SS Format and in 24 Hour-Clock Time")
        a=input("Enter the time you want to start the meeting at:")
        print(a)
        print('Meeting ID')
        b=int(input("Enter Meeting Id:"))
        print(b)
        c=input("Enter Meeting password:")
        print(c)
        dawriter=csv.writer(da)
        dawriter.writerow(['timing','meetingid','pswd'])
        list1=[a,b,c]
        dawriter.writerow(list1)
        da.close()
        ski1=0
    for i in range(1,n+1):
        if i==1:
            print("i=1")
            da = pd.read_csv('datimings.csv')
            meeo=datetime.now().strftime("%H:%M:%S")
            print('opening timing',meeo)
            meec=da.loc[0,"timing"]
            print('closing timing',meec)
            mee4=int(meeo[:2])
            mee5=int(meeo[3:5])
            mee6=int(meeo[6:9])
            mee7=int(meec[:2])
            mee8=int(meec[3:5])
            mee9=int(meec[6:9])
            diff1=abs(mee7-mee4)
            diff2=abs(mee8-mee5)
            diff3=abs(mee9-mee6)
            odiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
            odiffsec=abs(odiffsec)
            print("mdiffsec=",odiffsec)
            prev=meec
        if i>1 and i<=n:
            ski1=ski1+2
            da = pd.read_csv('datimings.csv')
            print("i=",i)
            print('opening timing',prev)
            meeo=prev
            meec=da.loc[ski1,"timing"]
            print('closing timing',meec)
            mee4=int(meeo[:2])
            mee5=int(meeo[3:5])
            mee6=int(meeo[6:9])
            mee7=int(meec[:2])
            mee8=int(meec[3:5])
            mee9=int(meec[6:9])
            diff1=abs(mee7-mee4)
            diff2=abs(mee8-mee5)
            diff3=abs(mee9-mee6)
            odiffsec=((diff1*60*60)+(diff2*60)+(diff3))-120
            odiffsec=abs(odiffsec)
            print("mdiffsec=",odiffsec)
            prev=meec
            
            
        def sign_in(meetingid,pswd):
            menp = pd.read_csv('menp.csv')
            m11=int(menp.loc[0,'m11'])
            m12=int(menp.loc[0,'m12'])
            m21=int(menp.loc[0,'m21'])
            m22=int(menp.loc[0,'m22'])
            m31=int(menp.loc[0,'m31'])
            m32=int(menp.loc[0,'m32'])
            m41=int(menp.loc[0,'m41'])
            m42=int(menp.loc[0,'m42'])
            subprocess.call(["/usr/bin/open", "/Applications/zoom.us.app"])
    
    
            time.sleep(10)
      
            pyautogui.moveTo(x=m11,y=m12)
            pyautogui.click()
        
            time.sleep(2)
        
            pyautogui.moveTo(x=m21,y=m22)
            pyautogui.click()
    
   
            pyautogui.moveTo(x=m31,y=m32)
            time.sleep(1)
            pyautogui.press("delete")
            pyautogui.write(meetingid)
            pyautogui.press('enter')
            
    
            time.sleep(8)
            #Types the password and hits enter
    
            pyautogui.moveTo(x=m41,y=m42)
            pyautogui.click()
            pyautogui.write(pswd)
            pyautogui.press('enter')
    

    
            time.sleep(2)
    
            pyautogui.moveTo(x=0,y=578)
            pyautogui.click()
        
        da = pd.read_csv('datimings.csv')
        time.sleep(odiffsec)
        while True:
            # checking of the current time exists in our csv file
            now = datetime.now().strftime("%H:%M:%S")
            if now in str(da['timing']):
                row = da.loc[da['timing'] == now]
                meetingid = str(row.iloc[0,1])
                pswd = str(row.iloc[0,2])
    
                sign_in(meetingid,pswd)
                time.sleep(10)
                print('signed in')
                break
            
            
    var=open("datimings.csv","r+")
    var.truncate(0)
    var.close()

          
print("""THE SCHEDULER:Zoom and Quick Time Player Automation Bot
1.Delete the previous mouse inputs and/or add another
2.Delete the previous  Default Inputs and input new deafult Time,Meeting ID and Password
3.Record zoom meeting and join the meeting automatically according to the deafult Time,Meeting ID and Password
4.Record and join the zoom meeting according to your input
5.Start screen Recording
6.End Screen Recording
7.Start and End Screen Recording
8.Join Meeting
9.ENTER ANOTHER OPTION
10.Exit""")  
    
print("write numbers only in this ques:")
ip=int(input("Choose your option:"))    
if ip==1:
    mtruncateandadd()
    print("please give your ans in yes or no")
    cont=str(input("Do you want to continue?"))
elif ip==2:
    truncateandadd()
    print("please give your ans in yes or no")
    cont=str(input("Do you want to continue?"))
elif ip==3:
    defaultwork()
    print("please give your ans in yes or no")
    cont=str(input("Do you want to continue?"))
elif ip==4:
    inputwork()
    print("please give your ans in yes or no")
    cont=str(input("Do you want to continue?"))
elif ip==5:
    r()
    print("please give your ans in yes or no")
    cont=str(input("Do you want to continue?"))
elif ip==6:
    e()
    print("please give your ans in yes or no")
    cont=str(input("Do you want to continue?"))
elif ip==7:
    sande()
    print("please give your ans in yes or no")
    cont=str(input("Do you want to continue?"))
elif ip==8:
    jm()
    print("please give your ans in yes or no")
    cont=str(input("Do you want to continue?"))
elif ip==9:
    print("loading...")
    cont="yes"
elif ip==10:
    print("Thank You for using The Scheduler")
    cont="no"
else:
    cont="yes"




   
while cont=="yes":
        print("""THE SCHEDULER:Zoom and Quick Time Player Automation Bot
1.Delete the previous mouse inputs and/or add another
2.Delete the previous  Default Inputs and input new deafult Time,Meeting ID and Password
3.Record zoom meeting and join the meeting automatically according to the deafult Time,Meeting ID and Password
4.Record and join the zoom meeting according to your input
5.Start screen Recording
6.End Screen Recording
7.Start and End Screen Recording
8.Join Meeting
9.ENTER ANOTHER OPTION
10.Exit""")
        print("write numbers only in this ques:")
        ip=int(input("Choose your option:"))
        if ip==1:
            mtruncateandadd()
            print("please give your ans in yes or no")
            cont=str(input("Do you want to continue?"))
        elif ip==2:
            truncateandadd()
            print("please give your ans in yes or no")
            cont=str(input("Do you want to continue?"))
        elif ip==3:
            defaultwork()
            print("please give your ans in yes or no")
            cont=str(input("Do you want to continue?"))
        elif ip==4:
            inputwork()
            print("please give your ans in yes or no")
            cont=str(input("Do you want to continue?"))
        elif ip==5:
            r()
            print("please give your ans in yes or no")
            cont=str(input("Do you want to continue?"))
        elif ip==6:
            e()
            print("please give your ans in yes or no")
            cont=str(input("Do you want to continue?"))
        elif ip==7:
            sande()
            print("please give your ans in yes or no")
            cont=str(input("Do you want to continue?"))
        elif ip==8:
            jm()
            print("please give your ans in yes or no")
            cont=str(input("Do you want to continue?"))
        elif ip==9:
            print("loading...")
            cont="yes"
        elif ip==10:
            print("Thank You for using The Scheduler")
            cont="no"
            break
        





    
            















