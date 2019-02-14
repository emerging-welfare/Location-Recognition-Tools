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

