# TREC-ToT 


We've mapped the Reddit-TOMT dataset to the [TREC-ToT](https://trec-tot.github.io/) 2023 corpus, and 
released the queries in the same format as the TREC-ToT dataset. 


Not all queries were mapped. The number of queries successfully mapped are reported in the table below:

| Split | # original queries | # queries mapped to TREC-ToT Corpus | 
|-------|----------------------|------------------|
| train | 10777                | 7252             |
| validation | 1346            | 918              |
| test       | 1346            | 933              |
| total      | 10558           | 9103             |


The format of the data is similar to the [TREC-ToT queries](https://trec-tot.github.io/guidelines), with 
`sentence_annotations` always `null`. 


 