#!/bin/bash

lex_name=$1
corpwtags_name=$2
corpwotags_name="corpwotags"
lookup_name="lookupout"
tagged_corp=$3

python wordsalone.py $corpwtags_name $corpwotags_name
cd data/
../produce_data_files.sh $lex_name > lex.out
cd ../
./get_entities.sh $corpwotags_name $lex_name > $lookup_name
python inds_to_tagged.py $lookup_name $corpwotags_name $corpwtags_name $tagged_corp


