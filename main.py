input_queue = ["S Mary", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe", "P Dee", "E Vicky", "E George", "P Dee",
"P Joe", "E Sally", "P Joe", "S Pete", "P Dee", "S Bill", "S Chase", "E Price", "P Dee", "E Sue", ]

p_queue = []
s_queue = []
e_queue = []
num_packets_input = len(input_queue)
# the number in the queue
print(num_packets_input)

# a function that print an item from the queue
def print_1(queue_in):
    count = 0
    try:
        while count < 1:
            print(queue_in[0])
            queue_in.pop(0)
            count += 1
    except:
        return

# a function that print 2 items from the queue
def print_2(queue_in):
    count = 0
    try:
        while count < 2:
            print(queue_in[0])
            queue_in.pop(0)
            count += 1
    except:
        return

# a function that print 3 items from the queue
def print_3(queue_in):
    count = 0
    try:
        while count < 3:
            print(queue_in[0])
            queue_in.pop(0)
            count += 1
    except:
        return

# set apart different three types of items which are assign in the first letter of queue
for x in range(num_packets_input):
    packet_in = input_queue[x]
    pclass = packet_in[0]
    if pclass == "P":
        p_queue.append(input_queue[x])
    elif pclass == "S":
        s_queue.append(input_queue[x])
    else:
        e_queue.append(input_queue[x])
# repeat print three P's and two S's and so on until the queue is empty.
while num_packets_input >= 0:
     print_3(p_queue)
     print_2(s_queue)
     print_1(e_queue)
     num_packets_input -= 1
