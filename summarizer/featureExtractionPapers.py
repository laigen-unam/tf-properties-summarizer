# -*- coding: UTF-8 -*-
import json
import re
from optparse import OptionParser
import os
import sys
from time import time

__author__ = 'CMendezC'

# Objective: Take transformed files with format word|lemma|pos,
#   for example: Multiple|multiple|JJ genetic|genetic|JJ variants|variant|NNS have|have|VBP
#   and create files with a different representation such as:
#   a) word = word
#   b) lemma = lemma
#   c) pos = pos
#   d) word_pos = word_pos word_pos
#   e) lemma_pos = lemma_pos lemma_pos

# Parameters:
#   1) --inputPath      Path to read files.
#   2) --outputPath     Path to write feature extraction files. File names are concatenated with feature name.
#   3) --feature        Type of feature to extract and create file: word, lemma, etc
#   4) --outputFile     File to concatenate all read files
#   5) --entityName     Entity names to filter sentences, names separated by -

# Ouput:
#   1) Files created. Name of feature is concatenated

# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR --feature lemma --outputFile ECK120012096_GntR.lemma.txt
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR --feature lemma_lemma_pos_pos --outputFile ECK120012096_GntR.lemma_lemma_pos_pos.txt
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR --feature word --outputFile ECK120012096_GntR.word.txt

# GntR
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR --feature lemma_lemma_pos_pos,word_word_pos_pos,lemma,word --outputFile ECK120012096_GntR.txt --entityName GntR
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012096_GntR --feature word --outputFile ECK120012096_GntR.txt

# FhlA
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011394_FhlA\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011394_FhlA --feature lemma_lemma_pos_pos,word_word_pos_pos,lemma,word --outputFile ECK120011394_FhlA.txt --entityName FhlA
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011394_FhlA\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011394_FhlA --feature word --outputFile ECK120011394_FhlA.txt

# MarA
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011412_MarA\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011412_MarA --feature lemma_lemma_pos_pos,word_word_pos_pos,lemma,word --outputFile ECK120011412_MarA.txt --entityName MarA
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011412_MarA\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011412_MarA --feature word --outputFile ECK120011412_MarA.txt

# ArgR
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011670_ArgR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011670_ArgR --feature lemma_lemma_pos_pos,word_word_pos_pos,lemma,word --outputFile ECK120011670_ArgR.txt --entityName ArgR
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011670_ArgR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011670_ArgR --feature word --outputFile ECK120011670_ArgR.txt

# CytR
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012407_CytR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012407_CytR --feature lemma_lemma_pos_pos,word_word_pos_pos,lemma,word --outputFile ECK120012407_CytR.txt --entityName CytR
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012407_CytR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012407_CytR --feature word --outputFile ECK120012407_CytR.txt

# Rob
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011190_Rob\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120011190_Rob --feature lemma_lemma_pos_pos,word_word_pos_pos,lemma,word --outputFile ECK120011190_Rob.txt --entityName Rob
# python featureExtractionPapers.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012407_CytR\transformed --outputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\TF_PMIDs_TXT_ECK120012407_CytR --feature word --outputFile ECK120012407_CytR.txt

# LREGULONDB
# python3.4 featureExtractionPapers.py
# --inputPath /home/cmendezc/lregulondb/transformed
# --outputPath /home/cmendezc/lregulondb/features
# --feature word,lemma

# Extraction of RIs and GCs. Automatic classification
# Evaluation dataset
# python3.4 featureExtractionPapers.py
# --inputPath /home/cmendezc/bitbucket_repositories/automatic-extraction-ris-gcs/automatic-classification/dataSets/test-dataSets/tra-sent
# --outputPath /home/cmendezc/bitbucket_repositories/automatic-extraction-ris-gcs/automatic-classification/dataSets/test-dataSets/features
# --feature word,lemma,lemma_lemma_pos_pos,lemma_lemma_tag_tag,tag4lemma
# --termPath /home/cmendezc/terminologicalResources
# --termFile termFilesTag_GC_ECCO.json
# python3.4 featureExtractionPapers.py --inputPath /home/cmendezc/bitbucket_repositories/automatic-extraction-ris-gcs/automatic-classification/dataSets/test-dataSets/tra-sent --outputPath /home/cmendezc/bitbucket_repositories/automatic-extraction-ris-gcs/automatic-classification/dataSets/test-dataSets/features --feature word,lemma,lemma_lemma_pos_pos,lemma_lemma_tag_tag,tag4lemma --termPath /home/cmendezc/terminologicalResources --termFile termFilesTag_GC_ECCO.json

