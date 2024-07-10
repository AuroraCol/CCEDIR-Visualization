# import csv
# file= open('MATH140BObs4-19-24.txt')
# csvreader = csv.reader(file)

# header = []
# header = next(csvreader)
# print(header)
#timer.split(".")[0], '%Y-%m-%dT%H:%M:%S')
#timer.strip("H:%M:%S")
#first start time -> second start time, ..., last start time -> class end time; if start time > class end time, 
#make one minute longer than start time 
#add all start times to a list, order of days, day 1 is type 1, etc. times in hroizontal bar. Type corresponds to number of observations
#per day
#compile all csvs into one, dates labeled via type (add into each), type column corresponds to type section of template


import pandas as pd
import mergeCSVs as merg
import datetime

#data1= pd.read_csv(r"C:\Users\auror\Pictures\SC494Data\Observations",'MATH140BObs04-03-24.txt')
# converting column data to list
timestampCSV = merg.df['Timestamp'].tolist()
obvCodeCSV=merg.df['Code'].tolist()
descCSV=merg.df['Description'].tolist()
instoStCSV=merg.df['Focus'].tolist()

handtimed=merg.df['TextValue'].tolist()
cleanedTimerListCSV = [x for x in handtimed if str(x) != 'nan']

# #code for the given obs, activity
# codeCSV = data1['Code'].tolist()
# #the names for the given codes, labels 
# codeNamesCSV = data1['Description'].tolist()
# #inst or student values 
# instorstudCSV = data1['Focus'].tolist()


# timerDataCSV = data1['TextValue'].tolist()
# cleanedTimerListCSV = [x for x in timerDataCSV if str(x) != 'nan']
 
# printing list data
starttime=[]
#print(timestampCSV)
for index in range(len(timestampCSV)):
    starttime.append(datetime.datetime.strptime(timestampCSV[index].split(".")[0].split("T")[1],'%H:%M:%S'))

#print(starttime)
# print(newtime)

endtime=[]
for i in range(1,len(timestampCSV)):
    if timestampCSV[i-1].split(".")[0].split("T")[0] == timestampCSV[i].split(".")[0].split("T")[0]:
        endtime.append(datetime.datetime.strptime(timestampCSV[i].split(".")[0].split("T")[1],'%H:%M:%S'))
    else:
        endtime.append(datetime.datetime.strptime(timestampCSV[i-1].split(".")[0].split("T")[1],'%H:%M:%S')+datetime.timedelta(seconds=75))

endtime.append(datetime.datetime.strptime(timestampCSV[len(timestampCSV)-1].split(".")[0].split("T")[1],'%H:%M:%S')+datetime.timedelta(seconds=75))
# print(endtime)
# print(len(endtime)==len(timestampCSV))

datelist=[]
for index in range(len(timestampCSV)):
    datelist.append(timestampCSV[index].split(".")[0].split("T")[0])
# print(datelist)
# print(len(starttime)==len(timestampCSV))
dateindex=[]
for index in range(len(datelist)):
    if datelist[index]== '2024-04-03':
        dateindex.append('1')
    elif datelist[index]== '2024-04-05':
        dateindex.append('2')
    elif datelist[index]== '2024-04-12':
        dateindex.append('3')
    elif datelist[index]== '2024-04-17':
        dateindex.append('4')
    elif datelist[index]== '2024-04-19':
        dateindex.append('5')
# print(len(datelist)==len(dateindex))
# print(endtime) 
# print(endtime.index(datetime.datetime(1900, 1, 1, 17, 6, 8)))
# print(endtime[180])
endtime[180] += +datetime.timedelta(minutes=4)
# print(endtime[180])

elapsedtime=[]
for index in range(len(starttime)):
    elapsedtime.append(endtime[index]-starttime[index])
# print(elapsedtime)

timerManual=[5 , 5 , 7, 7, 30, 15, 6, 12 , 27, 4, 11,5 ,10, 14 ,14,10 ,5 ,7, 34 , 8, 9 ,8,10 ,6 ,10 ,22 , 13 , 10 ,13 ,6 ,17,9,20 , 8 ,5 ,6,7 ,10 ,7 ,3,23,7 ,6 ,8 ,10,10,10 ,4 ,5 ,4,7 ,3 ,4 ,8 ,3, 8,5,10,22 ,10,5, 20,4,10,15 ,10 ,27,9,20,10,8,14,17,1 ,4,8,20,3,6,5,7,7,4,8,2 , 8,3,10,7,8,7]
averagemanual=sum(timerManual)/len(timerManual)
print(averagemanual)

# IK
# PE
# AWP
# CQA

timerTool=[]
for index in range(len(elapsedtime)):
    if obvCodeCSV[index]=='IK' or obvCodeCSV[index]=='PE' or obvCodeCSV[index]=='AWP' or obvCodeCSV[index]=='CQA':
        timerTool.append(elapsedtime[index].seconds)

averageTool=sum(timerTool)/len(timerTool)
print(averageTool)

qcount=[0,0]
for index in range(len(obvCodeCSV)):
    if obvCodeCSV[index]== 'IK':
        qcount[0]+=1
    else:
        qcount[1]+=1

print(qcount)
print(qcount[0]/sum(qcount))

