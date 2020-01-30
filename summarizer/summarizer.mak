SHELL := '/bin/bash'
###--------------------------------------------------------------------- DESCRIPTION ----------------------------------------------------------------------###

#	This makefile holds the commands needed to run our pipeline for automatic summarization of transcription factor (TF) properties.
#	This whole article-processing script is divided in some steps detailed in the 'Help' section of this script.
#   Following parameters must be considered:
#   - GEN_PATH: working directory.
#   - TF_LIST: TFs you want to retrieve information from.
#   - ARTICLES_PATH: input articles directory (default 'Articles').
#   - PREPROCESSED_PATH: preprocessing directory (default 'Preprocessed').
#   - TERMS_PATH: term list directory  (default 'Terminological_resources').
#   - STANFORD_POSTAGGER_PATH: Stanford POS Tagger directory.
#   - BIO_LEMMATIZER_PATH: BioLemmatizer directory.

#	Created by: Alan Vladimir (agodinez at lcg.unam.mx) and Carlos Méndez (cmendezc at ccg.unam.mx).

###-----------------------------------------------------------------------------------------------------------------------------------------------------------###
###---------------------------------------------------------------------- PARAMETERS ----------------------------------------------------------------------###

## --TFS of interest -- ##

## --- Change this variable to that of your Transcription Factors of interest--- ##
#TF_LIST=DinJ-YafQ,ZraR,CRP,ArgR,PhoP,FadR,ArcA,UhpA,AlsR,PhoB,NemR,NadR,GutM,MqsA,ArsR,FhlA,YgiV,PspF,YdfH,DpiA,AsnC,EbgR,MprA,SlyA,NagC,EvgA,BglJ,IHF,RtcR,YefM-YoeB,CreB,HdfR,LexA,MazE-MazF,AscG,PutA,BasR,CusR,YdeO,LldR,LeuO,MhpR,RbsR,GalS,BaeR,RcdA,CdaR,NarL,NhaR,DicA,GlpR,RutR,Fur,SgrR,Lrp,Zur,MlrA,AraC,AtoC,MraZ,DhaR,NikR,BetI,YpdB,SutR,PuuR,NanR,H-NS,YefM,RelB,FucR,GadX,FabR,YehT,MarA,BluR,UidR,KdgR,MurR,BirA,RhaS,FeaR,UlaR,PaaX,CueR,Dan,McbR,DeoR,RcnR,ZntR,ModE,CynR,CspA,UxuR,MelR,MazE,OmpR,AlpA,HipAB,TrpR,EnvY,CsgD,EnvR,HU,FliZ,Cbl,RstA,HyfR,ComR,MalI,RhaR,RcsB-BglJ,DnaA,GatR,Nac,Cra,AgaR,TdcA,GutR,BolA,IclR,GadW,Mlc,PgrR,LrhA,Ada,TdcR,HipB,MatA,YeiL,SoxS,OxyR,HypT,NorR,AllS,ArgP,NarP,GadE,XapR,AppY,CsiR,PrpR,Rob,RclR,CadC,MalT,FlhDC,QseB,TreR,SoxR,MntR,AdiY,PdhR,CytR,IscR,LsrR,YiaJ,DcuR,XylR,IdnR,MetJ,LacI,MtlR,NtrC,AcrR,SdiA,GcvA,LysR,GalR,YqhC,GntR,YqjI,FNR,MngR,KdpE,ExuR,StpA,DsdC
TF_LIST=EcnR,YdcI,RhaR,DeoR

## -- Working directories -- ##
## --- Set these variables to your paths --- ##

#General working directory path.
GEN_PATH=/home/cmendezc/github_repositories/tf-properties-summarizer/tf-properties-summarizer

#Directory path containing tf articles.
ARTICLES_PATH=${GEN_PATH}/Articles

#Directory path containing property-named subdirectories with the corresponding dictionaries of terms and json files.
TERMS_PATH=${GEN_PATH}/Terminological_resources_salmonella

#Directory path containing preprocessed articles.
PREPROCESSED_PATH=${GEN_PATH}/Preprocessed

#Directory path containing part-of-speech tagged articles.
POS_PATH=${GEN_PATH}/POS_tagged

#Directory path containing the processed articles after lemmatization.
LEMMATIZED_PATH=${GEN_PATH}/Lemmatized

#Directory path containing articles tagged with the entities recognized.
ENTITY_PATH=${GEN_PATH}/Entities

#Directory path containing the transformed sentences.
TRANSFORMED_PATH=${GEN_PATH}/Transformed/tra