###########################################################
#                       MAIN PROGRAM                      #
###########################################################

if __name__ == "__main__":
    # Parameter definition
    parser = OptionParser()
    parser.add_option("--inputPath", dest="inputPath",
                      help="Path to read files", metavar="PATH")
    parser.add_option("--outputPath", dest="outputPath",
                      help="Path to write feature extraction files, program is going to use --feature parameter to concatenate to file name.", metavar="PATH")
    parser.add_option("--features", dest="features",
                      help="Types of features to extract and create file: word, lemma, word_pos_word_pos, "
                           "lemma_pos_lemma_pos, pos, word_word_pos_pos, lemma_lemma_pos_pos, lemma_lemma_tag_tag, "
                           "word_word_tag_tag, tag, tag4word, tag4lemma", metavar="TEXT,TEXT")
    parser.add_option("--outputFile", dest="outputFile",
                      help="File to concatenate all read files", metavar="FILE")
    parser.add_option("--entityName", dest="entityName",
                      help="Entity name to filter sentences", metavar="FILE")
    parser.add_option("--concatenate", default=False,
                      action="store_true", dest="concatenate",
                      help="Concatenate all text into one file")
    parser.add_option("--termPath", dest="termPath",
                      help="Path to read term files", metavar="PATH")
    parser.add_option("--termFile", dest="termFile",
                      help="JSON file with terms files and tags", metavar="FILE")

    (options, args) = parser.parse_args()
    if len(args) > 0:
        parser.error("None parameters indicated.")
        sys.exit(1)

    # Printing parameter values
    print('-------------------------------- PARAMETERS --------------------------------')
    print("Path to read files: " + str(options.inputPath))
    print("Path to write feature extraction files: " + str(options.outputPath))
    print("Types of feature to extract: " + str(options.features))
    print("Output file: " + str(options.outputFile))
    print("Entity name to filter sentences: " + str(options.entityName))
    print("Concatenate all text into one file?: " + str(options.concatenate))
    print("Path to read term files: " + str(options.termPath))
    print("File to read terms", str(options.termFile))

    filesProcessed = 0
    t0 = time()

    featuresList = list(options.features.split(','))
    print("Features list: " + str(featuresList))

    if options.entityName is not None:
        # Creating regex for name entities as synonyms
        entityPattern = options.entityName + '\|'
        print('Pattern for entity names to filter: ' + entityPattern)

    hashTerms = {}
    print('Loading biological term files...')
    with open(os.path.join(options.termPath, options.termFile)) as data_file:
        hashes = json.load(data_file)
    hashTerms = hashes["hashTerms"]

    for path, dirs, files in os.walk(options.inputPath):
        for feature in featuresList:
            print("Extracting feature: " + feature)
            allText = ''
            for file in files:
                fileName = file[:file.find('.')]
                # print('     Filename: ' + fileName)
                with open(os.path.join(options.inputPath, file), mode="r", encoding="utf-8", errors="replace") as tFile:
                    print("   Extracting features from file..." + str(file))
                    lines = tFile.readlines()
                    filesProcessed += 1
                    with open(os.path.join(options.outputPath, file.replace('tra.txt', feature + '.txt')), "w", encoding="utf-8") as featFile:
                        lineNumber = 1
                        for line in lines:
                            wordLine = ''
                            lemmaLine = ''
                            posLine = ''
                            # Filtering by entityName
                            if options.entityName is not None:
                                # regexEntityName = re.compile(options.entityName + '\|')
                                regexEntityName = re.compile(entityPattern)
                                if regexEntityName.search(line) is None:
                                    continue
                                else:
                                    pass
                                    # print("     TF line: " + str(line.encode(encoding='UTF-8', errors='replace')))
                            for tok in line.split():
                                tokList = tok.split("|")
                                if len(tokList) < 3:
                                    print('Bad token:' + file + '-' + tok)
                                    continue
                                if feature == "word":
                                    wordLine += tokList[0] + " "
                                if feature == "lemma":
                                    lemmaLine += tokList[1] + " "
                                if feature == "pos":
                                    posLine += tokList[2] + " "
                                if feature == "word_pos_word_pos":
                                    wordLine += tokList[0] + "_" + tokList[2] + " "
                                if feature == "lemma_pos_lemma_pos":
                                    lemmaLine += tokList[1] + "_" + tokList[2] + " "
                                if feature == "word_word_pos_pos":
                                    wordLine += tokList[0] + " "
                                    posLine += tokList[2] + " "
                                if feature == "lemma_lemma_pos_pos":
                                    lemmaLine += tokList[1] + " "
                                    posLine += tokList[2] + " "
                                if feature == "word_word_tag_tag":
                                    wordLine += tokList[0] + " "
                                    if tokList[2] in hashTerms:
                                        posLine += tokList[2] + " "
                                if feature == "lemma_lemma_tag_tag":
                                    lemmaLine += tokList[1] + " "
                                    if tokList[2] in hashTerms:
                                        posLine += tokList[2] + " "
                                if feature == "tag":
                                    if tokList[2] in hashTerms:
                                        posLine += tokList[2] + " "

                                if feature == "tag4word":
                                    if tokList[2] in hashTerms:
                                        wordLine += tokList[2] + " "
                                    else:
                                        wordLine += tokList[0] + " "
                                if feature == "tag4lemma":
                                    if tokList[2] in hashTerms:
                                        lemmaLine += tokList[2] + " "
                                    else:
                                        lemmaLine += tokList[1] + " "


                            if feature == "word":
                                featFile.write(wordLine.strip() + '\n')
                                if options.concatenate:
                                    allText += fileName + '\t' + str(lineNumber) + '\t' + wordLine.strip() + '\n'
                            if feature == "lemma":
                                featFile.write(lemmaLine.strip() + '\n')
                                if options.concatenate:
                                    allText += fileName + '\t' + str(lineNumber) + '\t' + lemmaLine.strip() + '\n'
                            if feature in ["pos", "tag"]:
                                if options.concatenate:
                                    allText += fileName + '\t' + str(lineNumber) + '\t' + posLine.strip() + '\n'
                                featFile.write(posLine.strip() + '\n')
                            if feature in ["word_pos_word_pos", "tag4word"]:
                                featFile.write(wordLine.strip() + '\n')
                                if options.concatenate:
                                    allText += fileName + '\t' + str(lineNumber) + '\t' + wordLine.strip() + '\n'
                            if feature in ["lemma_pos_lemma_pos", "tag4lemma"]:
                                featFile.write(lemmaLine.strip() + '\n')
                                if options.concatenate:
                                    allText += fileName + '\t' + str(lineNumber) + '\t' + lemmaLine.strip() + '\n'
                            if feature in ["word_word_pos_pos", "word_word_tag_tag"]:
                                featFile.write(wordLine + posLine.strip() + '\n')
                                if options.concatenate:
                                    allText += fileName + '\t' + str(lineNumber) + '\t' + wordLine + posLine.strip() + '\n'
                            if feature in ["lemma_lemma_pos_pos", "lemma_lemma_tag_tag"]:
                                featFile.write(lemmaLine + posLine.strip() + '\n')
                                if options.concatenate:
                                    allText += fileName + '\t' + str(lineNumber) + '\t' + lemmaLine + posLine.strip() + '\n'
                            lineNumber += 1
            if options.concatenate:
                with open(os.path.join(options.outputPath, options.outputFile.replace('.txt', '.' + feature + '.txt')), "w", encoding="utf-8") as oFile:
                    oFile.write(allText)

    print("Files processed: " + str(filesProcessed))
