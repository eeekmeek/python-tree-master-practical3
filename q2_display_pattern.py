# Displaying patterns

def display_pattern(n):
    line = []
    last = []
    for i in range (n+1):
        num = str(i)
        last.insert(1,num)
        lastline = ' '.join(last)
        
    for i in range (n+1):
        num = str(i)
        line.insert(1,num)
        newline = ' '.join(line)
        print (newline.rjust(len(lastline)))
    
display_pattern(20)
