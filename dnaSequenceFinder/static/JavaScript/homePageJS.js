
function addSequence(sequence){
	document.getElementById("sequenceList").innerHTML=(document.getElementById("sequenceList").innerHTML + sequence);
	console.log("here");
}

function getFormData(seqName,proteinName,proteinIndex){

     let fullSeqName=seqName + ", " + proteinName + ", " + proteinIndex + "<br>";
     if (proteinIndex==-1)fullSeqName=seqName + ", " + proteinName+ "<br>";
     var savedSequence = "seqName";
     if (localStorage.getItem("sequences")==null){
         localStorage.setItem("sequences", fullSeqName);
         }
     else
         localStorage.setItem("sequences", localStorage.getItem("sequences")+fullSeqName);
}