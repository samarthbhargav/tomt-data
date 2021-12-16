# Reddit-TOMT

##### 'It's on the tip of my tongue' 
###### A new dataset for Known-Item Retrieval

DOI: Coming soon!

Authors: [Samarth Bhargav](https://samarthbhargav.github.io/) | [Georgios Sidiropolous](https://twitter.com/gnsidiro/) | [Evangelos Kanoulas](https://staff.fnwi.uva.nl/e.kanoulas/)

About our Lab: [IRLab (formerly ILPS), University of Amsterdam](https://irlab.science.uva.nl/)

Blog post: Coming soon!

### Abstract

TODO

### Bibtex

```
TODO
```


This repository contains data and code for reproducing the data collection and benchmarks for the Reddit-TOMT dataset. 

We are thankful for the following APIs/libraries/datasets/misc used in this project:

- Pushshift
- PRAW
- Wikiplots
- IMDbPy
- LabelStudio

Data: TODO  


## Setup 

This project was run in `python-3.7.10`, it is highly recommended to use this exact version, with a separate environment
using pyenv-virtualenv. The DPR benchmark's requirements are separate (see `DPR/README.md`). Run the following command to 
install all requirements:   

```
pip install -r top_reqs.txt
# install haystack
pip install farm-haystack@git+https://github.com/deepset-ai/haystack.git@da97d813056e5710009ddd5b00fc3531ece9aee7
# download spacy model
python -m spacy download en_core_web_md

```  


## Reproducing the data collection process 

To reproduce the data collection outlined in the paper, please read the [DATA.md](DATA.md) file
for prerequisites, and run the `download_paper_data.sh` script. This collects
a dataset for the years 2017-2020 inclusive.  

If you want to add to the collection or collect data for other domains or 
develop new methods, etc, see [Collecting Additional Data in DATA.md](DATA.md#Collecting-Additional-Data) 

  
## Data Collection  

  
## Benchmarks




