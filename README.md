# Location-Recognition-Tools

The tools in this project are related to the ERC funded Research Project about Event Extraction in Koc University.

There are various tools for different purposes.

Each tool will be explained in detail.

### Tool 1: ACE to Token-per-line converter


ACE corpus is very detailed and stored in XML format. In order to convert the corpus into a token-per-line format you can use the aceconv.py. You need to have the ACE corpus in the original format with file.tbl file available. 

For now aceconv.py has 2 modes: custom and default. Default mode uses the predefined values for the input variables. No arguments are required for execution.

**Requirements:** python version must be above python 3. Besides lxml, nltk,xml packages must be installed for python. Finally after installing nltk please download 'punkt' 'gazetteers' 'names' 'stopwords' with:
```
nltk.download('punkt')
nltk.download('gazetteers') ...
```

**In custom mode the program takes as input the following arguments:**

* base: base address of the folders of the ACE corpus

* filelistfile: full address of the file.tbl file which contains all the names of the files in the corpus

* outfilename: name of the output file

* tagtypes: Types of tags to be extracted from the corpus (multiple arguments)

* tagver: denotes the tagging version if 0 then tagging is binary if 1 each entity is tagged with its specific type (LOC, GPE, etc.)

 **Example run:**
 
 * In default mode: 
 ```
   $ python3 aceconv2.py def
```
 * In custom mode: python3 aceconv.py base filelistfile outfilename tagtypes tagver
 
 ```
    $ python3 aceconv2.py ACE/aceCorp/ ACE/aceCorp/docs/file.tbl acetotokenCorpus ORG LOC GPE 0
```
 * To help:
 
 ```
    $ python3 aceconv2.py -h
 ```
 **NOTE**: For now it is recommended to use the tool in default setting with "def" argument. In the default mode the ACE dataset must be in the current directory we are running the program and must be named "ACE".
 
 This converter uses the documents in the adj folders which are data also subject to discrepancy resolution/adjudication. This version of the converter uses all the raw text available in the .sgm files including the metadata. The entities inside the metadata such as headline are not tagged. 
 
 Future versions of the converter will not include these metadata as they create noise.
 
 Only in the default mode the converter deletes the DOCID, DOCTYPE, DATETIME and HEADLINE metadata and outputs the delete version of the corpus to the "wometaCorpus" file. 
 
 Following versions will allow the user to choose the final corpus name and whether to keep the metadata or not. Custom version does not delete metadata for now.
 
  **NOTE** : The ACE dataset must be in the same folder with the aceconv2.py file. The filenames in the file.tbl file must match with the dataset address.
 
 **Final version of converter**
 
 aceconv2.py
 
 Previous converter (aceconv.py) have issues related to tokenization and sentence splitting. In this new version we solved these issues. The final version has the following improvements over the previous version:
 
 * Sentence splitting and tokenization is done properly using nltk.
 * Document boundaries are included.
 * BIO tagging scheme is added to the entity tags.
 * GPE tags can be converted to LOC (to simplify the dataset according to the project needs)

The resulting corpus format is Conll-format and tools designed specifically for Conll can be directly applied.
 
 For the purpose of our project it suffices to run the converter in the default mode as in the example given below. 

 This tool outputs two files:
 * The raw format of the ACE corpus (intermediate)with the predefined entity types and metadata are marked with special characters.
 * The token-per-line format (Aceconllformat, tokperlineCorpus, tokperlineCorpusBIO) corpus with word tokenization and sentence tokenization applied. Nltk tools are used. Metadata is deleted in the default version. 
 
 #### tokperlineCorpus file
 This file contains 427, 4061, 5506 tokens tagged with LOC, ORG, GPE respectively. Same file tagged in BIO format is named tokperlineCorpusBIO
 
 #### ACEconllformat file
 
This file is the output of the final version of the converter. This is the output when we change the                                                     entity tags to fit the conll tags.
 
 
### Tool 2: Results and accuracy calculator 

results.ipynb

This tool calculates the precision recall and f1 scores for all our models with different configurations. The results are included inside the results folder and this folder must be downloaded to view the results. If one wants to calculates precision recall etc. for a different result then calling the acc function with the corresponding parameters is enough.

Since the tool is a ipython notebook it is enough to download the notebook and the results folder and go over the notebook.

### Tool 3: Corpus splitter

corpsplitter.py

This tool splits a given corpus into training,validation and test sets. The corpus must be in Conll format where Documents are separated from each other with the -DOCSTART- tag. The tool takes as input the corpus name and the ratios for the training and test sets and outputs three files:
* train.txt
* test.txt
* valid.txt

Example run: python corpsplitter.py --corpus_name Corpus name(required) --train_size \[Train size\](optional) ....


 ` $ python corpsplitter.py --corpus_name ACEconllformat --train_size 0.8 --test_size 0.2`
 
