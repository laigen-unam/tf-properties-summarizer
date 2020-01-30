from optparse import OptionParser
import os

parser = OptionParser()
parser.add_option("--path", dest="path",
	help="Input txt path", metavar="PATH")
parser.add_option("--tfList", dest="tfList",
        help="List of transcription factors", metavar="List")
(options, args) = parser.parse_args()

if len(args) > 0:
	parser.error("No parameter was given.")
	sys.exit(1)
TFs = options.tfList.split(',')
for t in TFs:
	with open(os.path.join(options.path,"ACT", t, "summary.txt")) as act:
		act = act.readlines()
	with open(os.path.join(options.path,"DOM", t, "summary.txt")) as dom:
		dom = dom.readlines()
	with open(os.path.join(options.path,"EVO", t, "summary.txt")) as evo:
		evo = evo.readlines()
	with open(os.path.join(options.path,"RP", t, "summary.txt")) as rp:
		rp = rp.readlines()
	with open(os.path.join(options.path,"SIT", t, "summary.txt")) as sit:
		sit = sit.readlines()
	with open(os.path.join(options.path,"TU", t, "summary.txt")) as tu:
		tu = tu.readlines()
	if len(act) != 0 or len(dom) != 0 or len(evo) != 0 or len(rp) != 0 or len(sit) != 0 or len(tu) != 0:
		if not os.path.exists(os.path.join(options.path, "complete", t)):
			os.mkdir(os.path.join(options.path, "complete", t))
		with open(os.path.join(options.path, "complete", t, "summary.txt"), 'a') as sm:
			sentences = {}
			scores = {}
			for line in act:
				line = line.split("\t")
				sentences.setdefault(line[2],[]).append(line[0])
				scores.setdefault(line[2],[]).append(line[3])
			for s in sentences:
				pmids = ",".join(sentences[s])
				sm.write("ACT\t{}\t{}\t{}".format(pmids, s, scores[s][0]))
			sentences = {}
			scores = {}
			for line in dom:
				line = line.split("\t")
				sentences.setdefault(line[2],[]).append(line[0])
				scores.setdefault(line[2],[]).append(line[3])
			for s in sentences:
				pmids = ",".join(sentences[s])
				sm.write("DOM\t{}\t{}\t{}".format(pmids, s, scores[s][0]))
			sentences = {}
			scores = {}
			for line in evo:
				line = line.split("\t")
				sentences.setdefault(line[2],[]).append(line[0])
				scores.setdefault(line[2],[]).append(line[3])
			for s in sentences:
				pmids = ",".join(sentences[s])
				sm.write("EVO\t{}\t{}\t{}".format(pmids, s, scores[s][0]))
			sentences = {}
			scores = {}
			for line in rp:
				line = line.split("\t")
				sentences.setdefault(line[2],[]).append(line[0])
				scores.setdefault(line[2],[]).append(line[3])
			for s in sentences:
				pmids = ",".join(sentences[s])
				sm.write("RP\t{}\t{}\t{}".format(pmids, s, scores[s][0]))
			sentences = {}
			scores = {}
			for line in sit:
				line = line.split("\t")
				sentences.setdefault(line[2],[]).append(line[0])
				scores.setdefault(line[2],[]).append(line[3])
			for s in sentences:
				pmids = ",".join(sentences[s])
				sm.write("SIT\t{}\t{}\t{}".format(pmids, s, scores[s][0]))
			sentences = {}
			scores = {}
			for line in tu:
				line = line.split("\t")
				sentences.setdefault(line[2],[]).append(line[0])
				scores.setdefault(line[2],[]).append(line[3])
			for s in sentences:
				pmids = ",".join(sentences[s])
				sm.write("TU\t{}\t{}\t{}".format(pmids, s, scores[s][0]))
