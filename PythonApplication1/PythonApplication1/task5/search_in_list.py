#поиск определнного значения
def l_search_on_val(S1,L1):     
    for i in L1:
        if S1 in i:
            return i
        
#поиск в диапазоне по цене        
def l_search_cost_in_range(Xmin, Xmax, L):        
    tL=[]
    for i in L:
        if int(Xmin)<=int(i[5])<=int(Xmax):
            tL.append(i)
    return tL
        
#вывести машины одной фирмы        
def l_search_brand(S, L):    
    tL=[]
    for i in L:
        if str(i).find(S)!=-1:
            tL.append(i)
    return tL

#вывести самую молодую машину        
def l_search_Max_on_param(param, L):
    M = max(i[param] for i in L)
    for i in L:
        if i[param]==M:
            return i

    