If the train_size and test_size does not add up to 1 the splitter automatically puts the remaining documents into the valid.txt. The splitter picks the documents randomly but uses the same seed everytime to split in the same way. You can download the "ACEconllformat" file together with corpsplitter.py to try on your own.


### Tool 4: word2vec trainer

This tool takes as input a filename which is the name of the unannotated corpus. The output is the trained vectors using the gensim's word2vec model. 

```
  $ python word2vec.py filename
```


### Tool 5: lookup table program

This program is an end-to-end lookup table program that makes of the MER tool already available.For details refer to the README file in the lookup document.


## Publicly Available Tools Used 

This section describes the machine learning tools we have used for place name recognition. These tools serve as the baseline models for place name recognition and named entity recognition systems for our task.

### Tool 1: NeuroNER 

NeuroNER is a Named Entity Recognition specific Neural Network based tool. The details about the tool and how to install it is available in the GitHub repository of the tool : [NeuroNer GitHub page](https://github.com/Franck-Dernoncourt/NeuroNER ). 

We assume that the users can download and install NeuroNER to their machine. Below we mention the errors we have encountered when we run the tool in a Unix machine. Hopefully this will speed up the installation process.

**Possible Errors**

 1 - We observed that changing the parameters.ini file is a safer way to change parameters rather than giving command line input.
 
 2 - Due to version difference we got an error at line 36  of utils_plots.py file. Changing line 36 to
 ``` ax=pc.axes ``` solves the problem.
 
 3 - In neuroner.py changing ``` import distutils``` to ``` import distutils.util``` was necessary again due to changes.
 
 4 - Prefer running the tool with ```python3``` to avoid problems that may arise due to python version difference.
 
 
 #### Results using NeuroNER
 
 We have already described in detail the results we have obtained using this tool in the ipython notebook [results](results.ipynb). Below we give the results we obtained for our initial test set for Indian News made up of 116 news documents. Each model is trained using different training sets. The results are calculated considering only the LOC type entities.
 
 | Model | Precision | Recall | F1-Score |
 | ----  | --|--              | -----    |
 | Neuro1 | 0.711 | **0.749** | 0.730 | 
 | Neuro2 | 0.407 | 0.516 | 0.455 | 
 | Neuro3 | **0.779** | 0.729 | **0.753** |
 

We have also done experiments using our own embeddings trained specifically on Indian News Corpus. This corpus consists of around 2M news articles. The NeuroNER tool recommends using the GloVe pretrained word embeddings. The results we have obtained also show that those word embeddings perform better than our own ones. Still we share them for those who would like to use them during their experiments. Diff file found under word2vec folder is the word embedding found in our own set and not available in GloVe's own word embeddings. Users can take the union of the two sets to obtain a reasonable initializer for word embeddings. 

To replicate the training and testing we also give the datasets we have used under conll2003 and ACEsplitted folders. Please remember that the training validation and test sets must be named train.txt valid.txt and test.txt respectively. Also remember that the dataformat for all input files must be the same. The files in conll2003 with the prefix "featsiz" are in compatible format with ACE files. 


### Tool 2: Wapiti

Wapiti is a CRF-based sequence labeling toolkit. Detailed information about installation and usage can be obtained from the [original website](https://wapiti.limsi.fr/). We have done numerous experiments using this tool with different configurations. Details about the results using this tool is given in the [results](results.ipynb) file. 


### Tool 3: NCRFPP

Thırd tool we have for place name recognition is NCRFPP. Relevant information about installation and running is available on [Github](https://github.com/jiesutd/NCRFpp). They give detailed results for the experiments on the Conll 2003 English NER task. Here we give the results we obtained for our own Indian News test set.

 | Model | Precision | Recall | F1-Score |
 | ----  | --|--              | -----    |
 | NCRFPP | 0.612 | 0.782 | 0.687 | 
 
 The tool does not append the prediction at the end of each file as in the case with many NER tools. This is not a major issue but we also give a python file named ```ncrfppappend.py``` which takes as input the gold labeled test set and  the file containing predictions and outputs a single file containing both the gold label and the prediction. Example run for the appender:
 
 ```
 python ncrfappender.py --goldfile gold.txt --predfile pred.txt --outfile out.txt
 ```
 The goldfile and predfile inputs must be given. The outfile parameter has the default value 'output'.


## Datasets 

This section explains the datasets used for the place name recognition task of our project.

### English News from India test set

This first batch of 116 documents from India is an annotated dataset for the location, person and organization type named entities. This dataset is constructed mainly for the Event Extraction task. Thus only the entities inside an event sentence is annotated. Named entities outside these sentences are not annotated. In order to have a consistent dataset the test set contains **only the event sentences**. 

The test set is available in the [Indian_News_testset](Indian_News_testset) folder with name `test.txt'.



