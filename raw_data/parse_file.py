#coding=utf-8
#!/usr/bin/env python

import json
import re
f1="E:\\work\\ads\\DeepInterestNetwork\\raw_data\\meta_Electronics_head10.json"
f2="E:\\work\\ads\\DeepInterestNetwork\\raw_data\\reviews_Electronics_5_head10.json"
if __name__=="__main__":
    fr=open(f1,'r')
    cnt=0
    for line in fr:
        if cnt==0:
            cnt+=1
            #line=re.sub("\'","\"",line)
            line=eval(line)
            #print(line)
            for k,v in line.items():
                print("%s:::%s"%(k,v))
            print(type(line))
            #json.loads(line)
        else:
            cnt+=1
