## Event Status Corpus



This folder contains the Event Status English Gigaword 5th Edition and Spanish Gigaword 3rd Edition converted to JSON format. Due to the versioning the pickle files may not be loaded appropriately. Thus we also give the pickle files converted using python 3. These files have the ending p3 to denote python version 3 is used during conversion. Files with the .json ending are the ready-to-use files in json format. Other files are pickle files which can be used in python by loading using pickle.

### English 
The files named "eventstatuscunojson" 
contains the json format corpus for the documents that are annotated only for the sentence level.
The file named "eventstatusbothjson" contains the json format corpus for the documents that are annotated for both 
phrase level and sentence level. 

## Spanish 

The file named "eventstatuscunospjson" 
contains the json format corpus for the documents that are annotated only for the sentence level.
The file named "eventstatusbothspjson" contains the json format corpus for the documents that are annotated for both 
phrase level and sentence level. 

The files are python lists that contain dictionaries as in JSON format, saved using **pickle** package.

To load the JSON formatted documents in python using pickle, use: 

```
import pickle
file = open("eventstatusbothjson","rb")
data = pickle.load(file)
```

Below we give a short description of each field in the json format:

* chunk_inds : Denotes the start and end index of a sentence containing an event keyword in the document.
* chunks : Sentences containing an event keyword in the document.
* doc_name: Name of the document as in English Gigaword Fifth Edition.
* keyword_inds: Index of the keyword inside the event sentence (chunk). This is not the character index but the token index where we used the .split() function in python for tokenization.
* keywords: Event keywords inside the document, one keyword for each chunk.
* metadata: Metadata related to the news document
* phrase_level_tags : Phrase level tag of each event sentence in the document. This field is not available in the sentence level only annotated documents.
* phrase_level_votes : Phrase level votes of each event sentence in the document. This field is not available in the sentence level only annotated documents.
* sentence_level_tags : Sentence level tag of each event sentence in the document.
* sentence_level_votes : Sentence level votes of each event sentence in the document.
* text: The news document with the html tags stripped off.
* title: Title of the news document.

### Converter

The program used for converting the datasets into JSON format is eventstatusjsonconverter.py. This program receives the arguments : path to the folder containing all the documents in .txt format and the name of the output file for json.

Example run is as follows : 

```
$ python eventstatusjsonconverter.py EventStatus/data/Spanish/annotated_texts eventstatus_spa
```

The first argument is the path to the directory containing the news documents and the second one is the name of the output files. Note that the program outputs to files for sentence level only annotations and sentence and phrase level annotations.
The file with the suffix cuno denotes the sentence level only datasets and the file with the suffix both denotes the datasets annotated for both sentence and phrase level. The converter generates both pickle files and json files. 
