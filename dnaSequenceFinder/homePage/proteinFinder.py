import glob, os


from searchHistory.models import Search
def findProtein(sequence):
	sequence=sequence.replace(" ","");
	sequence=sequence.upper()
	proteinDirectory = "homePage/Proteins/"
	for file in glob.glob(proteinDirectory+"*.txt"):
		infile=open(file,"r");
		protein =("".join(infile.readlines())).replace("\\n","").replace('\n', '')
		#print("seq is ",sequence,"protein is ",protein[0:100])
		if sequence in protein:
			print("yes")
			index = protein.index(sequence);
			proteinName=infile.name
			lastSlashIndex=proteinName.rindex("\\")
			proteinName=proteinName[lastSlashIndex+1:len(proteinName)-4] #cutout opening path and .txt
			seq = Search(
				sequence=sequence,
				proteinName=proteinName,
				proteinIndex=index,
			)
			#print("seq is ",sequence, "name is ",proteinName,"index is ",index)
			return seq;
	print("not found")
	seq = Search(
		sequence=sequence,
		proteinName="None found.",
		proteinIndex=-1,
	)
	return seq;