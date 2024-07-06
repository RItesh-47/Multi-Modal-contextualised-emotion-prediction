import moviepy.editor as mp
import csv, sys, os

def create_csv(filename, fields, csv_rows):
	with open(filename, 'w') as csvfile: 
		csvwriter = csv.writer(csvfile) 
		csvwriter.writerow(fields) 
		csvwriter.writerows(csv_rows)

#command line arguments
utterance_transcript = sys.argv[1]
moviename= sys.argv[2]
flag= sys.argv[3]
together= sys.argv[4]

#hyperparameters
utterances_in_context= 12
start_buffer= 0.5
end_buffer= 0.5

#initialisations
f = open(str(utterance_transcript))
utterance_timestamps=[]
truncated_context_timestamps=[]
context_csv=[]
times_csv=[]
time_1=0
time_2=0
fields_utterance = ['start_time','end_time','rename_to']
fields_context = ['start_time','end_time','rename_to']
fields_times= ['utterance_start_time', 'utterance_end_time',  'context_start_time', 'context_end_time', 'utterance_name','context_name', 'deleted']
w = []
w2=[]
t = 0
t_old =0
utterances_csv=[]

if(flag=='0'):	 # This is for srt utterance file 	
	for i, x in enumerate(f):
		if(len(x)<3): 
			continue
		if(x[2]==':'):
			y = x.split(':')
			y= y[0:3]
			y[2]= y[2][:-11]
			if len(y) <= 1:
				continue
			t_old = t
			t = int(y[0])*60*60 + int(y[1]) * 60 + int(y[2])
			w.append([t_old, t-t_old, str(str(utterance_transcript[:-4]) + str(i//2))])
   
if(flag=='1'):	#This is for youtube transcript utterance file 
	for i, x in enumerate(f):
		if x[0].isdigit():
			y = x.split(':')
			if len(y) <= 1:
				continue
			t_old = t
			if len(y) == 2:
				t = int(y[0])*60 + int(y[1]) 
			else:
				t = int(y[0])*60*60 + int(y[1]) *60 + int(y[2])
			w.append([t_old, t-t_old, str(str(utterance_transcript[:-4]) + str(i//2))])
			utterances_csv.append([t_old, t, moviename[:-4]+"_utterance"+ str(i//2)])
        
for i in range(len(utterances_csv)):
    if(i==0):
        continue
    t=[int(utterances_csv[i][0]),int(utterances_csv[i][1])]
    utterance_timestamps.append(t)
    
print(len(utterance_timestamps))
truncated_utterance_timestamps= utterance_timestamps[utterances_in_context:] # 0 to 49 numbered utterances are removed 
for i in range(len(truncated_utterance_timestamps)):
    truncated_utterance_timestamps[i][0]= truncated_utterance_timestamps[i][0]-start_buffer
    truncated_utterance_timestamps[i][1]= truncated_utterance_timestamps[i][1]+end_buffer

for i in range(len(truncated_utterance_timestamps)):
    t=[max(0,utterance_timestamps[i][0]-start_buffer),truncated_utterance_timestamps[i][1]]
    truncated_context_timestamps.append(t)
    context_csv.append([t[0], t[1],  moviename[:-4]+"_context"+ str(i//2)])
    times_csv.append([truncated_utterance_timestamps[i][0], truncated_utterance_timestamps[i][1],truncated_context_timestamps[i][0], truncated_context_timestamps[i][1],moviename[:-4]+"_utterance"+ str(i), moviename[:-4]+"_context"+ str(i),0 ])
#start time of context video of ith utterance should be start time of (i-50)th utterance, and end time should be end time of utterance 

# print(len(truncated_utterance_timestamps), len(truncated_context_timestamps))
utterances_csv= utterances_csv[utterances_in_context:]
print(utterances_csv[0:20])

create_csv('utterance.csv',fields_utterance, utterances_csv)
create_csv('context.csv',fields_context, context_csv)
create_csv('times.csv',fields_times, times_csv)

for i in range(len(truncated_context_timestamps)):
    time_2+= truncated_context_timestamps[i][1]-truncated_context_timestamps[i][0]
    time_1+= truncated_utterance_timestamps[i][1]-truncated_utterance_timestamps[i][0]
    
if(len(truncated_context_timestamps)!=len(truncated_utterance_timestamps)):
    	print("Stop, recheck")
print("Average length of utterance video is ", time_1/len(truncated_utterance_timestamps ))
print("Average length of context video is ", time_2/(60*len(truncated_context_timestamps )))

video = mp.VideoFileClip(moviename)

if(together=='1'):
    ind=1
    for i in range(len(truncated_utterance_timestamps)):
        c = video.subclip(truncated_utterance_timestamps[i][0],truncated_utterance_timestamps[i][1])
        c1 = video.subclip(truncated_context_timestamps[i][0],truncated_context_timestamps[i][1])
        c.write_videofile(moviename[:-4]+"_utterance"+str(ind)+".mp4")
        c1.write_videofile(moviename[:-4]+"_context"+str(ind)+".mp4")
        ind+=1    
elif(together=='0'):
    ind=1
    for segment in truncated_utterance_timestamps:
        c = video.subclip(segment[0],segment[1])
        c.write_videofile(moviename[:-4]+"_utterance"+str(ind)+".mp4")
        ind+=1    
    ind=1
    for segment in truncated_context_timestamps:
        c = video.subclip(segment[0],segment[1])
        c.write_videofile(moviename[:-4]+"_context"+str(ind)+".mp4")
        ind+=1    
  
cwd= os.getcwd()
cmd = 'mkdir ' + moviename[:-4]
os.system(cmd)
os.chdir(cwd+ '/' + moviename[:-4])
cmd = 'mkdir utterances_' + moviename[:-4]
os.system(cmd)
cmd = 'mkdir context_' + moviename[:-4]
os.system(cmd)