#Directory path containing the text from the original articles.
TRANSFORMED_TEXT_PATH=${GEN_PATH}/Transformed/text

#Directory path containing articles after feature extraction (not word).
FEATURE_PATH=${GEN_PATH}/Features/features

#Directory path containing articles after feature extraction (word only)
WORD_PATH=${GEN_PATH}/Features/word

#Directory path containing articles after feature extraction.
CLASSIFY_PATH=${GEN_PATH}/Classified

#Directory path containing txt and HTML versions of the final summaries.
SUMMARY_PATH=${GEN_PATH}/Summaries

#Directory paths containing models needed for sentence classification.
ACT_MODEL_PATH=${GEN_PATH}/Models_vectorizers/ACT
DOM_MODEL_PATH=${GEN_PATH}/Models_vectorizers/DOM
EVO_MODEL_PATH=${GEN_PATH}/Models_vectorizers/EVO
RP_MODEL_PATH=${GEN_PATH}/Models_vectorizers/RP
SIT_MODEL_PATH=${GEN_PATH}/Models_vectorizers/SIT
TU_MODEL_PATH=${GEN_PATH}/Models_vectorizers/TU

#Directory path containing articles after feature extraction.
ROUGE_PATH=${GEN_PATH}/Rouge_test

#Stanford POS Tagger directory.
STANFORD_POSTAGGER_PATH=/home/cmendezc/STANFORD_POSTAGGER/stanford-postagger-2018-02-27

#BioLemmatizer directory.
BIO_LEMMATIZER_PATH=/home/cmendezc/BIO_LEMMATIZER

#All pipeline
All: Help Parameters Preprocessing POS_tagging Lemmatizing Entity_tagging Transforming Feature_extraction Sentence_classification

#### SE ESCRIBIRÁN MÁS CUANDO SE REALIZE EL PIPELINE 'AUTOMATIC SUMMARIZATION'####
NLP_preprocess: Parameters Preprocessing POS_tagging Lemmatizing Entity_recognition Transforming Feature_extraction
#### SE ESCRIBIRÁN MÁS CUANDO SE REALIZE EL PIPELINE 'AUTOMATIC SUMMARIZATION'####
### Summarization: Parameters ###


###--------------------------------------------------------------- PRINT HELP ABOUT THIS FILE -------------------------------------------------------------###
Help:
	@echo "Target list:"
	@echo "Help                       List available targets."
	@echo "Parameters                 List the parameters required by this program."
	@echo "Preprocessing              'Clean' the articles to be summarized and detect entities within them."
	@echo "POS_tagging                Assign a tag to each word within the given files based on its part-of-speech category."
	@echo "Lemmatizing                Assing the lemma that corresponds to each word within the given files."
	@echo "Entity_tagging             Assign a tag to each 'entity' within the given files based on entity recognition."
	@echo "Transforming               Generate the internal representation of the sentences: WORD|LEMMA|POS."
	@echo "Feature_extraction         Generate the different sentence representations: lemma_lemma_tag_tag, lemma_lemma_pos_pos, etc."
	@echo "Sentence_classification    Classify the newly-generated sentences."
	@echo "Summary_generation         Generate automatic summaries in text and html format."
	@echo "All:                       Run all pipeline."

    ### SE ESCRIBIRÁN MÁS CUANDO SE REALIZE EL PIPELINE 'AUTOMATIC SUMMARIZATION'###
	#@echo "NLP_preprocess     Run all tasks from the 'NLP preprocessing pipeline.'"
	#@echo "Summarization      Run all tasks from the 'automatic summarization pipeline'."


###------------------------------------------------------------------- PRINT PARAMETERS -------------------------------------------------------------------###
Parameters:
	@echo "###------------------------------------------------ DESCRIPTION ------------------------------------------------###"
	@echo "This makefile holds the commands needed to run our pipeline for automatic summarization of transcription factor (TF) properties.
	@echo "###------------------------------------------------ PARAMETERS ------------------------------------------------###"
	@echo "General pathway: ${GEN_PATH}"
	@echo "Articles pathway: ${ARTICLES_PATH}"
	@echo "Terminological resources pathway(term dictionaries and json files): ${TERMS_PATH}"
	@echo "Preprocessed files pathway: ${PREPROCESSED_PATH}"
	@echo "POS tagged files pathway: ${POS_PATH}"
	@echo "Files after lemmatizing pathway: ${LEMMATIZED_PATH}"
	@echo "Entity tagged files pathway: ${ENTITY_PATH}"
	@echo "Transformed files pathway: ${TRANSFORMED_PATH}"
	@echo "Output files (after feature extraction) pathway: ${FEATURE_PATH}"
	@echo "Classified sentences pathway: ${CLASSIFY_PATH}" 
	#### SE ESCRIBIRÁN MÁS CUANDO SE REALIZE EL PIPELINE 'AUTOMATIC SUMMARIZATION'####
	@echo "For additional information about the files you are working with, have a look at our repository: (link del git)."


