import difflib

text1 = r'D:\asr_bengali\data\actual0a.txt'
text2 = r'D:\asr_bengali\data\test1.txt'
f1=open(text1,encoding="utf-8").readlines()
f2=open(text2,encoding="utf-8").readlines()
diff=difflib.HtmlDiff.make_file(f1,f2,text1,text2)
diff_ratio=open("D:\asr_bengali\data\test2.html")
diff_ratio.write(diff)
diff_ratio.close()
