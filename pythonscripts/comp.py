import sys
import difflib
file1 = "old.ini"
file2 = "li.ini"
fristfile=open(file1).readlines()
secondfile=open(file2).readlines()
diff = difflib.HtmlDiff().make_file(fristfile,secondfile,file1,file2)
difference_report=open("repot.html","w")
difference_report.write(diff)
difference_report.close()