###----------------------------------------------------------------- ARTICLE PREPROCESSING ----------------------------------------------------------------###
Preprocessing:
	@echo "###----------------------------------------------------------------- ARTICLE PREPROCESSING ----------------------------------------------------------------###"
	@echo "'Clean' the articles to be summarized and detect entities within them"
	@echo "Generating preprocessed articles pathway and subdirectories..."

	@mkdir -p ${PREPROCESSED_PATH} 
	@mkdir -p ${PREPROCESSED_PATH}/ACT && mkdir -p ${PREPROCESSED_PATH}/DOM && mkdir -p ${PREPROCESSED_PATH}/EVO && mkdir -p ${PREPROCESSED_PATH}/RP && mkdir -p ${PREPROCESSED_PATH}/SIT && mkdir -p ${PREPROCESSED_PATH}/TU
	
	@echo "Done!"
	
	@echo "Preprocessing paper files..."
	
	@python3 preprocessingTermDetection.py --inputPath ${ARTICLES_PATH} --outputPath ${PREPROCESSED_PATH}/ACT --termDetection --termPath ${TERMS_PATH}/ACT --termFiles ${TERMS_PATH}/ACT/termFilesLength_TFSummarization.json 
	@python3 preprocessingTermDetection.py --inputPath ${ARTICLES_PATH} --outputPath ${PREPROCESSED_PATH}/DOM --termDetection --termPath ${TERMS_PATH}/DOM --termFiles ${TERMS_PATH}/DOM/termFilesLength_TFSummarization.json 
	@python3 preprocessingTermDetection.py --inputPath ${ARTICLES_PATH} --outputPath ${PREPROCESSED_PATH}/EVO --termDetection --termPath ${TERMS_PATH}/EVO --termFiles ${TERMS_PATH}/EVO/termFilesLength_TFSummarization.json 
	@python3 preprocessingTermDetection.py --inputPath ${ARTICLES_PATH} --outputPath ${PREPROCESSED_PATH}/RP --termDetection --termPath ${TERMS_PATH}/RP --termFiles ${TERMS_PATH}/RP/termFilesLength_TFSummarization.json 
	@python3 preprocessingTermDetection.py --inputPath ${ARTICLES_PATH} --outputPath ${PREPROCESSED_PATH}/SIT --termDetection --termPath ${TERMS_PATH}/SIT --termFiles ${TERMS_PATH}/SIT/termFilesLength_TFSummarization.json 
	@python3 preprocessingTermDetection.py --inputPath ${ARTICLES_PATH} --outputPath ${PREPROCESSED_PATH}/TU --termDetection --termPath ${TERMS_PATH}/TU --termFiles ${TERMS_PATH}/TU/termFilesLength_TFSummarization.json 

	@echo "Done!"


###---------------------------------------------------------------------------- PART OF SPEECH TAGGING ----------------------------------------------------------------------------###
POS_tagging:
	@echo "###----------------------- PART OF SPEECH TAGGING -----------------------###"
	@echo "Assign a tag to each word within the given files based on its part-of-speech category."
	@echo "Generating POS-processed files pathway and subdirectories..."

	@mkdir -p ${POS_PATH}
	@mkdir -p ${POS_PATH}/ACT && mkdir -p ${POS_PATH}/DOM && mkdir -p ${POS_PATH}/EVO && mkdir -p ${POS_PATH}/RP && mkdir -p ${POS_PATH}/SIT && mkdir -p ${POS_PATH}/TU 

	@echo "Done!"

	@echo "Part Of Speach tagging:"

	@python3 posTaggingStanford.py --inputPath ${PREPROCESSED_PATH}/ACT --outputPath ${POS_PATH}/ACT --taggerPath ${STANFORD_POSTAGGER_PATH} --biolemmatizer
	@python3 posTaggingStanford.py --inputPath ${PREPROCESSED_PATH}/DOM --outputPath ${POS_PATH}/DOM --taggerPath ${STANFORD_POSTAGGER_PATH} --biolemmatizer
	@python3 posTaggingStanford.py --inputPath ${PREPROCESSED_PATH}/EVO --outputPath ${POS_PATH}/EVO --taggerPath ${STANFORD_POSTAGGER_PATH} --biolemmatizer 
	@python3 posTaggingStanford.py --inputPath ${PREPROCESSED_PATH}/RP --outputPath ${POS_PATH}/RP --taggerPath ${STANFORD_POSTAGGER_PATH} --biolemmatizer 
	@python3 posTaggingStanford.py --inputPath ${PREPROCESSED_PATH}/SIT --outputPath ${POS_PATH}/SIT --taggerPath ${STANFORD_POSTAGGER_PATH} --biolemmatizer 
	@python3 posTaggingStanford.py --inputPath ${PREPROCESSED_PATH}/TU --outputPath ${POS_PATH}/TU --taggerPath ${STANFORD_POSTAGGER_PATH} --biolemmatizer 

	@echo "Done!"


