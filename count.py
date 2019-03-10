s = "aabbccc"
dic = {}
for ch in s:
    dic[ch]=1+dic.get(ch,0)
 
print dic
