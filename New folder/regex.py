#algoritma buat nambahin sebuah pattern jadi ada query regexnya
def regex(S):
    S = S.replace('kah', '(kah)?')
    if(S.find('mengapa') != -1):
        S = S.replace('mengapa', 'mengapa|kenapa')
    else:
        S = S.replace('kenapa', 'mengapa|kenapa')
    if(S.find('bagaimana') != -1):
        S = S.replace('bagaimana', 'bagaimana|gimana')
    else:
        S.replace('gimana', 'gimana|bagaimana')
        
    S = S.replace(' ', '.*')
    return S


'''text = 'Apa ibukota negara Filipina'
S = regex('Apakah ibukota Filipina')
x = re.search(S, text)
print(x)'''