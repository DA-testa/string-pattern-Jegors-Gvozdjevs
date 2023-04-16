def read_input():
    fileorno = input().rstrip()
    if fileorno== 'I':
        inp= input().rstrip()
    elif fileorno== 'F':
        file= input().rstrip()
        with open("tests/6"+file, 'r') as F:
            inp=F.readline().rstrip()
    else:
        raise ValueError('Invalid input type: {}'.format(fileorno))
    
    pattern = inp.rstrip()
    text = input().rstrip()

    return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    

    per= 101
    nums= 256
    occurences= []
    ph= 0
    th= 0
    p= 1



    for i in range(len(pattern)):
        ph= (ph*nums + ord(pattern[i]))%per
        text_hash = (th*nums+ ord(text[i]))%per
        if i>0:
            p= (p*nums)%per



    for i in range(len(text) - len(pattern) + 1):
        if ph ==th:
            bool= True
            for j in range(len(pattern)):
                if text[i+j]!=pattern[j]:
                    bool= False
                    break
            if bool:
                occurences.append(i)




        if i < len(text) - len(pattern):
            th=((th-ord(text[i])*p)*nums+ ord(text[i+len(pattern)])) %per
            if th< 0:
                th+= per



    return [0]


# This part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

