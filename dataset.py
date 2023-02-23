import random
import csv

def calculate(m,r,h,s,t,a,u):
    cal= m+r+h+s+t+a+u
    score=0
    if cal  >= 7 :
        score = 4
    elif cal in [5,6] :
        score = 3
    elif cal in [3,4] :
        score = 2
    elif cal in [0,2]:
        score =1
    return score


with open('./all/datasets/dataset.csv','w',encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Score','Mobility','RR','HR','SBP','Temp','AVPU','Trauma'])
    for i in range(1000000):
        m=0;r=0;h=0;s=0;t=0;a=0;u=0
        score=0
        Mobility=random.choice(['Walking','Withhelp','Immobile'])
        RR=random.randint(5,30)
        HR=random.randint(35,135)
        SBP=random.randint(60,210)
        Temp=random.randint(32,42)
        AVPU=random.choice(['Alert','Voice','Pain','Unresponsive'])
        Trauma=random.choice(['Yes','No'])


    #Calculate mobility socre in variable m
        if Mobility == 'Walking' :
            m= 0
        elif Mobility == 'Withhelp' :
            m=1
        elif Mobility == 'Immobile' :
            m=2

    #Calculate respirotary rate in variable r

        if RR < 9 :
            r= 2
        elif RR in [9,14] :
            r= 0
        elif RR in [15,20] :
            r= 1
        elif RR in [21,29] :
            r= 2
        elif RR > 29 :
            r= 3

    #Calculate heart rate in variable h

        if HR < 41 :
            h= 2
        elif HR in [41,50] :
            h= 1
        elif HR in [51,100] :
            h= 0
        elif HR in [101,110] :
            h= 1
        elif HR in [111,129] :
            h= 2
        elif HR > 129 :
            h= 3

    #Calculate systolic blood pressure in variable s

        if SBP < 71 :
            s= 3
        elif SBP in [71,80] :
            s= 2
        elif SBP in [81,100] :
            s= 1
        elif SBP in [101,199] :
            s= 0
        elif SBP > 199 :
            s= 2

    #Calculate temperature in variable t

        if Temp < 35 :
            t= 2
        elif Temp in [35,38] :
            t= 0
        elif Temp > 39 :
            t= 2

    #Calculate AVPU socre in variable a
        if AVPU == 'Alert' :
            a= 0
        elif AVPU == 'Voice' :
            a=1
        elif AVPU == 'Pain' :
            a=2
        elif AVPU == 'Unresponsive' :
            a=2

    #Calculate Trauma socre in variable u
        if Trauma == 'No' :
            u= 0
        elif Trauma == 'Yes' :
            u=1

        score = calculate(m,r,h,s,t,a,u)
        #packet=[score, m,r,h,s,t,a,u]
        packet=[score, m,RR,HR,SBP,Temp,a,u]
        #print('score=',score)
        writer.writerow(packet)

        #file.write(line)
        #file.write('\n')