###---------------------------------------------------- SENTENCE LEMMATIZING ----------------------------------------------------###
Lemmatizing:
	@echo "###-------------------------------------------------- SENTENCE LEMMATIZING --------------------------------------------------###"
	@echo "Assign the lemma that corresponds to each word within the given files."
	@echo "Generating lemmatized files, pathway and subdirectories..."

	@mkdir -p ${LEMMATIZED_PATH}
	@mkdir -p ${LEMMATIZED_PATH}/ACT && mkdir -p ${LEMMATIZED_PATH}/DOM && mkdir -p ${LEMMATIZED_PATH}/EVO && mkdir -p ${LEMMATIZED_PATH}/RP && mkdir -p ${LEMMATIZED_PATH}/SIT && mkdir -p ${LEMMATIZED_PATH}/TU

	@echo "Done!"

	@echo "Lemmatizing files:"

	@python3 biolemmatizing.py --inputPath ${POS_PATH}/ACT --outputPath ${LEMMATIZED_PATH}/ACT --biolemmatizerPath ${BIO_LEMMATIZER_PATH}
	@python3 biolemmatizing.py --inputPath ${POS_PATH}/DOM --outputPath ${LEMMATIZED_PATH}/DOM --biolemmatizerPath ${BIO_LEMMATIZER_PATH}
	@python3 biolemmatizing.py --inputPath ${POS_PATH}/EVO --outputPath ${LEMMATIZED_PATH}/EVO --biolemmatizerPath ${BIO_LEMMATIZER_PATH}
	@python3 biolemmatizing.py --inputPath ${POS_PATH}/RP --outputPath ${LEMMATIZED_PATH}/RP --biolemmatizerPath ${BIO_LEMMATIZER_PATH}
	@python3 biolemmatizing.py --inputPath ${POS_PATH}/SIT --outputPath ${LEMMATIZED_PATH}/SIT --biolemmatizerPath ${BIO_LEMMATIZER_PATH}
	@python3 biolemmatizing.py --inputPath ${POS_PATH}/TU --outputPath ${LEMMATIZED_PATH}/TU --biolemmatizerPath ${BIO_LEMMATIZER_PATH}

	@echo "Done!"


###----------------------------------------------------- RECOGNIZED ENTITIES TAGGING --------------------------------------------------------###
Entity_tagging: 
	@echo "###--------------------- RECOGNIZED ENTITIES TAGGING --------------------###"
	@echo "Assign a tag to each 'entity' within the given files based on entity recognition"
	@echo "Generating lemmatized files, pathway and subdirectories..."

	@mkdir -p ${ENTITY_PATH}
	@mkdir -p ${ENTITY_PATH}/ACT && mkdir -p ${ENTITY_PATH}/DOM && mkdir -p ${ENTITY_PATH}/EVO && mkdir -p ${ENTITY_PATH}/RP && mkdir -p ${ENTITY_PATH}/SIT && mkdir -p ${ENTITY_PATH}/TU

	@echo "Done!"
	
	@echo "Tagging entities..."

	@python3 biologicalTermTagging.py --inputPath ${LEMMATIZED_PATH}/ACT --outputPath ${ENTITY_PATH}/ACT --termPath ${TERMS_PATH}/ACT --termFiles ${TERMS_PATH}/ACT/termFilesTag_TFSummarization_FreqWords.json
	@python3 biologicalTermTagging.py --inputPath ${LEMMATIZED_PATH}/DOM --outputPath ${ENTITY_PATH}/DOM --termPath ${TERMS_PATH}/DOM --termFiles ${TERMS_PATH}/DOM/termFilesTag_TFSummarization_FreqWords.json
	@python3 biologicalTermTagging.py --inputPath ${LEMMATIZED_PATH}/EVO --outputPath ${ENTITY_PATH}/EVO --termPath ${TERMS_PATH}/EVO --termFiles ${TERMS_PATH}/EVO/termFilesTag_TFSummarization_FreqWords.json
	@python3 biologicalTermTagging.py --inputPath ${LEMMATIZED_PATH}/RP --outputPath ${ENTITY_PATH}/RP --termPath ${TERMS_PATH}/RP --termFiles ${TERMS_PATH}/RP/termFilesTag_TFSummarization_FreqWords.json
	@python3 biologicalTermTagging.py --inputPath ${LEMMATIZED_PATH}/SIT --outputPath ${ENTITY_PATH}/SIT --termPath ${TERMS_PATH}/SIT --termFiles ${TERMS_PATH}/SIT/termFilesTag_TFSummarization_FreqWords.json
	@python3 biologicalTermTagging.py --inputPath ${LEMMATIZED_PATH}/TU --outputPath ${ENTITY_PATH}/TU --termPath ${TERMS_PATH}/TU --termFiles ${TERMS_PATH}/TU/termFilesTag_TFSummarization_FreqWords.json

	@echo "Done!"


