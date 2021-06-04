from django.shortcuts import render
import pandas as pd

informations=pd.read_csv('courses/Data/courses.csv',sep=',')

def index (request):
    df=pd.DataFrame(informations,columns=['course_name','start_date','teacher','exam_date','price'])
    allData=[]
    for i in range(df.shape[0]):
        temp=df.iloc[i]
        allData.append(dict(temp))
    context= {'Data':allData}
    return render (request,'course_list.html',context)