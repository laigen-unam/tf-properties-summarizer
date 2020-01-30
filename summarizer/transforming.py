# -*- coding: UTF-8 -*-
import re
from optparse import OptionParser
import os
import sys
from time import time

__author__ = 'CMendezC'

#Modified by Blanchet | Regular expression for SSA tag identification

# Objective: Transforming BIOLemmatized files:
#   1) Transformed files
#   2) Text files to extract aspects

# Parameters:
#   1) --inputPath Path to read input files.
#   2) --transformedPath Path to place output files.
#   3) --textPath Path to place output files.
#   4) --crf Let POS tag instead of substituting it by term or freq tag

# Output:
#   1) transformed files
#   2) text files

# Execution:
# python transforming.py --inputPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\aspectClassificationDatasets\term --transformedPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\aspectClassificationDatasets\transformed --textPath C:\Users\cmendezc\Documents\GENOMICAS\AUTOMATIC_SUMMARIZATION_TFS\corpus\aspectClassificationDatasets\textToExtractAspects

###########################################################
#                       MAIN PROGRAM                      #
###########################################################

if __name__ == "__main__":
    # Parameter definition
    parser = OptionParser()
    parser.add_option("-i", "--inputPath", dest="inputPath",
                      help="Path to read input files", metavar="PATH")
    parser.add_option("-o", "--transformedPath", dest="transformedPath",
                      help="Path to place transformed files", metavar="PATH")
    parser.add_option("--textPath", dest="textPath",
                      help="Path to place text files", metavar="PATH")
    parser.add_option("--crf", default=False,
                      action="store_true", dest="crf",
                      help="Let POS tag instead of substituting it by term or freq tag?")
    parser.add_option("--termPath", dest="termPath",
                      help="Path to read term files", metavar="PATH")
    parser.add_option("--termFiles", dest="termFiles",
                      help="JSON file with terms files and tags", metavar="PATH")

    (options, args) = parser.parse_args()

    if len(args) > 0:
        parser.error("None parameters indicated.")
        sys.exit(1)

    # Printing parameter values
    print('-------------------------------- PARAMETERS --------------------------------')
    print("Path to read input files: " + str(options.inputPath))
    print("Path to place transformed files: " + str(options.transformedPath))
    print("Path to place text files: " + str(options.textPath))
    print("Let POS tag instead of substituting it by term or freq tag? " + str(options.crf))


with open(os.path.join(options.termPath, options.termFiles)) as dicts:
    tags_d = {}
    dicts = dicts.readlines()
    tagset = []
    for line in dicts: 
    	if re.search("\"(?P<son>\w+)\":\s\"(?P<father>\w+)\"", line):
            s = re.search("\"(\w+)\":\s\"(\w+)\"", line).group(1)
            tagset.append(s)

    filesPreprocessed = 0
    t0 = time()
    print("Transforming files...")
    # Walk directory to read files
    for path, dirs, files in os.walk(options.inputPath):
        # For each file in dir
        for file in files:
            print("   Transforming file..." + str(file))
            #TrpR	NN	TrpR NN PennPOS
            # ,	,	, , NUPOS}
            # tryptophan	NN	tryptophan NN PennPOS
            listLine1 = []
            listLine2 = []
            text = ''
            lemma = ''
            pos = ''
            textTransformed = ''
            textText = ''
            with open(os.path.join(path, file), "r", encoding="utf-8", errors="replace") as iFile:
                # Create output file to write
                with open(os.path.join(options.textPath, file.replace('term.txt', 'txt')), "w", encoding="utf-8") as textFile:
                    with open(os.path.join(options.transformedPath, file.replace('term.txt', 'tra.txt')), "w", encoding="utf-8") as transformedFile:
                        for line in iFile:
                            if line == '\n':
                                textFile.write(textText + '\n')
                                transformedFile.write(textTransformed + '\n')
                                textTransformed = ''
                                textText = ''
                            else:
                                line = line.strip('\n')
                                listLine1 = line.split('\t')
                                text = listLine1[0]
                                # Replacing a strange space character
                                text = text.replace(' ', '-')
                                listLine2 = listLine1[2].split(' ')
                                if len(listLine2) < 3:
                                    continue
                                lemma = listLine2[0]
                                # Replacing a strange space character
                                lemma = lemma.replace(' ', '-')
                                if listLine2[2] == "TermTag":
                                    pos = listLine2[1]
                                    #print('Line ' + str(line.encode(encoding='UTF-8', errors='replace')))
                                else:
                                    pos = listLine1[1]
                                textText = textText + text + ' '
                                textTransformed = textTransformed + text + '|' + lemma + '|' + pos + ' '
            filesPreprocessed += 1

    # Imprime archivos procesados
    print()
    print("Files preprocessed: " + str(filesPreprocessed))
    print("In: %fs" % (time() - t0))
