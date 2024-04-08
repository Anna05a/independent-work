def check_sequence(sequence):
    
    i = 0
    while i < len(sequence):
        
        count_zero = 0
        while i < len(sequence) and sequence[i] == '0':
            count_zero += 1
            i += 1
        
        
        if i == len(sequence):
            return False
        
        
        count_one = 0
        while i < len(sequence) and sequence[i] == '1':
            count_one += 1
            i += 1
        
        
        if count_zero != count_one:
            return False
    
    return True


sequence1 = "01010101"
sequence2 = "00011100011"
result1 = check_sequence(sequence1)
result2 = check_sequence(sequence2)
print("Послідовність 1:", result1)
print("Послідовність 2:", result2)
