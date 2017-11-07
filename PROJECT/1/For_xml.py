# -*- coding: utf-8 -*-

import  xml.dom.minidom
import sys
import re
import os
import codecs

reload(sys)
sys.setdefaultencoding('utf8')

def get_seg_sentence():
    fw = open('XXX.txt','w')
    fw_label = open('XXX_label.txt','w')

    #文件名
    files = []
    start = "w_xml/cet_"
    end = ".xml"
    for i in range(1487):
        files.append(start + str(i+1) +end)

    for fname in files:
        fr = open(fname, 'r')
        content = fr.read()
        fr.close()
        dom = ""
        #处理格式问题
        if 'encoding="GB2312"' in content:
            content = content.decode('GB2312').encode('UTF-8')
            content = content.replace('encoding="GB2312"', 'encoding="UTF-8"')
            dom = xml.dom.minidom.parseString(content)
        else:
            dom = xml.dom.minidom.parse(fname)
       
        #得到文档元素对象
        root = dom.documentElement  
        #获得标签属性值
        itemlistT = root.getElementsByTagName('title')

        for item in itemlistT:
            sentences = item.getElementsByTagName('Segmented_S')
            if len(sentences)==0:
                continue
            string = sentences[0].firstChild.data
            string = string.replace('/',' ')
            #只提取中文
            p = re.compile(r'\w*',re.L)
            result = p.sub("",string)
            print >> fw,result
            
            emotion = ['Joy','Hate','Love','Sorrow','Anxiety','Surprise','Anger','Expect']
            string1 = ""
            for it in emotion:
                string1 += item.getElementsByTagName(it)[0].firstChild.data+" "
            print >> fw_label,string1