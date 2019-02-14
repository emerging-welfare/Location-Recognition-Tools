## Event Status Corpus


### English 
This folder contains the Event Status English Gigaword 5th Edition converted to JSON format. The file named "eventstatuscunojson" 
contains the json format corpus for the documents that are annotated only for the sentence level.
The file named "eventstatusbothjson" contains the json format corpus for the documents that are annotated for both 
phrase level and sentence level. The files are python lists that contain dictionaries as in JSON format, saved using **pickle** package.

To load the JSON formatted documents use: 

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

