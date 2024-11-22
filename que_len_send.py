import sys

def queue_len_send(trace_file, output_file):
    queue_length = 0
    events = []  

    with open(trace_file, 'r') as file:
        for i in file:
            line = i.strip().split()
            if len(line) < 2:
                    continue
                
            event = line[0]  
            time = float(line[1])  
                
              
            if event == "+":
                queue_length += 1
                    
            elif event == "-":
                 queue_length -= 1
                
            
            events.append((time, queue_length))

    with open(output_file, 'w') as output_file:
        for time, length in events:
            output_file.write(f"{time} {length}\n")
        
    print(f"Queue length data written to {output_file}")
    

if __name__ == "__main__":

    file_trace = sys.argv[1]
    file_output = sys.argv[2]

    queue_len_send(file_trace, file_output)
