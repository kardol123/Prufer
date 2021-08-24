# Prufer Model 

We use the deep learning model used by the xing-hu in her implememtation of the code summrization task. The original code is [avialeble here ](https://github.com/xing-hu/EMSE-DeepCom.git)

# Model Training
```
cd Prufer/ source code 

python3 __main__.py config.yaml --train -v

```
# To Evaluate the Model 

The metrics for the evaluation of the code are BLEU, METEOR and are calulated as per the xing-hu in her implememtation of the code summrization task. [The metrics implementation is available here  ](https://github.com/xing-hu/EMSE-DeepCom/tree/master/scripts). The ROUGE-L is a standard implemention with pyhton library. 


# AST Generation of the Code 

We refer the AST generation by the xing-hu to generate the AST. [Code to generate the AST of the code ](https://github.com/xing-hu/EMSE-DeepCom/blob/master/data_utils/get_ast.py). 

# Prufer Sequence Generation 


# Context of the Code generation 














