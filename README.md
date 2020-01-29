# Knowledge extraction for assisted curation of summaries of bacterial transcription factor properties

Here, we publish an effective approach for knowledge extraction to assist curation 
of summaries describing following bacterial transcription factor (TF) properties:
1.	The biological processes in which the regulated genes are involved.
2.	The number, name, and size of the structural domains constituting the TF.
3.	Evolutionary features of the TF.
4.	Processes and conditions that regulate (positively or negatively) the activity and/or conformation of the TF.
5.	Processes and conditions that regulate the activity and organization of the transcription unit that contains the gene encoding the TF.
6.	Specific attributes of the TF's binding site, such as its size and spatial arrangement.

We were able to recover automatically a median of 77% of the knowledge 
contained into manual summaries (obtained from RegulonDB) 
describing properties of 177 TFs of 
*Escherichia coli* K-12 by processing 5961 scientific articles. 
Furthermore, training a predictive model with manual summaries of *E. coli*, 
we generated summaries for 305 TFs of *Salmonella typhimurium* from 3498 articles.
A simple Web page to browse the summaries in html format 
is available in *website* directory. 

```
/automatic-summaries
└───/ecoli
└───/salmonella
└───/website
```

This approach is based on automatic text summarization and extended 
our initial approach published on 2017 
where we generated summaries by focusing on two particular properties: 
structural domain and 
biological processes of regulated genes:
- Carlos-Francisco Méndez-Cruz, Socorro Gama-Castro, Citlalli Mejía-Almonte, 
Marco-Polo Castillo-Villalba, Luis-José Muñiz-Rascado, Julio Collado-Vides. 
(2017). First steps in automatic summarization of transcription factor properties 
for RegulonDB: classification of sentences about structural domains and regulated 
processes. *Database*, Oxford University Press (https://academic.oup.com/database/article/doi/10.1093/database/bax070/4237584)

## Manual summaries

We employed manual summaries from RegulonDB (http://regulondb.ccg.unam.mx/) 
as training data to train our automatic summarizer. 
We manually classified the sentences of 177 manual summaries 
in one or more of the six TF properties. 
To classify the sentences, we tagged specific relevant information associated 
to each TF property using XML tags (see supplementary Table S1 and 
supplementary Figure S1).

```
/manual-summaries
└───/xml-tagged
└───/sentences-per-property
```

## Salmonella manual evaluation
Manual evaluation by two curators of 10 automatic summaries 
generated for *Salmonella* showed that the 96% of the sentences 
were relevant sentences to describe properties of a TF. 
However, only the 65% of sentences were classified in the correct property.
```
/salmonella-manual-evaluation
```
 
## Transcription factors summarizer

### Input
You must place input files of the article collection within a subdirectory 
of your Working Directory (WD). 
We suggest naming it 'Articles' (as that would be the default value taken by 
the pipeline). Input files must be raw text files. 
Extension '.txt' is mandatory for these files.

### NLP preprocessing pipeline
The first step is preprocessing the input files. This step must be performed 
only once for the same article collection.

#### Prerequisites
You must have installed Stanford POS Tagger and BioLemmatizer in your computer. 
They are not included within this repository, have a look at the following 
references for instructions on the download and installation of these programs:
- Toutanova, K., Klein, D., Manning, C. and Singer, Y. (2003) 
Feature-rich part-of-speech tagging with a cyclic dependency network. 
In Proceedings of the HLT-NAACL, pp. 252-259 
(https://nlp.stanford.edu/software/tagger.shtml).
- Liu, H., Christiansen, T., Baumgartner, W. A., Jr., and Verspoor, K. (2012) 
BioLemmatizer: a lemmatization tool for morphological processing of 
biomedical text. J. Biomed. Semantics, 3, 1-29 
(https://sourceforge.net/projects/biolemmatizer/).

#### Preprocessing directory
Our pipeline utilizes the 'Preprocessed' directory to save temporary files 
for each preprocessing task. We suggest to remove this directory and 
the files contained in it once the pipeline has been run successfully.

#### Term list directory
Several term lists are employed. These lists are JSON files that must be located 
on the term list directory (a subdirectory of the WD). 
We suggest naming it 'Terminological_resources' (as that would be the default 
value taken by the pipeline).

### Configure the makefile
Once all prerequisites have been fulfilled and 
every dependency has been installed, 
the whole pipeline can be executed with a single make command:
```
$ make -f summarizer.mak All
```

You should indicate following data:
- `GEN_PATH`: working directory. 
- `TF_LIST`: TFs you want to retrieve information from. 
- `ARTICLES_PATH`: input articles directory (default 'Articles').
- `PREPROCESSED_PATH`: preprocessing directory (default 'Preprocessed'). 
- `TERMS_PATH`: term list directory  (default 'Terminological_resources'). 
- `STANFORD_POSTAGGER_PATH`: Stanford POS Tagger directory. 
- `BIO_LEMMATIZER_PATH`: BioLemmatizer directory. 

For further information, you can run the command: 
```
$ make -f summarizer.mak -Help
```
	
For more details about the parameters needed to run this pipeline, 
you can run the command:
```
$ make -f summarizer.mak -Parameters
```

Alternatevely, any step can be run by invoking the corresponding make task: 
'Help', 'Preprocessing', 'POS_Tagging', 'Entity_tagging','Transforming',
'Feature_extraction', 'Sentence_classification' and 'Summary_generation'.


### Run examples
With mandatory arguments only:
```
$ make -f summarizer.mak All GEN_PATH="/users/user1/automatic-summarization-transcription-factors" TF_LIST="DinJ-YafQ,ZraR,CRP,ArgR,PhoP,FadR,ArcA,UhpA,AlsR,PhoB,NemR,NadR,GutM,MqsA,ArsR,FhlA" STANFORD_POSTAGGER_PATH="/users/user1/stanford/stanford-postagger-2015-12-09" BIO_LEMMATIZER_PATH="/users/user1/biolemmatizer/BIO_LEMMATIZE"
```
	
With an additional (optional) argument:
```
$ make -f summarizer.mak All GEN_PATH="/users/user2/automatic-summarization-transcription-factors" TF_LIST="DinJ-YafQ,ZraR,CRP" STANFORD_POSTAGGER_PATH="/users/user2/stanford/stanford-postagger-2015-12-09" BIO_LEMMATIZER_PATH="/users/user1/biolemmatizer/BIO_LEMMATIZE" ARTICLES_PATH="/users/data/articles/ecoli"
```	

## Developers

* **Juan Antonio Blanchet Villezcas**
* **Alan Vladimir Godínez Plascencia**
* **Cristian Jesús González Colín**
* **Carlos Francisco Méndez Cruz**

## Contact 
Carlos Méndez: cmendezc at ccg.una.mx
