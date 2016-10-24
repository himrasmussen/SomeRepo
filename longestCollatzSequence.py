# Longest Collatz sequense (14)
# 837799

def longest_Collatz_sequence(n):
    longest_sequence = 0
    for i in range(n+1, 2, -1): 
        sequence = 0
        m = i
        while m != 1:
            if m % 2 == 0:
                m = m / 2
                sequence += 1
            elif m % 2 == 1:
                m = (m*3) + 1
                sequence += 1
            
        if sequence > longest_sequence:
            longest_sequence = sequence
            longest_sequence_number = i
            print(str(i), str(longest_sequence))
    return longest_sequence, longest_sequence_number

print(str(longest_Collatz_sequence(1000000)))


'''
odd 1,000,000 --> 333,333
even 1,000,000 --> 500,000 -1
'''

