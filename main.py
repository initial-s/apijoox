from object import Object
import json

joox = Object()

keywords = raw_input("Masukkan Judul / Artis Lagu : ")
data  = joox.songinfoResults(songid=str(keywords))
data1 = ({"results":data,"status":"200"})
print data1
print "==========="