# -*- coding: UTF-8 -*-
import time

# Conditions / recursif
def f_Meg_recur(a,b,c=0):
    if b == 0 :
        return c
    else :
        if b%2 == 0:
            return f_Meg_recur(2*a,b/2,c)
        else:
            return f_Meg_recur(a,b-1,c+a)

# Conditions / Iteratif
def f_Meg_iter(a,b):
    c=0
    while b != 0 :
        if b%2 == 0:
            a=2*a
            b=b/2
        else :
            b = b-1
            c = c+a
    return c

# Equation / Recursif
def s_Meg_recur(a,b,c=0): 
    if b == 0 :
        return c
    else :
        return int(s_Meg_recur(a*(2-b%2),(b-b%2)/(2-b%2),c + a*(b%2)))

# Equation / Iteratif
def s_Meg_iter(a,b):
    c=0
    while b != 0 :
        c = c + a*(b%2)
        a = a*(2-b%2)
        b = (b-b%2)/(2-b%2)
    return int(c)

# fonction de test
def Test():
    #Definition de a et b
    a=2016
    b=1337

    #init des variables de temps cumulé
    t_s_Meg_iter=0
    t_s_Meg_recur=0
    t_f_Meg_iter=0
    t_f_Meg_recur=0

    #Definition du nombre de run
    run=10

    #definition du nombre de cycles / run
    Cycles=100000

    
    #boucles de test
    for i in range(run):
        print('-----')

        t0=time.time()
        for t in range(Cycles):
           s_Meg_iter(a,b)
        t1=time.time()-t0
        print('s_meg_iter ', i ," : ", t1 ,' Secondes')
        t_s_Meg_iter+=t1

        t0=time.time()
        for t in range(Cycles):
            s_Meg_recur(a,b)
        t1=time.time()-t0
        print('s_Meg_recur ', i ," : ", t1 ,' Secondes')
        t_s_Meg_recur+=t1

        t0=time.time()
        for t in range(Cycles):
            f_Meg_iter(a,b)
        t1=time.time()-t0
        print('f_Meg_iter ', i ," : ", t1 ,' Secondes')
        t_f_Meg_iter+=t1

        t0=time.time()
        for t in range(Cycles):
            f_Meg_recur(a,b)
        t1=time.time()-t0
        print('f_Meg_recur ', i ," : ", t1 ,' Secondes')
        t_f_Meg_recur+=t1

    # Print des temps totaux   
    print('~~~~~~~~~~~~~')
    print('Total s_meg_iter : ', t_s_Meg_iter ,' Secondes')
    print('Total s_Meg_recur : ', t_s_Meg_recur ,' Secondes')
    print('Total f_Meg_iter : ', t_f_Meg_iter ,' Secondes')
    print('Total f_Meg_recur : ', t_f_Meg_recur ,' Secondes')
    print('~~~~~~~~~~~~~')
    

# lance le test
Test()