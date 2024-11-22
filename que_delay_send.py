import re

# Input and output file names
trace_file = "tcp-example.tr"
file_output = "que_del_out.txt"

result = {}


queueing_delays = []


with open(trace_file, "r") as file:
    for i in file:
      
        line = i.strip().split()
        if len(line) < 3:
            continue  

      
        operation = line[0]  
        time = float(line[1])
        packet_id_search = re.search(r"TcpHeader.*Seq=(\d+)", i)
        

        if packet_id_search:
            packet_id = packet_id_search.group(1)

            if operation == "+":
             
                result[packet_id] = time
                
            elif operation == "-" and packet_id in result:
               
               
                delay = time - result[packet_id]
                queueing_delays.append((time, delay))
              
              
                del result[packet_id]

with open(file_output, "w") as out_file:
    for dequeue_time, delay in queueing_delays:
        out_file.write(f"{dequeue_time} {delay}\n")


