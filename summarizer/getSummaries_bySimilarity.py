from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
import seaborn as sns
import os
from optparse import OptionParser
import matplotlib.pyplot as plt

parser = OptionParser()
parser.add_option("--classifiedPath", dest="classifiedPath",
        help="Path to read classified files", metavar="PATH")
parser.add_option("--wordPath", dest="wordPath",
        help="Path to read word files", metavar="PATH")
parser.add_option("--sumPath", dest="sumPath",
        help="Path to place summary files", metavar="PATH")
parser.add_option("--feature", dest="feature",
        help="Feature used in the classifier model", metavar="Feature")
parser.add_option("--tfList", dest="tfList",
        help="List of transcription factors", metavar="List")
parser.add_option("--removeStopWords", default=False,
                  action="store_true", dest="removeStopWords",
                  help="Eliminate stop words")
parser.add_option("--binary", default=False,
                  action="store_true", dest="binary",
                  help="binary?")
parser.add_option("--similarity", dest="similarity",

                  help="Similarity threshold", metavar="N.N", default=1.0)

(options, args) = parser.parse_args()
if len(args) > 0:
        parser.error("None parameters indicated.")
        sys.exit(1)

TFs = options.tfList.split(',')

stop_words = stopwords.words('english') + ['.', ',', ';', ':', '(', ')', '[', ']', '{', '}', "'", '+', '>', '<', '-']

if not os.path.exists(options.sumPath):
        os.mkdir(options.sumPath)
for t in TFs:
        threshold = float(options.similarity)
        listLabels = []
        listSentences = []
        if not os.path.exists(os.path.join(options.sumPath, t)):
                os.mkdir(os.path.join(options.sumPath, t)
        if os.path.exists(os.path.join(options.classifiedPath, t)):
                print("g")
                with open(os.path.join(options.classifiedPath, t, options.feature + ".classified.txt")) as cFile, open(os.path.join(options.wordPath, t, t + "_concatenated.word.txt")) as wFile:
                        cFile = cFile.readlines()
                        wFile = wFile.readlines()
                        for line in cFile[1:]:
                                line = line.split("\t")
                                pclass = line[3]
                                pclass = pclass.strip("\n")
                                if pclass != "OTHER":
                                        for wline in wFile:
                                                wsline = wline.split("\t")
                                                if line[0] == wsline[0] and line[1] == wsline[1] and wline[2] not in listSentences:
                                                        listLabels.append(wsline[0] + '\t' + wsline[1])
                                                        listSentences.append(wsline[2].strip("\n"))

                if len(listSentences) == 1:
                    with open(os.path.join(options.sumPath, t, "summary.txt"), 'w', encoding="utf-8") as sFile:
                        sFile.write('{}\t{}\t0\n'.format(listLabels[0], listSentences[0]))
                elif len(listSentences) == 0:
                    with open(os.path.join(options.sumPath, t, "summary.txt"), 'w', encoding="utf-8") as sFile:
                        continue
                else:
                    # COSINE SIMILARITY AMONG SENTENCES
                    print("Vectorizing sentences...")
                    if options.removeStopWords:
                        #vectorizer = TfidfVectorizer(lowercase=False, binary=options.binary, stop_words=stop_words)
                        vectorizer = CountVectorizer(lowercase=False, binary=options.binary, stop_words=stop_words)
                    else:
                        #vectorizer = TfidfVectorizer(lowercase=False, binary=options.binary)
                        vectorizer = CountVectorizer(lowercase=False, binary=options.binary)
                    matrix = vectorizer.fit_transform(listSentences)
                    print('   Matrix size:{}'.format(matrix.shape))
                    # SIMILARITY
                    print("Calculating cosine similarity...")
                    similarityMatrix = cosine_similarity(matrix)
                    print("   similarityMatrix shape: {}".format(similarityMatrix.shape))
                    # CLUSTERING
                    print("Clustering...")
                    df = pd.DataFrame(similarityMatrix, index=listLabels, columns=listLabels)
                    result = sns.clustermap(df, linewidths=.5,
                                   figsize=(25, 25), cmap=plt.cm.Reds, metric="cosine")
                    with open(os.path.join(options.sumPath, t, "summary.txt"), 'w', encoding="utf-8") as sFile:
                        idx_before = -1
			for idx in result.dendrogram_row.reordered_ind:
			    if idx_before == -1:
			        sFile.write('{}\t{}\t{}\n'.format(listLabels[idx], listSentences[idx], 0))
			    else:
			        similarity = similarityMatrix[idx][idx_before]
			        if similarity <= threshold:
			            sFile.write('{}\t{}\t{}\n'.format(listLabels[idx], listSentences[idx], similarity))
			        else:
			            sFile.write('{}\t{}\t{}\n'.format(listLabels[idx], listSentences[idx], similarity))
			    idx_before = idx

