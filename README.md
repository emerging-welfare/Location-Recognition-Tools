# Location-Recognition-Tools

The tools in this project are related to the ERC funded Research Project about Event Extraction in Koc University.

There are various tools for different purposes.

Each tool will be explained in detail.

ACE corpus is very detailed and stored in XML format. In order to convert the corpus into a token-per-line format you can use the aceconv.py. You need to have the ACE corpus in the original format with file.tbl file available. 

For now aceconv.py has 2 modes: custom and default. Default mode uses the predefined values for the input variables. No arguments are required for execution.

In custom mode the program takes as input the following arguments:

base: base address of the folders of the ACE corpus

filelistfile: full address of the file.tbl file which contains all the names of the files in the corpus\\
outfilename: name of the output file\\
tagtypes: Types of tags to be extracted from the corpus (multiple arguments)\\
tagver: denotes the tagging version if 0 then tagging is binary if 1 each entity is tagged with its specific type (LOC, GPE, etc.)\\
