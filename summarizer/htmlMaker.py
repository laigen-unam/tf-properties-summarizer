from optparse import OptionParser
import os
import re

parser = OptionParser()
parser.add_option("--inputPath", dest="inputPath",
					help="Input txt path", metavar="PATH")
parser.add_option("--htmlPath", dest="htmlPath",
					help="HTML txt path", metavar="PATH")
(options, args) = parser.parse_args()

if len(args) > 0:
	parser.error("No parameter was given.")
	sys.exit(1)

if not os.path.exists(options.htmlPath):
	os.mkdir(options.htmlPath)

for path in os.listdir(options.inputPath):
	with open(os.path.join(options.inputPath, path, "summary.txt")) as iFile, open(os.path.join(options.htmlPath, path + ".summary.html"), 'w') as hFile:
		hFile.write('<!doctype html>\n<style>\n@charset "utf-8";\nbody {{\n\theight: 100%;\n\tmargin: 0;\n\tpadding: 0;\n}}\n\n.banner {{\n\tposition: fixed;\n\ttop: 0;\n\twidth: 100%;\n\theight: 65px;\n\tbackground: gray;\n\tline-height: 65px;\n}}\n.spacer {{\n\theight: 10px;\n}}\n\n.main-content {{\n\tpadding: 5%;\n}}\n\n.collapse_ACT {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\theight: 30px;\n\tline-height: 30px;\n\tborder-style: none solid none none;\n\tborder-color: #B4045F;\n\tborder-width: thick;\n\tbackground: #DCDCDC;\n}}\n.collapse_ACT + input{{\n\tdisplay: none;\n}}\n.collapse_ACT + input + div{{\n\tdisplay: none;\n}}\n.collapse_ACT + input:checked + div{{\n\tdisplay: block;\n}}\n.ACT {{\n\ttext-align: justify;\n\ttext-justify: inter-word;\n}}\n.ACT_collapse_similarity {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\tbackground: white;\n\tborder-style: none none none solid;\n\tborder-color: #B4045F;\n}}\n.ACT_collapse_similarity:hover{{\n\tbackground: #e5d3dc;\n}}\n.ACT_collapse_similarity + input {{\n\tdisplay: none;\n}}\n.ACT_collapse_similarity + input + div{{\n\tdisplay: none;\n}}\n\n.ACT_collapse_similarity + input:checked + div{{\n\tdisplay: block;\n}}\n.ACT_collapse_similarity > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n.ACT_collapse_similarity {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\tbackground: white;\n\tborder-style: none none none solid;\n\tborder-color: #B4045F;\n\tpadding-left: 5px;\n}}\n.ACT_collapse_similarity:hover{{\n\tbackground: #e5d3dc;\n}}\n.ACT_collapse_similarity + input {{\n\tdisplay: none;\n}}\n.ACT_collapse_similarity + input + div{{\n\tdisplay: none;\n}}\n.ACT_collapse_similarity + input:checked + div{{\n\tdisplay: block;\n}}\n.ACT_collapse_similarity > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n.ACT_similar {{\n\tpadding-left: 2%;\n\ttext-align: justify;\n\ttext-justify: inter-word;\n\tborder-style: none none none solid;\n\tborder-color: #B4045F;\n}}\n.ACT_similar > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n\n.collapse_DOM {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\theight: 30px;\n\tline-height: 30px;\n\tborder-style: none solid none none;\n\tborder-color: #B404AE;\n\tborder-width: thick;\n\tbackground: #DCDCDC;\n}}\n.collapse_DOM + input{{\n\tdisplay: none;\n}}\n.collapse_DOM + input + div{{\n\tdisplay: none;\n}}\n.collapse_DOM + input:checked + div{{\n\tdisplay: block;\n}}\n.DOM {{\n\ttext-align: justify;\n\ttext-justify: inter-word;\n}}\n.DOM_collapse_similarity {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\tbackground: white;\n\tborder-style: none none none solid;\n\tborder-color: #B404AE;\n\tpadding-left: 5px;\n}}\n.DOM_collapse_similarity:hover{{\n\tbackground: #e8d7e7;\n}}\n.DOM_collapse_similarity + input {{\n\tdisplay: none;\n}}\n.DOM_collapse_similarity + input + div{{\n\tdisplay: none;\n}}\n.DOM_collapse_similarity + input:checked + div{{\n\tdisplay: block;\n}}\n.DOM_collapse_similarity > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}.DOM_similar {{\n\tpadding-left: 2%;\n\ttext-align: justify;\n\ttext-justify: inter-word;\n\tborder-style: none none none solid;\n\tborder-color: #B404AE;\n}}\n.DOM_similar > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n\n.collapse_EVO {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\theight: 30px;\n\tline-height: 30px;\n\tborder-color: #7401DF;\n\tborder-style: none solid none none;\n\tborder-width: thick;\n\tbackground: #DCDCDC;\n}}\n.collapse_EVO + input{{\n\tdisplay: none;\n}}\n.collapse_EVO + input + div{{\n\tdisplay: none;\n}}\n.collapse_EVO + input:checked + div{{\n\tdisplay: block;\n}}\n.EVO {{\n\ttext-align: justify;\n\ttext-justify: inter-word;\n}}\n.EVO_collapse_similarity {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\tbackground: white;\n\tborder-style: none none none solid;\n\tborder-color: #7401DF;\n\tpadding-left: 5px;\n}}\n.EVO_collapse_similarity:hover{{\n\tbackground: #e2d7ed;\n}}\n.EVO_collapse_similarity + input {{\n\tdisplay: none;\n}}\n.EVO_collapse_similarity + input + div{{\n\tdisplay: none;\n}}\n.EVO_collapse_similarity + input:checked + div{{\n\tdisplay: block;\n}}\n.EVO_collapse_similarity > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n.EVO_similar {{\n\tpadding-left: 2%;\n\ttext-align: justify;\n\ttext-justify: inter-word;\n\tborder-style: none none none solid;\n\tborder-color: #7401DF;\n}}\n.EVO_similar > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n\n.collapse_RP {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\theight: 30px;\n\tline-height: 30px;\n\tborder-color: #0174DF;\n\tborder-style: none solid none none;\n\tborder-width: thick;\n\tbackground: #DCDCDC;\n}}\n.collapse_RP + input{{\n\tdisplay: none;\n}}\n.collapse_RP + input + div{{\n\tdisplay: none;\n}}\n.collapse_RP + input:checked + div{{\n\tdisplay: block;\n}}\n.RP {{\n\ttext-align: justify;\n\ttext-justify: inter-word;\n}}\n.RP_collapse_similarity {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\tbackground: white;\n\tborder-style: none none none solid;\n\tborder-color: #0174DF;\n\tpadding-left: 5px;\n}}\n.RP_collapse_similarity:hover{{\n\tbackground: #c9d7e2;\n}}\n.RP_collapse_similarity + input {{\n\tdisplay: none;\n}}\n.RP_collapse_similarity + input + div{{\n\tdisplay: none;\n}}\n.RP_collapse_similarity + input:checked + div{{\n\tdisplay: block;\n}}\n.RP_collapse_similarity > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n.RP_similar {{\n\tpadding-left: 2%;\n\ttext-align: justify;\n\ttext-justify: inter-word;\n\tborder-style: none none none solid;\n\tborder-color: #0174DF;\n}}\n.RP_similar > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n\n.collapse_SIT {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\theight: 30px;\n\tline-height: 30px;\n\tborder-color: #0489B1;\n\tborder-style: none solid none none;\n\tborder-width: thick;\n\tbackground: #DCDCDC;\n}}\n.collapse_SIT + input{{\n\tdisplay: none;\n}}\n.collapse_SIT + input + div{{\n\tdisplay: none;\n}}\n.collapse_SIT + input:checked + div{{\n\tdisplay: block;\n}}\n.SIT {{\n\ttext-align: justify;\n\ttext-justify: inter-word;\n}}\n.SIT_collapse_similarity {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\tbackground: white;\n\tborder-style: none none none solid;\n\tborder-color: #0489B1;\n\tpadding-left: 5px;\n}}\n.SIT_collapse_similarity:hover{{\n\tbackground: #d0dfe2;\n}}\n.SIT_collapse_similarity + input {{\n\tdisplay: none;\n}}\n.SIT_collapse_similarity + input + div{{\n\tdisplay: none;\n}}\n.SIT_collapse_similarity + input:checked + div{{\n\tdisplay: block;\n}}\n.SIT_collapse_similarity > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n.SIT_similar {{\n\tpadding-left: 2%;\n\ttext-align: justify;\n\ttext-justify: inter-word;\n\tborder-style: none none none solid;\n\tborder-color: #0489B1;\n}}\n.SIT_similar > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n\n.collapse_TU {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\theight: 30px;\n\tline-height: 30px;\n\tborder-color: #04B486;\n\tborder-style: none solid none none;\n\tborder-width: thick;\n\tbackground: #DCDCDC;\n}}\n.collapse_TU + input{{\n\tdisplay: none;\n}}\n.collapse_TU + input + div{{\n\tdisplay: none;\n}}\n.collapse_TU + input:checked + div{{\n\tdisplay: block;\n}}\n.TU {{\n\ttext-align: justify;\n\ttext-justify: inter-word;\n}}\n.TU_collapse_similarity {{\n\tcursor: pointer;\n\tdisplay: block;\n\tcolor: black;\n\tbackground: white;\n\tborder-style: none none none solid;\n\tborder-color: #04B486;\n\tpadding-left: 5px;\n}}\n.TU_collapse_similarity:hover{{\n\tbackground: #d0e2de;\n}}\n.TU_collapse_similarity + input {{\n\tdisplay: none;\n}}\n.TU_collapse_similarity + input + div{{\n\tdisplay: none;\n}}\n.TU_collapse_similarity + input:checked + div{{\n\tdisplay: block;\n}}\n.TU_collapse_similarity > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n.TU_similar {{\n\tpadding-left: 2%;\n\ttext-align: justify;\n\ttext-justify: inter-word;\n\tborder-style: none none none solid;\n\tborder-color: #04B486;\n}}\n.TU_similar > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\n\nul {{ \n\tlist-style-type: none;\n\tpadding: 0;\n\tmargin: 0;\n}}\nul li > a {{\n\ttext-decoration: none;\n\tcolor: gray;\n}}\nul li:hover, ul li:focus {{\n\tbackground: #F0F0F0;\n}}\n\nul li:first-child span {{\n  border-left:none;  \n}}\n\n</style>\n<html>\n<head>\n<meta charset="utf-8">\n<title>TF properties - {}</title>\n<meta name="theme-color" content="#ffffff">\n</head>\n<body>\n\t<div class="banner">\n\t\t<center><font color="white" size="16px" face="arial">{}</font></center>\n\t</div>\n\t<div align="center" class="main-content">\n\t\t<div class="spacer">\n\t</div><br>'.format(path, path))
		iFile = iFile.readlines()
		s = []
		for line in iFile:
			sline = line.split("\t")
			if sline[0] == "ACT":
				s.append(line)
		if len(s) > 0:
			hFile.write('\t\t\t<label class="collapse_ACT" for="_1"><font size="5px">{} transcriptional activity</font></label>\n\t\t\t\t<input id="_1" type="checkbox">\n\t\t\t\t<div class="ACT"><br><ul>'.format(path))
			c = 0
			b = False
			for line in s[:-1]:
				c += 1
				pmidlinks = []
				line = line.split("\t")
				next_line = s[c]
				next_line = next_line.split("\t")
				if float(next_line[3]) < 0.8 and not b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) >= 0.8 and not b:
					hFile.write('\t\t\t\t<label class="ACT_collapse_similarity" for="act_similarity_{}">\n'.format(c))
					hFile.write('{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></label>\n")
					hFile.write('<input id="act_similarity_{}", type="checkbox">\n<div class="ACT_similar">\n'.format(c))
					b = True
				elif float(next_line[3]) >= 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) < 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li></div>\n")
					b = False
			if b:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li></div>\n")
			else:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li>\n")
			hFile.write('\t\t\t\t</div></ul><br>\n')
		s = []
		for line in iFile:
			sline = line.split("\t")
			if sline[0] == "DOM":
				s.append(line)
		if len(s) > 0:
			hFile.write('\t\t\t<label class="collapse_DOM" for="_2"><font size="5px">{} protein domains</font></label>\n\t\t\t\t<input id="_2" type="checkbox">\n\t\t\t\t<div class="DOM"><br><ul>'.format(path))
			c = 0
			b = False
			for line in s[:-1]:
				c += 1
				pmidlinks = []
				line = line.split("\t")
				next_line = s[c]
				next_line = next_line.split("\t")
				if float(next_line[3]) < 0.8 and not b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) >= 0.8 and not b:
					hFile.write('\t\t\t\t<label class="DOM_collapse_similarity" for="dom_similarity_{}">\n'.format(c))
					hFile.write('{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></label>\n")
					hFile.write('<input id="dom_similarity_{}", type="checkbox">\n<div class="DOM_similar">\n'.format(c))
					b = True
				elif float(next_line[3]) >= 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) < 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li></div>\n")
					b = False
			if b:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li></div>\n")
			else:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li>\n")
			hFile.write('\t\t\t\t</div></ul><br>\n')
		s = []
		for line in iFile:
			sline = line.split("\t")
			if sline[0] == "EVO":
				s.append(line)
		if len(s) > 0:
			hFile.write('\t\t\t<label class="collapse_EVO" for="_3"><font size="5px">{} evolution</font></label>\n\t\t\t\t<input id="_3" type="checkbox">\n\t\t\t\t<div class="EVO"><br><ul>'.format(path))
			c = 0
			b = False
			for line in s[:-1]:
				c += 1
				pmidlinks = []
				line = line.split("\t")
				next_line = s[c]
				next_line = next_line.split("\t")
				if float(next_line[3]) < 0.8 and not b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) >= 0.8 and not b:
					hFile.write('\t\t\t\t<label class="EVO_collapse_similarity" for="evo_similarity_{}">\n'.format(c))
					hFile.write('{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></label>\n")
					hFile.write('<input id="evo_similarity_{}", type="checkbox">\n<div class="EVO_similar">\n'.format(c))
					b = True
				elif float(next_line[3]) >= 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) < 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li></div>\n")
					b = False
			if b:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li></div>\n")
			else:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li>\n")
			hFile.write('\t\t\t\t</div></ul><br>\n')
		s = []
		for line in iFile:
			sline = line.split("\t")
			if sline[0] == "RP":
				s.append(line)
		if len(s) > 0:
			hFile.write('\t\t\t<label class="collapse_RP" for="_4"><font size="5px">Processes regulated by {}</font></label>\n\t\t\t\t<input id="_4" type="checkbox">\n\t\t\t\t<div class="RP"><br><ul>'.format(path))
			c = 0
			b = False
			for line in s[:-1]:
				c += 1
				pmidlinks = []
				line = line.split("\t")
				next_line = s[c]
				next_line = next_line.split("\t")
				if float(next_line[3]) < 0.8 and not b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) >= 0.8 and not b:
					hFile.write('\t\t\t\t<label class="RP_collapse_similarity" for="rp_similarity_{}">\n'.format(c))
					hFile.write('{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></label>\n")
					hFile.write('<input id="rp_similarity_{}", type="checkbox">\n<div class="RP_similar">\n'.format(c))
					b = True
				elif float(next_line[3]) >= 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) < 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li></div>\n")
					b = False
			if b:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li></div>\n")
			else:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li>\n")
			hFile.write('\t\t\t\t</div></ul><br>\n')
		s = []
		for line in iFile:
			sline = line.split("\t")
			if sline[0] == "SIT":
				s.append(line)
		if len(s) > 0:
			hFile.write('\t\t\t<label class="collapse_SIT" for="_5"><font size="5px">{} binding site</font></label>\n\t\t\t\t<input id="_5" type="checkbox">\n\t\t\t\t<div class="SIT"><br><ul>'.format(path))
			c = 0
			b = False
			for line in s[:-1]:
				c += 1
				pmidlinks = []
				line = line.split("\t")
				next_line = s[c]
				next_line = next_line.split("\t")
				if float(next_line[3]) < 0.8 and not b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) >= 0.8 and not b:
					hFile.write('\t\t\t\t<label class="SIT_collapse_similarity" for="sit_similarity_{}">\n'.format(c))
					hFile.write('{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></label>\n")
					hFile.write('<input id="sit_similarity_{}", type="checkbox">\n<div class="SIT_similar">\n'.format(c))
					b = True
				elif float(next_line[3]) >= 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) < 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li></div>\n")
					b = False
			if b:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li></div>\n")
			else:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li>\n")
			hFile.write('\t\t\t\t</ul></div><br>\n')
		s = []
		for line in iFile:
			sline = line.split("\t")
			if sline[0] == "TU":
				s.append(line)
		if len(s) > 0:
			hFile.write('\t\t\t<label class="collapse_TU" for="_6"><font size="5px">Transcription units regulated by {}</font></label>\n\t\t\t\t<input id="_6" type="checkbox">\n\t\t\t\t<div class="TU"><br><ul>'.format(path))
			c = 0
			b = False
			for line in s[:-1]:
				c += 1
				pmidlinks = []
				line = line.split("\t")
				next_line = s[c]
				next_line = next_line.split("\t")
				if float(next_line[3]) < 0.8 and not b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) >= 0.8 and not b:
					hFile.write('\t\t\t\t<label class="TU_collapse_similarity" for="tu_similarity_{}">\n'.format(c))
					hFile.write('{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></label>\n")
					hFile.write('<input id="tu_similarity_{}", type="checkbox">\n<div class="TU_similar">\n'.format(c))
					b = True
				elif float(next_line[3]) >= 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li>\n")
				elif float(next_line[3]) < 0.8 and b:
					hFile.write('<li>{}\t['.format(line[2]))
					pmids = line[1].split(",")
					for p in pmids:
						pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
					hFile.write(", ".join(pmidlinks))
					hFile.write("]<br></li></div>\n")
					b = False
			if b:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li></div>\n")
			else:
				line = s[-1]
				line = line.split("\t")
				hFile.write('<li>{}\t['.format(line[2]))
				pmids = line[1].split(",")
				pmidlinks = []
				for p in pmids:
					pmidlinks.append('<a href="https://www.ncbi.nlm.nih.gov/pubmed/?term={}" target="_blank">{}</a>'.format(p,p))
				hFile.write(", ".join(pmidlinks))
				hFile.write("]<br></li>\n")
			hFile.write('\t\t\t\t</div></ul></div><br>\n')
		hFile.write('\t</div>\n</body>\n</html>')

