def sort_split (my_list):
    my_list.sort()
    
    chunk_len = len(my_list) / 3
    extra = len(my_list) % 3
    
    chunks = []
    begin = 0 
    
    if extra==1:
        chunks.append(my_list[0:chunk_len+1])
        begin = chunk_len+1
        chunks.append(my_list[begin:begin+chunk_len])
        begin = begin+chunk_len
        chunks.append(my_list[begin:begin+chunk_len])

    elif extra==2:
        chunks.append(my_list[0:chunk_len+1])
        begin = chunk_len+1
        chunks.append(my_list[begin:begin+chunk_len+1])
        begin = begin+chunk_len+1
        chunks.append(my_list[begin:begin+chunk_len])

    else:
        chunks.append(my_list[0:chunk_len])
        begin = chunk_len
        chunks.append(my_list[begin:begin+chunk_len])
        begin = begin+chunk_len
        chunks.append(my_list[begin:begin+chunk_len])

    return chunks


chunks_result = sort_split([1,2])
print chunks_result
