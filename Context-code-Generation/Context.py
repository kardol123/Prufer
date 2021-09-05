import networkx as nx
import re
from networkx.algorithms.traversal.depth_first_search import dfs_tree
import pandas as pd

context_list_constant=['Annotation', 'AnnotationDeclaration', 'AnnotationMethod', 'ArrayCreator', 'ArrayInitializer', 'ArraySelector', 'AssertStatement', 'Assignment', 'BasicType', 'BinaryOperation', 'BlockStatement', 'BreakStatement', 'Cast', 'CatchClause', 'CatchClauseParameter', 'ClassCreator', 'ClassDeclaration', 'ClassReference', 'CompilationUnit', 'ConstantDeclaration', 'ConstructorDeclaration', 'ContinueStatement', 'Creator', 'Declaration', 'DoStatement', 'Documented', 'ElementArrayValue', 'ElementValuePair', 'EnhancedForControl', 'EnumBody', 'EnumConstantDeclaration', 'EnumDeclaration', 'ExplicitConstructorInvocation', 'Expression', 'FieldDeclaration', 'ForControl', 'ForStatement', 'FormalParameter', 'IfStatement', 'Import', 'InferredFormalParameter', 'InnerClassCreator', 'InterfaceDeclaration', 'Invocation', 'LambdaExpression', 'Literal', 'LocalVariableDeclaration', 'Member', 'MemberReference', 'MethodDeclaration', 'MethodInvocation', 'MethodReference', 'Node', 'PackageDeclaration', 'Primary', 'ReferenceType', 'ReturnStatement', 'Statement', 'StatementExpression', 'SuperConstructorInvocation', 'SuperMemberReference', 'SuperMethodInvocation', 'SwitchStatement', 'SwitchStatementCase', 'SynchronizedStatement', 'TernaryExpression', 'This', 'ThrowStatement', 'TryResource', 'TryStatement', 'Type', 'TypeArgument', 'TypeDeclaration', 'TypeParameter', 'VariableDeclaration', 'VariableDeclarator', 'VoidClassReference', 'WhileStatement', 'STR', 'NUM', 'STR_', 'NUM_', 'XXX', 'BOOL']

list1=[]
list2=[]
list3=[]
list4=[]
mid=[]



def neighbourt(T,item):# (T,item,st1,list1,list2):
    
    st1=""
    
    if item in T.nodes():
        for n in T.neighbors(item):
            if n > item and T.degree(n) == 1:
                st1=st1+str(n)+"_"
                #print(st1)
            
            
    
    return st1


