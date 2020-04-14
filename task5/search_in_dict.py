from my_str_cmp import compare
#поиск определнного значения
def d_search_on_val(S1, S2, D):
    tL=[]
    for i in D.keys():
        if str(D[i][S1])==S2:           
            tL.append({i:D[i]})
    return tL
       
#поиск в диапазоне
def d_search_in_range(param, Xmin, Xmax, D):
    tL=[]
    for i in D.keys():
        if Xmin<=str(D[i][param])<=Xmax:
            tL.append({i:D[i]})
    return tL
         
#вывести машины одной фирмы
def d_search_brand(S, D):
    tL=[]
    for i in D.keys():
        if str(i).find(S)!=-1:
            tL.append({i:D[i]})
    return tL

#поиск максимума по параметру
def d_search_Max_on_param(param, D):
    M = max(D[i][param] for i in D.keys())
    for i in D.keys():
        for j in D[i].keys():
            if D[i][j]==M:
                return {i:D[i]}
            
#поиск через нечеткое сравнение
def df_search_brand(S, D):
    tL=[]
    for i in D.keys():
        if compare(S,str(i))> 0.1 :
            tL.append({i:D[i]})
    return tL

