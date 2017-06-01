    ff=open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/BoP2017-DBQA.dev.txt','r')
    fr=open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/rate.txt','a+')
    fq = open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/qu.txt', 'a+')
    fa = open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/an.txt', 'a+')





    i=0
    s=0
    string1=[]
    while True:
        line=ff.readline()
        if line:
            string1.append(line.split('\t'))
        else:
            break
    f.close()

    s=0
    for i in range(0,len(string1)):
        s=s+1
        for j in range(0,3):
            if(j==0):
                fr.write(str(s)+'\t'+string1[i][j]+'\n')
            elif(j==1):
                data = string1[i][j]
                data_temp = data.decode('utf-8')
                data = ''.join(re.findall(u'[\u4e00-\u9fff]+', data_temp))
                data2 = jieba.cut(data)
                data3 = " ".join(data2)
                fq.write(str(s)+'\t'+data3+'\n')
            else:
                data = string1[i][j]
                data_temp = data.decode('utf-8')
                data = ''.join(re.findall(u'[\u4e00-\u9fff]+', data_temp))
                data2 = jieba.cut(data)
                data3 = " ".join(data2)
                fa.write(str(s)+'\t'+data3+'\n')

if __name__ == '__main__':
    com_tf()