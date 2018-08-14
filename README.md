# Location-Recognition-Tools

The tools in this project are related to the ERC funded Research Project about Event Extraction in Koc University.

There are various tools for different purposes.

Each tool will be explained in detail.

### Tool 1: ACE to Token-per-line converter

ACE corpus is very detailed and stored in XML format. In order to convert the corpus into a token-per-line format you can use the aceconv.py. You need to have the ACE corpus in the original format with file.tbl file available. 

For now aceconv.py has 2 modes: custom and default. Default mode uses the predefined values for the input variables. No arguments are required for execution.

**In custom mode the program takes as input the following arguments:**

* base: base address of the folders of the ACE corpus

* filelistfile: full address of the file.tbl file which contains all the names of the files in the corpus

* outfilename: name of the output file

* tagtypes: Types of tags to be extracted from the corpus (multiple arguments)

* tagver: denotes the tagging version if 0 then tagging is binary if 1 each entity is tagged with its specific type (LOC, GPE, etc.)

 **Example run:**
 
 * In default mode: 
 ```
   $ python3 aceconv.py def
```
 * In custom mode: python3 aceconv.py base filelistfile outfilename tagtypes tagver
 
 ```
    $ python3 aceconv.py ACE/aceCorp/ ACE/aceCorp/docs/file.tbl acetotokenCorpus ORG LOC GPE 0
```
 * To help:
 
 ```
    $ python3 aceconv.py -h
 ```
 
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
 * GPE tags are converted to LOC (to simplify the dataset according to the project needs)

The resulting corpus format is Conll-format and tools designed specifically for Conll can be directly applied.
 
 For the purpose of our project it suffices to run the converter in the default mode as in the example given below. 
 
 **Example run for version2:**
 For default version:
  
 ```
    $ python3 aceconv2.py def
 ```
 This tool outputs two files:
 * The raw format of the ACE corpus (intermediate)with the predefined entity types and metadata are marked with special characters.
 * The token-per-line format (Aceconllformat) corpus with word tokenization and sentence tokenization applied. Nltk tools are used. Metadata is deleted in the default version.
 
 #### tokperlineCorpus file
 This file contains 427, 4061, 5506 tokens tagged with LOC, ORG, GPE respectively. 
 
 #### ACEconllformat file
 
This file is the output of the final version of the converter. This is our current corpus we are using for Location Recognition.
 
 
### Tool 2: Results and accuracy calculator 

results.ipynb

This tool calculates the precision recall and f1 scores for Wapiti on Conll and Ace datasets with different configurations. The results are included inside the results folder and this folder must be downloaded to view the results. If one wants to calculates precision recall etc. for a different result then calling the acc function with the corresponding parameters is enough.

Since the tool is a ipython notebook it is enough to download the notebook and the results folder and go over the notebook.

### Tool 3: Corpus splitter

corpsplitter.py

This tool splits a given corpus into training,validation and test sets. The corpus must be in Conll format where Documents are separated from each other with the -DOCSTART- tag. The tool takes as input the corpus name and the ratios for the training and test sets and outputs three files:
* train.txt
* test.txt
* valid.txt

Example run: python corpsplitter.py --corpus_name \[Corpus name\](required) --train_size \[Train size\](optional) ....


 ` $ python corpsplitter.py --corpus_name ACEconllformat --train_size 0.8 --test_size 0.2`
 
If the train_size and test_size does not add up to 1 the splitter automatically puts the remaining documents into the valid.txt. The splitter picks the documents randomly but uses the same seed everytime to split in the same way. You can download the "ACEconllformat" file together with corpsplitter.py to try on your own.


### Tool 4: word2vec trainer

This tool takes as input a filename which is the name of the unannotated corpus. The output is the trained vectors using the gensim's word2vec model. 

 ` $ python word2vec.py filename
