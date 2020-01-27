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
we generated summaries for 185 TFs of *Salmonella typhimurium* from 3498 articles. 

```
automatic-summaries
│
└───ecoli
└───salmonella
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
as training data to train an automatic summarizer. 
We manually classified the sentences of 177 manual summaries 
of TFs of RegulonDB in one or more of the six TF properties. 
To classify the sentences, we tagged specific relevant information associated 
to each TF property using XML tags.
We obtained a training data set with 2244 sentences in total 
formed by six subsets of sentences from all summaries, 
one per TF property. 
Positive examples were those pertaining to the TF property, 
while negative examples were all the remaining sentences. 


 
(see a description of this information in supplementary Table S1, 
and an example of a tagged manual summary in supplementary Figure S1). 


The automatic summaries are created by the concatenation of the automatically 
classified sentences from scientific articles, 
this is performed by an SVM classifier. 
The evaluation of these initial automatic summaries indicated 
that they carried part of the relevant information included in the 
manual summaries generated by the biocurator.

<!-- At the Computational Genomics Program (Center for Genome Sciences, UNAM), 
we conducted research on Biomedical natural language processing and Text mining 
to assist curation for  

This database contains a set of descriptions (summaries) of several properties of 
transcription factors (TFs). 
These summaries are manually written by curators employing several 
scientific articles. This activity takes significant time and effort due to the 
overwhelming amount of biomedical literature that keeps increasing every day. 

We aim to -->

## Transcription factors summarizer

### Input
You must place input files of the article collection within a subdirectory of your Working Directory (WD). 
We suggest naming it 'Articles' (as that would be the default value taken by 
the pipeline). Input files must be raw text files. 
Extension '.txt' is mandatory for these files.

# NLP preprocessing pipeline
The first step is preprocessing the input files. This step must be performed 
only once for the same article collection.

## Preprocessing directory
Our pipeline utilizes the 'Preprocessed' directory to save temporary files 
for each preprocessing task. We suggest to remove this directory and 
the files contained in it once the pipeline has been run successfully.

## Term list directory
Several term lists are employed. These lists are JSON files that must be located 
on the term list directory (a subdirectory of the WD). 
We suggest naming it 'Terminological_resources' (as that would be the default 
value taken by the pipeline).

## Prerequisites
You must have installed Stanford POS Tagger and BioLemmatizer in your computer. 
They are not included within this repository, have a look at the following 
references for instructions on the download and installation of these programs:
- Toutanova, K., Klein, D., Manning, C. and Singer, Y. (2003) Feature-rich part-of-speech tagging with a cyclic dependency network. In Proceedings of the HLT-NAACL, pp. 252-259.
- https://nlp.stanford.edu/software/tagger.shtml
- Liu, H., Christiansen, T., Baumgartner, W. A., Jr., and Verspoor, K. (2012) BioLemmatizer: a lemmatization tool for morphological processing of biomedical text. J. Biomed. Semantics, 3, 1-29.
- https://sourceforge.net/projects/biolemmatizer/


### Configure the makefile
Once all prerequisites have been fulfilled and every dependency has been installed, 
the whole pipeline can be executed with a single make command:
	make -f summarizer.mak All

You should indicate the TFs you want to retrieve information from:`TF_LIST`, your 
working directory: `GEN_PATH`, the path for the input articles directory (it is obligatory if your directory is not named 'Articles') `ARTICLES_PATH`, the preprocessing directory (it is obligatory if your directory is not named 'Preprocessed'): `PREPROCESSED_PATH`, the term list directory it is obligatory if your directory is not named 'Terminological_resources'): `ERMS_PATH`, the Stanford POS Tagger directory (`STANFORD_POSTAGGER_PATH`), the BioLemmatizer directory (`BIO_LEMMATIZER_PATH`). For further information, you can run the command: 
	make -f summarizer.mak -Help
For more details about the parameters needed to run this pipeline, you can run the 
command:
	make -f summarizer.mak -Parameters


Alternatevely, any subprocess can be run by invoking the corresponding make task: 
'Help', 'Preprocessing', 'POS_Tagging', 'Entity_tagging','Transforming',
'Feature_extraction', 'Sentence_classification' and 'Summary_generation'.


#### Examples:
	Ex. given with mandatory arguments only:
	make -f summarizer.mak All GEN_PATH="/users/user1/automatic-summarization-transcription-factors" TF_LIST="DinJ-YafQ,ZraR,CRP,ArgR,PhoP,FadR,ArcA,UhpA,AlsR,PhoB,NemR,NadR,GutM,MqsA,ArsR,FhlA" STANFORD_POSTAGGER_PATH="/users/user1/stanford/stanford-postagger-2015-12-09" BIO_LEMMATIZER_PATH="/users/user1/biolemmatizer/BIO_LEMMATIZE"
	Ex. given with an additional (optional) argument (detailed documentation on optional and mandatory arguments available running the commands: 'make -f summarizer.mak -Help' and 'make -f summarizer.mak -Parameters'):
	make -f summarizer.mak All GEN_PATH="/users/user2/automatic-summarization-transcription-factors" TF_LIST="DinJ-YafQ,ZraR,CRP" STANFORD_POSTAGGER_PATH="/users/user2/stanford/stanford-postagger-2015-12-09" BIO_LEMMATIZER_PATH="/users/user1/biolemmatizer/BIO_LEMMATIZE" ARTICLES_PATH="/users/data/articles/ecoli"


## Developers

* **Carlos Francisco Méndez Cruz**
* **Juan Antonio Blanchet Villezcas**
* **Alan Vladimir Godínez Plascencia**
* **Cristian Jesús González Colín**

## Contact 
Carlos Méndez: cmendezc at ccg.una.mx
