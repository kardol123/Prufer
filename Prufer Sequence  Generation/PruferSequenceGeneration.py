import pandas as pd
import networkx as nx
import re


def prufercode(list1,list2,list3,count):
    
    
    try:
        if(len(list1)>0):
            list4=[]
            T = nx.Graph()
            T.add_nodes_from(list1)
            T.add_nodes_from(list2)
            edgeList = list(zip(list1,list2))
            edgeList1 = list(zip(list1,list2,list3))
            T.add_edges_from(edgeList,label = 1) 
            T.remove_edges_from(nx.selfloop_edges(T))
            #degrees = [val for (node, val) in T.degree()]
            
            
            list5=[]
            list6=[]
            
            for (node, val) in T.degree():
                if val == 1:
                    list5.append(node)
                    
            #print(T.number_of_nodes())
           
            
            if T.number_of_nodes() <= 2:
                #k=nx.bfs_tree(T, 0)# for bfs
                #print(k)
                k=[1,0,0,1] #for prufer code 
                
            elif T.number_of_nodes() > 2:
                #k=nx.bfs_tree(T, 0)# for bfs
                k=nx.to_prufer_sequence(T) #for prufer code 
                
            n=len(T)
            
            #print(count,set(T),set(range(n)))
            fruit_dictionary = dict(zip(list1, list3))
            
            
            #print(fruit_dictionary)
            
            for j in list5:
                finalstring=[]
                j1=fruit_dictionary[j]
                temp_trminal=j1.split()
                
                if (len(temp_trminal)>1):
                    temp_first=temp_trminal[0]
                    finalstring.append(temp_first)
                    
                    temp_second=temp_trminal[1]
                    if (temp_second != "STR_" and temp_second != "NUM_" and temp_second != "BOOL_" and temp_second != "XXX" ):
                        if (temp_second.isupper() != True):
                            #temp_second=' '.join(re.sub( r"([A-Z])", r" \1", temp_second).split())
                            temp_second=' '.join(re.split(',|\.',temp_second))
                            temp_second= re.split('_+', temp_second)
                            for count26400 in range(len(temp_second)): 
                                if (temp_second[count26400].isupper() != True):
                                    finalstring.append(' '.join(re.sub( r"([A-Z])", r" \1", temp_second[count26400]).split()))
                                    
                                    
                #print(finalstring)
                
                list6.append(' '.join(finalstring))
                
               # list6.append(j1)
            
            for i in k:
                z1=fruit_dictionary[i]
                list4.append(z1)
            
            #print(list4) 
            list4.extend(list6)# join the prufer code and termial code 
            #print(list4)
            
            
            
                
                
            
            #print(list4)
            print(count)
            with open("train-prufer-sequence","a")as outfile:
                outfile.write(' '.join(map(str,list4))+'\n')
    
    except Exception as e:
        n=len(T)
        print(count,set(T),set(range(n)))
        print(e)
        val=input("enter the value ")
        
        
        


list1=[]
list2=[]
list3=[]
mid=[]
fd=pd.read_csv("train-prufer.csv",header=None)

    
pre=0
count=0

for i,j,k in zip(fd[0],fd[1],fd[2]):
    if(pre <= i):
        list1.append(i)
        list2.append(j)
        list3.append(k)
        pre=i
    elif(pre > i ):
        prufercode(list1,list2,list3,count)
        count=count+1
        list1=[]
        list2=[]
        list3=[]
        list1.append(i)
        list2.append(j)
        list3.append(k)
        pre=0
        
prufercode(list1,list2,list3,count)         
