import os
import difflib
bad_words = ['#']
with open('mdscash.ini') as oldfile, open('cash.ini', 'w') as newfile:
  for line in oldfile:
    if not any(bad_word in line for bad_word in bad_words):
      newfile.write(line)
with open('mdsold.ini') as oldfile, open('old.ini', 'w') as newfile:
  for line in oldfile:
    if not any(bad_word in line for bad_word in bad_words):
      newfile.write(line)



first="cash.ini"

second="old.ini"

flines= open(first).readlines()

slines= open (second).readlines()

diff=difflib.HtmlDiff().make_file(flines, slines, first, second)

difference_report=open('filter.html','w')

difference_report.write(diff)




difference_report.close