###----------------------------------------------------- SENTENCE TRANSFORMATION --------------------------------------------------------###
Transforming: 
	@echo "###----------------------- SENTENCE TRANSFORMATION ----------------------###"
	@echo 'Generate the internal representation of the sentences: WORD|LEMMA|POS'
	@echo "Generating transformed files, pathway and subdirectories..."

	@mkdir -p ${TRANSFORMED_PATH} && mkdir -p ${TRANSFORMED_TEXT_PATH}
	@mkdir -p ${TRANSFORMED_PATH}/ACT && mkdir -p ${TRANSFORMED_PATH}/DOM && mkdir -p ${TRANSFORMED_PATH}/EVO && mkdir -p ${TRANSFORMED_PATH}/RP && mkdir -p ${TRANSFORMED_PATH}/SIT && mkdir -p ${TRANSFORMED_PATH}/TU
	@mkdir -p ${TRANSFORMED_TEXT_PATH}/ACT && mkdir -p ${TRANSFORMED_TEXT_PATH}/DOM && mkdir -p ${TRANSFORMED_TEXT_PATH}/EVO && mkdir -p ${TRANSFORMED_TEXT_PATH}/RP && mkdir -p ${TRANSFORMED_TEXT_PATH}/SIT && mkdir -p ${TRANSFORMED_TEXT_PATH}/TU

	@echo "Done!"

	@echo "Transforming sentences..."

	@python3 transforming.py --inputPath ${ENTITY_PATH}/ACT --transformedPath ${TRANSFORMED_PATH}/ACT --textPath ${TRANSFORMED_TEXT_PATH}/ACT --termPath ${TERMS_PATH}/ACT --termFiles ${TERMS_PATH}/ACT/termFilesTag_TFSummarization_FreqWords.json
	@python3 transforming.py --inputPath ${ENTITY_PATH}/DOM --transformedPath ${TRANSFORMED_PATH}/DOM --textPath ${TRANSFORMED_TEXT_PATH}/DOM --termPath ${TERMS_PATH}/DOM --termFiles ${TERMS_PATH}/DOM/termFilesTag_TFSummarization_FreqWords.json
	@python3 transforming.py --inputPath ${ENTITY_PATH}/EVO --transformedPath ${TRANSFORMED_PATH}/EVO --textPath ${TRANSFORMED_TEXT_PATH}/EVO --termPath ${TERMS_PATH}/EVO --termFiles ${TERMS_PATH}/EVO/termFilesTag_TFSummarization_FreqWords.json
	@python3 transforming.py --inputPath ${ENTITY_PATH}/RP --transformedPath ${TRANSFORMED_PATH}/RP --textPath ${TRANSFORMED_TEXT_PATH}/RP --termPath ${TERMS_PATH}/RP --termFiles ${TERMS_PATH}/RP/termFilesTag_TFSummarization_FreqWords.json
	@python3 transforming.py --inputPath ${ENTITY_PATH}/TU --transformedPath ${TRANSFORMED_PATH}/TU --textPath ${TRANSFORMED_TEXT_PATH}/TU/ --termPath ${TERMS_PATH}/TU --termFiles ${TERMS_PATH}/TU/termFilesTag_TFSummarization_FreqWords.json
	@python3 transforming_sit.py --inputPath ${ENTITY_PATH}/SIT --transformedPath ${TRANSFORMED_PATH}/SIT --textPath ${TRANSFORMED_TEXT_PATH}/SIT --termPath ${TERMS_PATH}/SIT --termFiles ${TERMS_PATH}/SIT/termFilesTag_TFSummarization_FreqWords.json

	@echo "Done!"


