# Average TCP throughput


# tshark -r tcp-example-0-0.pcap -T fields -e frame.time_epoch -e tcp.len > receiver_packets_N0.txt

# tshark -r tcp-example-1-0.pcap -T fields -e frame.time_epoch -e tcp.len > receiver_packets_N1.txt

# tshark -r tcp-example-2-0.pcap -T fields -e frame.time_epoch -e tcp.len > receiver_packets_N2.txt


def average_throughtput(pcap_file):
    tot_bytes=0
    start_time=None
    end_time=None
    
    
    with open(pcap_file,'r') as file:
        for i in file:
            line=i.strip().split()
            
            if(len(line)<2):
                continue
            
            time_stamp,len_tcp=float(line[0]),float(line[1])
            
            tot_bytes+=len_tcp
            
            if(start_time==None):
                start_time=time_stamp
                
            end_time=time_stamp
            
    duration=end_time-start_time
    throughput=(tot_bytes*8)/(duration*1e6)
    return throughput
    
    
    
            
         
print(f"Throughput for N0 {round(average_throughtput("receiver_packets_N0.txt"),2)} Mbps")

print(f"Throughput for N1 {round(average_throughtput("receiver_packets_N1.txt"),2)} Mbps")

print(f"Throughput for N2 {round(average_throughtput("receiver_packets_N2.txt"),2)} Mbps")            
            
            


