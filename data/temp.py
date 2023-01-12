import os  
import cv2
import numpy

# condition_success = 97

# while True:
#   print(chr(condition_success))
#   if condition_success>=97 & condition_success<=122:
#         os.makedirs('D:\snippy\data\lower ' + chr(condition_success)) # creates folder1 if condition_success is 1
#         condition_success += 1
  
#   else:
#     break


# condition_success = 97
# for i in range(26):
#   path = "D:\snippy\\tokens\\"+ str(i) +".png"
#   print(path)
#   img = cv2.imread(path)
#   path = 'D:\snippy\data\lower ' + chr(condition_success) + "\\" + str(i+3) + ".png"
#   print(path)
#   cv2.imwrite(path ,img)
#   condition_success += 1


condition_success = 65
for i in range(26):
  path = "D:\snippy\\tokens\\"+ str(i) +".png"
  print(path)
  img = cv2.imread(path)
  path = 'D:\snippy\data\\' + chr(condition_success) + "\\" + str(i+3) + ".png"
  print(path)
  cv2.imwrite(path ,img)
  condition_success += 1

# condition_success = 65
# for i in range(26):
#   path = 'D:\snippy\data\\' + chr(condition_success) + "\\" + str(i+1) + ".png"
#   os.remove(path)
#   condition_success += 1