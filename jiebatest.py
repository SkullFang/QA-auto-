# encoding:utf-8

import sys
import jieba
import string
import re
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf-8')  # 设置默认编码为utf-8


## 计算词频的例子
def com_tf():
    f = open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/answer.txt', 'r')
    finn=open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/testanswer.txt', 'a')
    fin = open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/disanswer.txt', 'a+')
    f1=open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/disquestion.txt','r')
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
            # print string1[i][j]+'\n'
    # print len(string1)
    # print string1[0][2]
    # print string1[1][0]
    # for st in string1[1:-1]:
    #     print str(st)
    # while True:
    #     line=f1.readline()
    #     if line:
    #         s=s+1
    #     else:
    #         break
    # f1.close()
    # print s

    # lines=f.readlines()
    # i=0
    # for line in lines:
    #     i = i + 1
    #     finn.write(str(i) + '\t' + line + '\n')

    # i=0
    # while True:
    #     line=f.readline()
    #     if line:
    #         i=i+1
    #         data=f.readline()
    #         finn.write(str(i)+'\t'+data+'\n')
    #     else:
    #         break
    # print i

    # s=0
    # for line in lines:
    # #     s = s + 1
    #     data = line
    #     data_temp = data.decode('utf-8')
    #     data = ''.join(re.findall(u'[\u4e00-\u9fff]+', data_temp))
    #     data2 = jieba.cut(data)
    #     data3 = " ".join(data2)
    #     fin.write(str(s) + '\t' + data3 + '\n')



    #
    # s=0
    # while True:
    #     line=f.readline()
    #     if line:
    #         s=s+1
    #         data = f.readline()
    #         data_temp = data.decode('utf-8')
    #         data = ''.join(re.findall(u'[\u4e00-\u9fff]+', data_temp))
    #         data2 = jieba.cut(data)
    #         data3 = " ".join(data2)
    #         fin.write(str(s)+"\t"+data3 + '\n')
    #     else:
    #         break
    # f.close()
    # print s

# def testread():
#     f = open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/answer.txt', 'r')
#     line = f.readline()
#     print line




    # data_temp = data.decode('utf-8')  # 转换为unicode编码形式
    # data = ''.join(re.findall(u'[\u4e00-\u9fff]+', data_temp))  # 必须为unicode类型，取出所有中文字符
    # # sts = data.translate(None, string.punctuation)            # 删除英文的标点符号，中文标点不支持。
    #
    # data2 = jieba.cut(data)  # 分词
    # data3 = " ".join(data2)  # 结果转换为字符串（列表转换为字符串）
    #
    # fin.write(data3+'\n')  # 分词结果写入7temp.txt
    #
    # wlist = data3.split()      # 将分词结果按空格切割为列表（字符串的切割）
    # num_dict = Counter(wlist)  # 统计词频

    # 统计结果写入result.txt(字典的遍历)
    # for (k, v) in num_dict.items():
    #     open('data/result.txt', 'a+').write(str(k) + ' ' + str(v) + '\n')   # 将k，v转换为str类型


if __name__ == '__main__':
    com_tf()
    # f = open('/Users/zhangyan/Desktop/Learning/BoP2017_DBAQ_dev_train_data/disanswer.txt', 'r')
    # line = f.readline()
    # print line

