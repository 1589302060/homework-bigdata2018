import re
import string
import matplotlib.pyplot as plt#下载了一些，相信应该都有吧
import numpy as np
import os
#图中所有被注释掉的print均为辅助数据，实际运行中可选择的显示，为了避免显示过多，将大多数的print注释掉了
def readname():
    filePath = 'C:\\Users\\15893\\Desktop\\320180941141-juyida\\homework10'#该路径为我电脑中数据文件的存放路径，需要修改
    if not os.path.isdir(filePath):#修改的时候记得要是双斜杠或反斜杠
        print('Error: "', filePath, '" is not a directory or does not exist.')
    name = os.listdir(filePath)
    return name

def text_save(filename,data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    #    file.close()
    #    print("保存文件成功")


    #print(data2[1])
    #return data2
def plots():#设计了此功能，慎用，用途为分析文件中的具体三维加速度数据，但会导致电脑严重卡顿
    plt.plot(x)
    plt.show()
    plt.plot(y)
    plt.show()
    plt.plot(z)
    plt.show()

if __name__ == "__main__":
    name = readname()
    print(name)
    for i in name:
        print(i)
l=0
q=0
w=0
#fi = open("namedata.txt", "r")
finvari = list(range(201))
fintime = list(range(201))
err1 =  list(range(100))
err2 =  list(range(100))
while l<198 and 'json'in name[l]:#循环，批量处理文件中所有json数据

    file = name[l]
    l+=1
    kind='0'
    if 'device' in file:
        kind='device'
    if 'gyroscope' in file:
        kind="gyroscope"
    if 'accelerometer' in file:
        kind="accelerometer"
#    print(kind)
# 关键字1,2(修改引号间的内容)
    w1 = ':'
    w2 = ','
    f = open(file, 'r',encoding='UTF-8')
    buff = f.read()
    pat = re.compile(w1 + '(.*?)' + w2, re.S)
    result = pat.findall(buff)
#    print(result)
#print(result.replace('}', ''))
    count1=int(len(result))
    if count1<100:#避免因为空数据使得下文报错
        break
    print(count1)
    time=count1/5
    fintime[l]=time
#    print("回答问卷用时约为",time,"秒")
    if time<500 or time>4800:
        #print("问卷用时异常，判断为无效问卷")
        err1[q]=file
        q+=1
    #if count1<1000:
     #   print("该组数据量过小，被认定为无效数据")

    i=0
    j=0
    x = list(range(int((count1/3))))
    y = list(range(int((count1/3))))
    z = list(range(int((count1/3))))
    z1 = list(range(int((count1/3))))

    xsum=0.0000
    ysum=0.0000
    zsum=0.0000
    xvari=0.0#方差的缩写，在实际计算中没用方差公式，平均值基于水平
    yvari=0.0
    zvari=0.0
    xvari2=0.0#方差的缩写，平均值为实际数值
    yvari2=0.0
    zvari2=0.0
#print(x[1])
    while i<count1-2:
        x[j]=result[i]
        xsum+=float(result[i])
        xvari+=float(result[i])*float(result[i])
        y[j]=result[i+1]
        ysum+=float(result[i+1])
        yvari+=float(result[i+1])*float(result[i+1])
        z[j]=result[i+2]
    #znumber+=float(result[i+2])
        i=i+3
        j+=1
    #print(x)
    #print(y)
    #print(z)
    z1 = list(map(lambda x : re.sub("}", '', x), z))
#    print(z1)
    i=0
    while i<count1/3-1:
        zsum+=float(z1[i])
        zvari+=float(z1[i])*float(z1[i])
        i+=1
    #plt.scatter(x, y, s=3)         #二维好似意义不大吧
    #plt.show()

#plots()             #如果想使用上面被注掉的def plots()的话，请将这行开头的＃去掉，不过我没敢试，一个json的数据都会卡pycharm一会，不敢想象100个。
    xave=xsum/int(count1/3)
    yave=ysum/int(count1/3)
    zave=zsum/int(count1/3)
 #   print("平均值")
  #  print(xave)
   # print(yave)
    #print(zave)
   # print("基于水平面的类方差")
    #print(xvari/int(count1/3))
   # print(yvari/int(count1/3))
    #print(zvari/int(count1/3))
    i=0
    while i<count1/3-1:
        xvari2+=(float(x[i])-xave)*(float(x[i])-xave)
        i+=1
    i=0
    while i<count1/3-1:
        yvari2+=(float(y[i])-yave)*(float(y[i])-yave)
        i+=1
    i=0
    while i<count1/3-1:
        zvari2+=(float(z1[i])-zave)*(float(z1[i])-zave)
        i+=1
 #  print(xvari2/int(count1/3))
  #  print(yvari2/int(count1/3))
   # print(zvari2/int(count1/3))
    finvari[l]=xvari2/int(count1/3)+yvari2/int(count1/3)+zvari2/int(count1/3)
    if l%3!=2:
        if finvari[l]>0.6:
            err2[w]=file
            w+=1
    if l%3==2:
        if finvari[l]>5000:
            err2[w]=file
            w+=1
#print(finvari)
#print(fintime)
plt.plot(finvari)#加速度方差
plt.show()
plt.plot(fintime)#实验时间
plt.show()
print(err1)
print(err2)

text_save('errdata1.txt',err1)
text_save('errdata2.txt',err2)