###----------------------------------------------------- FEATURE EXTRACTION --------------------------------------------------------###
Feature_extraction: 
	@echo "###------------------------- FEATURE EXTRACTION -------------------------###"
	@echo "Generate the different sentence representations: lemma_lemma_tag_tag, lemma_lemma_pos_pos, etc."
	@echo "Generating the final files of the 'nlp preprocessing pipeline', pathway and subdirectories..."

	@mkdir -p ${FEATURE_PATH} && mkdir -p ${WORD_PATH}
	@mkdir -p ${FEATURE_PATH}/ACT && mkdir -p ${FEATURE_PATH}/DOM && mkdir -p ${FEATURE_PATH}/EVO && mkdir -p ${FEATURE_PATH}/RP && mkdir -p ${FEATURE_PATH}/SIT && mkdir -p ${FEATURE_PATH}/TU
	@mkdir -p ${WORD_PATH}/ACT && mkdir -p ${WORD_PATH}/DOM && mkdir -p ${WORD_PATH}/EVO && mkdir -p ${WORD_PATH}/RP && mkdir -p ${WORD_PATH}/SIT && mkdir -p ${WORD_PATH}/TU

	@echo "Done!"

	@echo "Extracting features..."

	@tfs="${TF_LIST}" ; \
	IFS=',' read -r -a TF_Array <<< "$$tfs" ; \
	echo $${#TF_Array[*]}; \
	for tf in $${TF_Array[@]}; \
	do \
                mkdir -p ${FEATURE_PATH}/DOM/$$tf && mkdir -p ${WORD_PATH}/DOM/$$tf && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/DOM --outputPath ${FEATURE_PATH}/DOM/$$tf --feature lemma_lemma_tag_tag --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/DOM --termFile ${TERMS_PATH}/DOM/termFilesTag_TFSummarization_FreqWords.json --concatenate && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/DOM --outputPath ${WORD_PATH}/DOM/$$tf --feature word --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/DOM --termFile ${TERMS_PATH}/DOM/termFilesTag_TFSummarization_FreqWords.json --concatenate && mkdir -p ${FEATURE_PATH}/ACT/$$tf && mkdir -p ${WORD_PATH}/ACT/$$tf && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/ACT --outputPath ${FEATURE_PATH}/ACT/$$tf --feature lemma_lemma_tag_tag --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/ACT --termFile ${TERMS_PATH}/ACT/termFilesTag_TFSummarization_FreqWords.json --concatenate && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/ACT --outputPath ${WORD_PATH}/ACT/$$tf --feature word --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/ACT --termFile ${TERMS_PATH}/ACT/termFilesTag_TFSummarization_FreqWords.json --concatenate && mkdir -p ${FEATURE_PATH}/EVO/$$tf && mkdir -p ${WORD_PATH}/EVO/$$tf && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/EVO --outputPath ${FEATURE_PATH}/EVO/$$tf --feature lemma_lemma_pos_pos --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/EVO --termFile ${TERMS_PATH}/EVO/termFilesTag_TFSummarization_FreqWords.json --concatenate && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/EVO --outputPath ${WORD_PATH}/EVO/$$tf --feature word --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/EVO --termFile ${TERMS_PATH}/EVO/termFilesTag_TFSummarization_FreqWords.json --concatenate && mkdir -p ${FEATURE_PATH}/RP/$$tf && mkdir -p ${WORD_PATH}/RP/$$tf && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/RP --outputPath ${FEATURE_PATH}/RP/$$tf --feature lemma_lemma_pos_pos --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/RP --termFile ${TERMS_PATH}/RP/termFilesTag_TFSummarization_FreqWords.json --concatenate && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/RP --outputPath ${WORD_PATH}/RP/$$tf --feature word --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/RP --termFile ${TERMS_PATH}/RP/termFilesTag_TFSummarization_FreqWords.json --concatenate && mkdir -p ${FEATURE_PATH}/SIT/$$tf && mkdir -p ${WORD_PATH}/SIT/$$tf && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/SIT --outputPath ${FEATURE_PATH}/SIT/$$tf --feature tag4lemma --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/SIT --termFile ${TERMS_PATH}/SIT/termFilesTag_TFSummarization_FreqWords.json --concatenate && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/SIT --outputPath ${WORD_PATH}/SIT/$$tf --feature word --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/SIT --termFile ${TERMS_PATH}/SIT/termFilesTag_TFSummarization_FreqWords.json --concatenate && mkdir -p ${FEATURE_PATH}/TU/$$tf && mkdir -p ${WORD_PATH}/TU/$$tf && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/TU --outputPath ${FEATURE_PATH}/TU/$$tf --feature lemma_lemma_tag_tag --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/TU --termFile ${TERMS_PATH}/TU/termFilesTag_TFSummarization_FreqWords.json --concatenate && python3 featureExtractionPapers.py --inputPath ${TRANSFORMED_PATH}/TU --outputPath ${WORD_PATH}/TU/$$tf --feature word --outputFile $$tf\_concatenated.txt --entityName $$tf --termPath ${TERMS_PATH}/TU --termFile ${TERMS_PATH}/TU/termFilesTag_TFSummarization_FreqWords.json --concatenate; \
	done

	@echo "Done!"


###----------------------------------------------------- SENTENCE CLASSIFICATION --------------------------------------------------------###
Sentence_classification: 
	@echo "###----------------------- SENTENCE CLASSIFICATION ----------------------###"
	@echo 'Sentence classification:'
	@echo "Generating transformed files, pathway and subdirectories..."

	# @mkdir -p ${CLASSIFY_PATH}
	# @mkdir -p ${CLASSIFY_PATH}/ACT && mkdir -p ${CLASSIFY_PATH}/DOM && mkdir -p ${CLASSIFY_PATH}/EVO && mkdir -p ${CLASSIFY_PATH}/RP && mkdir -p ${CLASSIFY_PATH}/SIT && mkdir -p ${CLASSIFY_PATH}/TU
	# @mkdir -p ${ACT_MODEL_PATH} && mkdir -p ${DOM_MODEL_PATH} && mkdir -p ${EVO_MODEL_PATH} && mkdir -p ${TU_MODEL_PATH} && mkdir -p ${RP_MODEL_PATH} && mkdir -p ${SIT_MODEL_PATH}

	#@echo "Done!"

	@echo "Classifying sentences..."

	@tfs="${TF_LIST}" ; \
	IFS=',' read -r -a TF_Array <<< "$$tfs" ; \
	echo $${#TF_Array[*]}; \
	for tf in $${TF_Array[@]}; \
	do \
                mkdir -p ${CLASSIFY_PATH}/ACT/$$tf && python3 classify.py --inputPath ${FEATURE_PATH}/ACT/$$tf --inputFile $$tf\_concatenated.lemma_lemma_tag_tag.txt --outputPath ${CLASSIFY_PATH}/ACT/$$tf --inputTXTPath ${WORD_PATH}/ACT/$$tf --inputTXTFile $$tf\_concatenated.word.txt --modelPath ${ACT_MODEL_PATH} --modelName l_l_t_t.TFIDF.swFalse.sn1.fn2.tfbinFalse.RandomUS.0.SVMrbf --outputFile lemma_lemma_tag_tag.classified.txt && mkdir -p ${CLASSIFY_PATH}/DOM/$$tf && python3 classify.py --inputPath ${FEATURE_PATH}/DOM/$$tf --inputFile $$tf\_concatenated.lemma_lemma_tag_tag.txt --outputPath ${CLASSIFY_PATH}/DOM/$$tf --inputTXTPath ${WORD_PATH}/DOM/$$tf --inputTXTFile $$tf\_concatenated.word.txt --modelPath ${DOM_MODEL_PATH} --modelName l_l_t_t.TFIDF.swFalse.sn1.fn1.tfbinFalse.SVD.200.SVMrbf --outputFile lemma_lemma_tag_tag.classified.txt && mkdir -p ${CLASSIFY_PATH}/EVO/$$tf && python3 classify.py --inputPath ${FEATURE_PATH}/EVO/$$tf --inputFile $$tf\_concatenated.lemma_lemma_pos_pos.txt --outputPath ${CLASSIFY_PATH}/EVO/$$tf --inputTXTPath ${WORD_PATH}/EVO/$$tf --inputTXTFile $$tf\_concatenated.word.txt --modelPath ${EVO_MODEL_PATH} --modelName l_l_p_p.TFIDF.swFalse.sn1.fn1.tfbinTrue.SVD.200.SVMrbf --outputFile l_l_p_p.classified.txt && mkdir -p ${CLASSIFY_PATH}/RP/$$tf && python3 classify.py --inputPath ${FEATURE_PATH}/RP/$$tf --inputFile $$tf\_concatenated.lemma_lemma_pos_pos.txt --outputPath ${CLASSIFY_PATH}/RP/$$tf --inputTXTPath ${WORD_PATH}/RP/$$tf --inputTXTFile $$tf\_concatenated.word.txt --modelPath ${RP_MODEL_PATH} --modelName l_l_p_p.TFIDF.swFalse.sn1.fn2.tfbinTrue.SVD.200.SVMrbf --outputFile lemma_lemma_pos_pos.classified.txt && mkdir -p ${CLASSIFY_PATH}/SIT/$$tf && python3 classify.py --inputPath ${FEATURE_PATH}/SIT/$$tf --inputFile $$tf\_concatenated.tag4lemma.txt --inputTXTFile $$tf\_concatenated.word.txt --outputPath ${CLASSIFY_PATH}/SIT/$$tf --inputTXTPath ${WORD_PATH}/SIT/$$tf --modelPath ${SIT_MODEL_PATH} --modelName tag4lemma.TFIDF.swFalse.sn1.fn1.tfbinTrue.SVD.200.SVMrbf --outputFile tag4lemma.classified.txt && mkdir -p ${CLASSIFY_PATH}/TU/$$tf && python3 classify.py --inputPath ${FEATURE_PATH}/TU/$$tf --inputFile $$tf\_concatenated.lemma_lemma_tag_tag.txt --outputPath ${CLASSIFY_PATH}/TU/$$tf --inputTXTPath ${WORD_PATH}/TU/$$tf --inputTXTFile $$tf\_concatenated.word.txt --modelPath ${TU_MODEL_PATH} --modelName l_l_t_t.TFIDF.swFalse.sn1.fn1.tfbinTrue.SVD.200.SVMrbf --outputFile lemma_lemma_tag_tag.classified.txt; \
	done

	@echo "Done!"
	
	
###----------------------------------------------------- Summary generation ---------------------------------------------------------###
Summary_generation: 
	@echo "###----------------------- SUMMARY GENERATION ----------------------###"
	@echo "Retrieving txt formatted summaries..."

	@python3 getSummaries_bySimilarity.py --classifiedPath ${CLASSIFY_PATH}/ACT --wordPath ${WORD_PATH}/ACT --sumPath ${SUMMARY_PATH}/ACT --feature lemma_lemma_tag_tag --tfList ${TF_LIST} --similarity 0.8
	@python3 getSummaries_bySimilarity.py --classifiedPath ${CLASSIFY_PATH}/DOM --wordPath ${WORD_PATH}/DOM --sumPath ${SUMMARY_PATH}/DOM --feature lemma_lemma_tag_tag --tfList ${TF_LIST} --similarity 0.8
	@python3 getSummaries_bySimilarity.py --classifiedPath ${CLASSIFY_PATH}/EVO --wordPath ${WORD_PATH}/EVO --sumPath ${SUMMARY_PATH}/EVO --feature l_l_p_p --tfList ${TF_LIST} --similarity 0.8
	@python3 getSummaries_bySimilarity.py --classifiedPath ${CLASSIFY_PATH}/RP --wordPath ${WORD_PATH}/RP --sumPath ${SUMMARY_PATH}/RP --feature lemma_lemma_pos_pos --tfList ${TF_LIST} --similarity 0.8
	@python3 getSummaries_bySimilarity.py --classifiedPath ${CLASSIFY_PATH}/SIT --wordPath ${WORD_PATH}/SIT --sumPath ${SUMMARY_PATH}/SIT --feature tag4lemma --tfList ${TF_LIST} --similarity 0.8
	@python3 getSummaries_bySimilarity.py --classifiedPath ${CLASSIFY_PATH}/TU --wordPath ${WORD_PATH}/TU --sumPath ${SUMMARY_PATH}/TU --feature lemma_lemma_tag_tag --tfList ${TF_LIST} --similarity 0.8

	@echo "Done!"

	@echo "Retrieving HTML formatted summaries..."

	@python3 getCompleteSummaries.py --path ${SUMMARY_PATH} --tfList ${TF_LIST}
	@python3 htmlMaker.py --inputPath ${SUMMARY_PATH}/complete --htmlPath ${SUMMARY_PATH}/html
 
	@echo "Done!"

############################################################################################################################################################

	@echo "All generated files can be accesed at: '${GEN_PATH}'"
