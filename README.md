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
 
 **Second version of converter**
 
 Previous converter (aceconv.py) have issues related to tokenization and sentence splitting. In this new version we solved these issues. The only drawback of this version is that it includes the metadata of each document. 
 
 **Example run for version2:**
 For default version:
  
 ```
    $ python3 aceconv2.py def
 ```
 This tool outputs two files:
 * The raw format of the ACE corpus with the predefined entity types and metadata are marked with special characters.
 * The token-per-line format corpus with word tokenization and sentence tokenization applied. Nltk tools are used. Metadata is deleted in the default version.
 
 
