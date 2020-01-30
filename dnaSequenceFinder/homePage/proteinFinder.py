from searchHistory.models import Search
def findProtein(sequence):
	file = open("homePage/proteinList.txt","r");
	proteinList = file.readlines();

	for protein in proteinList:
		if sequence in protein:
			index = protein.index(sequence);
			seq = Search(
				sequence=sequence,
				proteinName=protein.strip(),
				proteinIndex=index,
			)
			return seq;
	seq = Search(
		sequence=sequence,
		proteinName="None found.",
		proteinIndex=-1,
	)
	return seq;