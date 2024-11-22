set term png
set output 'queue_delay_sender.png'
set xlabel 'Dequeue Time (s)'
set ylabel 'Queueing Delay (s)'
plot 'que_del_out.txt' using 1:2 with lines title 'queue delay vs Time'