def prufercode_context(parent_node_list,child_node_list,explanation_node,context_node,count):

    try:
        t=""
        tj=""
        if(len(list1)>1):
            list4=[]
            T = nx.Graph()
            T.add_nodes_from(parent_node_list)
            T.add_nodes_from(child_node_list)
            edgeList = list(zip(parent_node_list,child_node_list))
            edgeList1 = list(zip(parent_node_list,child_node_list,explanation_node))
            edgeList2 = list(zip(parent_node_list,child_node_list,explanation_node,context_node))
            T.add_edges_from(edgeList,label = 1) 
            T.remove_edges_from(nx.selfloop_edges(T))

            nei=[]
            list5=[]
            list6=[]
            
            for (node, val) in T.degree():
                if val == 1:
                    list5.append(node) # collect all terminal nodes 
            
            if T.number_of_nodes() > 2:
                k=nx.to_prufer_sequence(T) 
              
            
            list_of_neighbour=[]
            
            finallist_of_neighbour=[]
            
            for eachitem in k:#if eachitem != 0:
                st12=""
                fruit_dictionary23 = dict(zip(parent_node_list, explanation_node))
                ab23=fruit_dictionary23[eachitem]

                if  ab23=='BlockStatement' or ab23=='StatementExpression' :#or ab23 =='ForStatement' or ab23=='SwitchStatementCase' or ab23 == 'WhileStatement'or ab23 =='IfStatement' or ab23 =='BlockStatement'or ab23 =='TryStatement'or ab23=='SwitchStatement'or ab23=='ContinueStatement' or ab23=='DoStatement' or ab23=='ReturnStatement'or ab23=='Assignment':#or ab23=='SynchronizedStatement'or ab23=='Assignment'or ab23=='ClassCreator'or ab23=='MethodDeclaration':#  or ab23=='LambdaExpression'or ab23=='CatchClause':#or ab23=='LocalVariableDeclaration'or ab23=='BinaryOperation': 
                    list_of_neighbour.append(ab23+"_")
                    
                elif eachitem==0:
                    list_of_neighbour.append(str(eachitem)+"_")
                    
                else: 
                    k1=neighbourt(T,eachitem)
                    
                    print(k1)
                    
                    list_of_neighbour.append(k1)
                        
           
            set1={}
            set2={}
           
            
            
            Context_from_dictionary=""
            context_string=" "
            context_list=[]
            for obs in list_of_neighbour:
                
                set1=obs.split("_")
                
                finallist_of_neighbour.append(set(set1))# after removing the duplicates 

             
            
           
            fruit_dictionary66 = dict(zip(parent_node_list,context_node)) 
            #print(fruit_dictionary66)
            fruit_dictionary77 = dict(zip(explanation_node,context_node)) 
            #print(fruit_dictionary77)
            for each_neighbour_list in finallist_of_neighbour:
                for each_item in each_neighbour_list:
                    if each_item !='':
                        if each_item=='BlockStatement' or each_item =='StatementExpression':#  now generate the context
                            Context_from_dictionary=fruit_dictionary77[each_item]
                            if Context_from_dictionary != 'XXX':
                                Context_from_dictionary==each_item+" "+Context_from_dictionary
                            elif Context_from_dictionary == 'XXX':
                                Context_from_dictionary=each_item
                
                        else:
                            Context_from_dictionary=fruit_dictionary66[int(each_item)]
                            #print(Context_from_dictionary,"  ",each_item)
                        try:
                            context_string=context_string+" "+Context_from_dictionary+" "
                            #context_string=context_string+" "+each_item+" "+Context_from_dictionary+" "
                            #print(context_string)
                            
                        except:
                            context_string=context_string+"nan1"+" "
                            
                             
                context_string=context_string+"  "
                pos_of_context=context_string.split()
                for i in range(len(pos_of_context)):
                    temp1=pos_of_context[i]
                    temp1=' '.join(re.split(',|\.',temp1))
                    temp1= re.split('_+',temp1)
                    for j in range(len(temp1)):
                        temp2=temp1[j]
                        if temp2 in context_list_constant:
                            context_list.append(temp2) 
                        
                        elif temp2 not in context_list_constant:
                            if (temp2.isupper() != True):
                                temp2=' '.join(re.sub( r"([A-Z])", r" \1", temp2).split())
                                context_list.append(temp2)
                            else:
                                context_list.append(temp2)
                                
                                    
                        
                    
                
                
                context_string=""
                
            
            final_list=[]
            
            
            list_temp=' '.join(context_list)
            list_temp=re.sub(r'\bSTR\b', '',list_temp)
            list_temp=re.sub(r'\bNUM\b', '',list_temp)
            list_temp=re.sub(r'\bnan1\b', '',list_temp)
            list_temp=re.sub(r'\bNum\b', '',list_temp)
            #list_temp=re.sub(r"\b[a-zA-Z]\b", "", list_temp)
            final_list=list_temp.split()
            with open("context_of_program_for_train","a")as outfile:
                #print(final_list)
                outfile.write(' '.join(map(str,final_list))+'\n')
            with open("prufer_of_program_for_train","a")as outfile:
                outfile.write(' '.join(map(str,k))+'\n')    
                
            
    
    except Exception as e:
        print("ekllo",e)
        val=input("enter the value ")
        
        
fd=pd.read_csv("train-prufer.csv",header=None)


pre=0
count=0

for i,j,k,l in zip(fd[0],fd[1],fd[2],fd[3]):
    if(pre <= i):
        list1.append(i)
        list2.append(j)
        list3.append(k)
        list4.append(l)
        pre=i
    elif(pre > i ):
        prufercode_context(list1,list2,list3,list4,count)
        count=count+1
        list1=[]
        list2=[]
        list3=[]
        list4=[]
        list1.append(i)
        list2.append(j)
        list3.append(k)
        list4.append(l)
        pre=0
        
prufercode_context(list1,list2,list3,list4,count)        
        
