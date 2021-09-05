import json
import csv

def Prufer_(cur_root_id, node_list):
    cur_root = node_list[cur_root_id]
    list1=[]
    list2=[]
    tmp_list = []
    tmp_list.append("(")
    val=" "
    
    if 'children' in cur_root:
        str1 = cur_root['type']
    elif 'children' not in cur_root:
        str1 = cur_root['type']+" "+cur_root['value']
  
    tmp_list.append(str1)
    if 'children' in cur_root:
        if 'value' in cur_root:
            val=cur_root["value"]
            #print(val)
        elif 'value' not in cur_root: 
            val="XXX"
            #print(val)
        chs = cur_root['children']
        with open("test-prufer.csv", "a") as f:
            writer = csv.writer(f)
            for x in chs:
                writer.writerow((cur_root['id'],x,cur_root['type'],val))  
                
        for ch in chs:
            tmp_list.extend(Prufer_(ch, node_list))
    elif 'children' not in cur_root:
        with open("train-prufer.csv", "a") as f1:
            writer1 = csv.writer(f1)
            writer1.writerow((cur_root['id'],cur_root['id'],cur_root['type']+" "+cur_root['value'],cur_root['value']))
    tmp_list.append(")")
    tmp_list.append(str1)
    return tmp_list

def get_sbt_structure(ast_file, out_file):
    count=1
    with open(ast_file, 'r') as ast_file:
        with open(out_file, 'w+') as out:
            asts = ast_file.readlines()
            for a in asts:
                #count=count+1
                #print(count)
                check1=[]
                check2=set()
                a = json.loads(a)
                #print(set(range(0,len(a))))
                for i1 in a:
                    if 'children' in i1:
                        check1.append(i1["children"])
                        ko=i1["children"]
                        for i in ko:
                            check2.add(i)
                #print(set(check1))  
                check2.add(0)
                if set(check2) == set(range(0,len(a))):
                    count=count+1
                    tmp_list=Prufer_(0,a)
                    out.write(' '.join(tmp_list) + '\n')
                    print(count)
                if set(check2) != set(range(0,len(a))):
                    print("not equal")
                    val=input("value ")

get_sbt_structure("train_code.json", "train.token.ast2640.txt")
