import glob
import os
import pandas as pd
#from myPyPDF import PdfFileWriter
#from myPyPDF import PdfFileMerger
#from myPyPDF import PdfFileReader
from pikepdf import Pdf
from docx2pdf import convert
df = pd.read_csv("./student_list_grade.csv")
worst_value = 100 # change if larger is better
print(list(df["ranking"])[2])

df["ranking"] = df["ranking"].fillna(worst_value)
df["ranking"] = df["ranking"].replace(to_replace ="nan",
				 value =worst_value)
strong_baseline = 0
df.to_csv("./student_list_grade_out.csv",index = False)
rank = []
for ID, pass_strong, ranking in zip(df["ID"],df["strong"],df["ranking"]):
	if pass_strong == 1:
		rank.append((ranking, ID))
rank = sorted(rank)
#print(rank,len(rank))
id2submission = {}
id2name = {}
submissions = os.listdir("unzipped_submissions")
for s in submissions:
	ID  = s.split("_")[1]
	id2submission[ID] = s
for name_, id_  in zip(df["Student"],df["ID"]):
	name_ = "".join(name_.split("(")[0].strip().split(" "))
	id_ = str(id_)
	id2name[id_] = name_

import subprocess

def doc2pdf_linux(doc):
	"""
	convert a doc/docx document to pdf format (linux only, requires libreoffice)
	:param doc: path to document
	"""
	cmd = 'libreoffice --convert-to pdf'.split() + [doc] + '--outdir'.split() + [".".join(doc.split(".")[:-1]+["pdf"])]
	p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
	p.wait(timeout=10)
	stdout, stderr = p.communicate()
	if stderr:
		raise subprocess.SubprocessError(stderr)


#strong_reports = PdfFileMerger(strict=False)
#pdfWriter = PdfFileWriter()
strong_reports = Pdf.new()
report = []
no_report = []
cur = 0
for n,(score, ID) in enumerate(rank):
	ID = str(ID)
	gotten = False
	if ID in id2submission:
		sub = id2submission[ID].split("_")[:2]
		sub[0] = sub[0][:len(id2name[ID])]
		out_dir_name = f'{str(n+1).zfill(4)}_{"_".join(sub)}'+".zip"
		cmd = f'cp -R {os.path.join("./submissions",id2submission[ID])} {os.path.join("./strong_submissions",out_dir_name)}'.split()
		p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
		p.wait(timeout=10)
		#s()
		for r,d,fs in os.walk(os.path.join("unzipped_submissions",id2submission[ID])):
			for f in fs:
				if (f.endswith(".doc") or f.endswith(".docx") or f.endswith(".odt")or f.endswith(".rft")) and not f.startswith(".") and not f.startswith("~"):
					f_with_dir = os.path.join(r, f)
					doc2pdf_linux(f_with_dir)
					print(f_with_dir)
		
		
		for r,d,fs in os.walk(os.path.join("unzipped_submissions",id2submission[ID])):
			for f in fs:
				if (f.endswith(".pdf")) and not f.startswith("."):
					#report.append(os.path.join(r, f))
					f_with_dir = os.path.join(r, f)
					print("found pdf",f_with_dir)
					# try:
					# 	test_reports.append(f_with_dir)
					# 	test_reports.write("test.pdf")
					# except:
					# 	print("Decode Error",f_with_dir)
						#continue
					#with open(f_with_dir,'rb') as pdf:
					#strong_reports.append(PdfFileReader(pdf))
					#strong_reports.append(f_with_dir)
					strong_reports.pages.extend(Pdf.open(f_with_dir).pages)
					
					gotten = True
					cur += 1
					break
					#print(report)
					#s()
					#break
			if gotten:
				break
	if not gotten:
		no_report.append(ID)
	else:
		report.append(ID)
strong_reports.save("strong.pdf")
print("strong and submitted",len(rank))
print("no report",len(no_report),no_report)
print("with report",len(report),report)
