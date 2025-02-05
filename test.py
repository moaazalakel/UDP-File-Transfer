import math
import sys

filename            = "LargFile.jpg"

def packeting(FilePath,fileID):

    
  mtu=1500
  udphdr=8
  iphdr=24
  mss=mtu-udphdr-iphdr
  fileIPBytes=fileID.to_bytes(2, 'big')
  file = open(FilePath, 'rb')
  
  # storing file data in variable "file_data"
  file_data = file.read()
  file.close()
  n = math.ceil(len(file_data)/mss)
  file_list=list()
  for i in range(n):
    if i == n-1:
      file_list.append(i.to_bytes(2,'big')+fileIPBytes+file_data[i*mss::]+(1).to_bytes(4,'big'))
    else:
      file_list.append(i.to_bytes(2,'big')+fileIPBytes+file_data[i*mss:(i+1)*mss]+(0).to_bytes(4,'big'))
  return file_list

packet_list = []
packet_list = packeting(filename,10)

print(int.from_bytes(packet_list[2][0:2],'big'))
