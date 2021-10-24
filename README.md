# Prufer Model 

We use the deep learning model used by the xing-hu in her implementation of the code summarization task. The original Code of xing-hu implementation is [available  here ](https://github.com/xing-hu/EMSE-DeepCom.git)

# Model Training
```
cd Prufer/ source code 

python3 __main__.py config.yaml --train -v

```
# To Evaluate the Model 

The metrics for the evaluation of the Code are BLEU, METEOR and are calculated as per the xing-hu in her implementation of the code summarization task. [The metrics implementation is available here  ](https://github.com/xing-hu/EMSE-DeepCom/tree/master/scripts). The ROUGE-L is a standard implementation with the python library. 


# AST Generation of the Code 

We refer to the AST generation by the xing-hu to generate our AST json file. [Implentation of the AST generation by xing-hu ](https://github.com/xing-hu/EMSE-DeepCom/blob/master/data_utils/get_ast.py). 

# Prufer Sequence Generation 

Following are the steps for generation for Prufer sequence generation.

1) Generate the CSV File from the AST file. 

```
python3 ASTtoCSV.py

```
2) Generate the Prufer sequence 


```

python3 PruferSequenceGeneration.py

```

# Context of the Code generation 

To genererate the Context of the code run :


```

python3 Context.py


```

# Dataset 

We use two datsets to test the efficiency and the efficacy of the Code Comment generation model. 

1) [TL-CodeSum Dataset](https://github.com/xing-hu/TL-CodeSum)
2) [COdeXGlue Dataset](https://github.com/microsoft/CodeXGLUE/tree/main/Code-Text/code-to-text)


