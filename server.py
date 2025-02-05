from socket import *
import sys
import random
import math
import time
from xml.etree.ElementTree import tostring

argv = sys.argv
localIP = argv[1]
localPort = argv[2]

def sender (localIP, localPort):
  #localIP     = "127.1"
  #localPort   = 15000
  bufferSize  = 2048

  # Create a datagram socket

  UDPServerSocket = socket(AF_INET, SOCK_DGRAM)

  # Bind to address and ip
  UDPServerSocket.bind((localIP, localPort))


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
    n=math.ceil(len(file_data)/mss)
    file_list=list()
    for i in range(n):
      if i==n-1:
        file_list.append(i.to_bytes(2,'big')+fileIPBytes+file_data[i*mss::]+(1).to_bytes(4,'big'))
      else:
        file_list.append(i.to_bytes(2,'big')+fileIPBytes+file_data[i*mss:(i+1)*mss]+(0).to_bytes(4,'big'))
    return file_list

  # Listen for incoming datagrams
  packet_list = []

  print("UDP server up and listening")

  while (True):
 
    try:
      bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    except KeyboardInterrupt:
      print("shutting down")
      break
    except:
      continue

    filename = bytesAddressPair[0].decode()

    address = bytesAddressPair[1]


    print("file {} requested".format(filename))
    print("Client IP Address:{}".format(address))

    N = 10

    NumberOfPackets = 0

    w_start = 0
    w_end = N

    packet_list = packeting(filename,10)

    previous_packet_ID = -1

    percentage_Loss = random.randint(5,15)

    UDPServerSocket.settimeout(5)

    while(True):

      for packet in packet_list[w_start:w_end]:
        # Sending a reply to client
        Loss_factor = random.randint(0,100)
        if Loss_factor > percentage_Loss:
      
          UDPServerSocket.sendto(packet, address)
          NumberOfPackets +=1

      while(True):

        try:
          ACK_address = UDPServerSocket.recvfrom(bufferSize)
        except:
          print('Time out.. \n resending..')
          break


        packet_ID = int.from_bytes(ACK_address[0][0:2],'big')
        if packet_ID == previous_packet_ID:
          break
        else:
          #print("packet {} Ack'd".format(packet_ID))
          previous_packet_ID = packet_ID
        if packet_ID == w_end-1:
          break
      
      print("last packet Ack'd is ",(previous_packet_ID), " out of ",len(packet_list))

      if previous_packet_ID == len(packet_list)-1:
        break

      w_start = previous_packet_ID + 1
      if w_start + N >= len(packet_list):
        w_end = len(packet_list)
      else:
        w_end = w_start + N

    print("{} packets sent".format(NumberOfPackets))
    print("{} sent successfuly".format(filename))

    print("UDP server up and listening")

sender (localIP , int(localPort))




   

       