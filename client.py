from socket import *
import sys
import time
import math
from xml.etree.ElementTree import tostring

argv = sys.argv
filename = argv[1]

def reciever (filename):
    
    bytesToSend = str.encode(filename)
    serverAddressPort = ("127.1", 15000)
    bufferSize = 2048

    # Create a UDP socket at client side
    UDPClientSocket = socket(AF_INET, SOCK_DGRAM)

    def collecting_packets(packet_list):
        data_list=[i[4:-4] for i in packet_list]
        #print(type(data_list[2]))
        file = b''
        for data in data_list:
            file = file+data
            file2 = open('received.png', 'wb')
        #print(type(file))
        # writing encrypted data in in file
        file2.write(file)
        file2.close()
        return file

    # Send to server using created UDP socket
    packet_list = []

    UDPClientSocket.sendto(bytesToSend, serverAddressPort)

    print('recieving...')

    UDPClientSocket.settimeout(1)

    Current_packet_ID = 0

    while True:
    
        window_packet_list = []
        while True:
            try:
                packet = UDPClientSocket.recvfrom(bufferSize)
                #print(int.from_bytes(packet[0][0:2],'big'))
            except:
                break
            
        
            window_packet_list.append(packet[0])

        for pack in window_packet_list:
            # Sending ACK to server
            packet_ID = int.from_bytes(pack[0:2],'big')

            if packet_ID == Current_packet_ID:
                UDPClientSocket.sendto(pack[0:4], serverAddressPort)

            #print("packet {} ACK sent".format(packet_ID))

                packet_list.append(pack)

                Current_packet_ID +=1
                previousACK = pack[0:4]

            else:
                UDPClientSocket.sendto(previousACK, serverAddressPort)
                print("packet {} ACK failed".format(Current_packet_ID))
                break

        if packet_list[-1][-4::] == (1).to_bytes(4,'big'):
            break

    print('saving...')
    image = collecting_packets(packet_list)
    print("{} recieved successfuly".format(filename))
    print("{} packets recieved".format(len(packet_list)))

reciever (filename)