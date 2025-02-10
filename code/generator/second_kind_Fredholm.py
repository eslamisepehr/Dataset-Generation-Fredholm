# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:43:17 2024

@author: Hassan
"""

import numpy as np
import warnings
import os
import sympy as sp
from brian2.parsing.sympytools import sympy_to_str

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
warnings.filterwarnings("ignore")

n_iterations=10

def vec2exp_u(vector):
    vectorMaxLength=15
    s='@' 
    for j,i in enumerate(vector):
            
        notFount=True        
        for counter,character in enumerate(s):
            
            if character =='@':
                s_left=s[0:counter]
                s_right=s[counter+1:]
                myMod= i % 4
                if (myMod==0 or myMod==1) and j > vectorMaxLength:
                    myMod=3
                    
                match myMod:
                    case 0:
                        s=s_left+'@$@'+s_right
                    case 1:
                        s=s_left+'(@$@)'+s_right
                    case 2:
                        s=s_left+'%(@)'+s_right
                    case 3:
                        s=s_left+'&'+s_right
                        pass
                notFount=False
                
            if character =='$':
                s_left=s[0:counter]
                s_right=s[counter+1:]
                myMod= i % 4
                match myMod:
                    case 0:
                        s=s_left+'+'+s_right
                    case 1:
                        s=s_left+'-'+s_right
                    case 2:
                        s=s_left+'/'+s_right
                    case 3:
                        s=s_left+'*'+s_right
                notFount=False
                
            if character =='%':
                 s_left=s[0:counter]
                 s_right=s[counter+1:]
                 myMod= i % 16
                 match myMod:
                    case 0:
                        s=s_left+'(@)**2'+s_right[3:]
                    case 1:
                        s=s_left+'(@)**3'+s_right[3:]
                    case 2:
                        s=s_left+'(@)**4'+s_right[3:]
                    case 3:
                        s=s_left+'(@)**5'+s_right[3:]
                    case 4:
                        s=s_left+'t**2'+s_right[3:]
                    case 5:
                        s=s_left+'t**3'+s_right[3:] 
                    case 6:
                        s=s_left+'t**4'+s_right[3:]
                    case 7:
                        s=s_left+'t**5'+s_right[3:] 
                    case 8:
                        s=s_left+'sin'+s_right
                    case 9:
                        s=s_left+'cos'+s_right
                    case 10: 
                        s=s_left+'tan'+s_right
                    case 11:
                        s=s_left+'exp'+s_right
                    case 12:
                        s=s_left+'log'+s_right
                    case 13:
                        s=s_left+'sinh'+s_right
                    case 14:
                        s=s_left+'cosh'+s_right   
                    case 15:
                        s=s_left+'tanh'+s_right
                 notFount=False
                
            if character =='&':
                s_left=s[0:counter]
                s_right=s[counter+1:]
                myMod= i % 2
                
                if  myMod==0:
                    s=s_left+'t'+s_right
                if myMod==1:
                    random_coefficient=-10+20*np.random.rand()
                    w=str(random_coefficient)
                    s=s_left+w+s_right
                      
                notFount=False
                
            if notFount==False:
                break;
    return s

def vec2exp_kernel(vector):
    vectorMaxLength=10
    s='@' 
    for j,i in enumerate(vector):
            
        notFount=True        
        for counter,character in enumerate(s):
            
            if character =='@':
                s_left=s[0:counter]
                s_right=s[counter+1:]
                myMod= i % 4
                if (myMod==0 or myMod==1) and j > vectorMaxLength:
                    myMod=3
                    
                match myMod:
                    case 0:
                        s=s_left+'@$@'+s_right
                    case 1:
                        s=s_left+'(@$@)'+s_right
                    case 2:
                        s=s_left+'%(@)'+s_right
                    case 3:
                        s=s_left+'&'+s_right
                        pass
                notFount=False
                
            if character =='$':
                s_left=s[0:counter]
                s_right=s[counter+1:]
                myMod= i % 4
                match myMod:
                    case 0:
                        s=s_left+'+'+s_right
                    case 1:
                        s=s_left+'-'+s_right
                    case 2:
                        s=s_left+'/'+s_right
                    case 3:
                        s=s_left+'*'+s_right
                notFount=False
                
            if character =='%':
                 s_left=s[0:counter]
                 s_right=s[counter+1:]
                 myMod= i % 16
                 match myMod:
                    case 0:
                        s=s_left+'(@)**2'+s_right[3:]
                    case 1:
                        s=s_left+'(@)**3'+s_right[3:]
                    case 2:
                        s=s_left+'(@)**4'+s_right[3:]
                    case 3:
                        s=s_left+'(@)**5'+s_right[3:]
                    case 4:
                        s=s_left+'x**2'+s_right[3:]
                    case 5:
                        s=s_left+'x**3'+s_right[3:] 
                    case 6:
                        s=s_left+'t**2'+s_right[3:]
                    case 7:
                        s=s_left+'t**3'+s_right[3:]
                    case 8:
                        s=s_left+'sin'+s_right
                    case 9:
                        s=s_left+'cos'+s_right
                    case 10: 
                        s=s_left+'tan'+s_right
                    case 11:
                        s=s_left+'exp'+s_right
                    case 12:
                        s=s_left+'log'+s_right
                    case 13:
                        s=s_left+'sinh'+s_right
                    case 14:
                        s=s_left+'cosh'+s_right   
                    case 15:
                        s=s_left+'tanh'+s_right
                 notFount=False
                
            if character =='&':
                s_left=s[0:counter]
                s_right=s[counter+1:]
                myMod= i % 3
                
                if  myMod==0:
                    s=s_left+'x'+s_right
                if  myMod==1:
                    s=s_left+'t'+s_right
                if  myMod==2:
                    random_coefficient=-10+20*np.random.rand()
                    w=str(random_coefficient)
                    s=s_left+w+s_right
                      
                notFount=False
                
            if notFount==False:
                break;
    return s

def generate_a_function_u():
    maxNumber=255
    vector=[]
    myRand=np.random.randint(maxNumber)
    vector.append(myRand)
    s=vec2exp_u(vector)
    maxNumber=255
    while ('@' in s) or ('$' in s) or ('%' in s) or ('&' in s) or ('^' in s) or ('!' in s) or ('#' in s):
        myRand=np.random.randint(maxNumber)
        vector.append(myRand)
        s=vec2exp_u(vector)
    return s

def generate_a_function_kernel():
    maxNumber=255
    vector=[]
    myRand=np.random.randint(maxNumber)
    vector.append(myRand)
    s=vec2exp_kernel(vector)
    maxNumber=255
    while ('@' in s) or ('$' in s) or ('%' in s) or ('&' in s) or ('^' in s) or ('!' in s) or ('#' in s):
        myRand=np.random.randint(maxNumber)
        vector.append(myRand)
        s=vec2exp_kernel(vector)
    return s

for i in range(1):
    x=sp.Symbol('x')
    t=sp.Symbol('t')
    u=generate_a_function_u()
    kernel=generate_a_function_kernel()
    u=sp.parse_expr(u)
    kernel=sp.parse_expr(kernel)
    mylambda=-10+20*np.random.rand()
    a=-10+20*np.random.rand()
    b=-10+20*np.random.rand()
    if a>b:
        mytemp=a
        a=b
        b=mytemp
    try:
        temp1=mylambda*sp.integrate(u*kernel,(t,a,b))
        u=u.subs(t,x)
        f=u-temp1
        mylambda=str(mylambda)
        a=str(a)
        b=str(b)
        u=sympy_to_str(u)
        f=sympy_to_str(f)
        kernel=sympy_to_str(kernel)
        print('************************************************')
        print(u+', '+f+', '+kernel+', '+mylambda+', '+a+', '+b)
        print(u+', '+f+', '+kernel+', '+mylambda+', '+a+', '+b,file=open('Data_set_FredHolm.txt','a'))
    except:
        pass
    