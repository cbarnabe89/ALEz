//function computeNLE(){
//    var normalHousing = document.getElementById('normal_housing').value;
//    var normalUtilitiesHeat = document.getElementById('normal_utilities_heat').value;
//    var additionNLE = (parseFloat(normalHousing) + parseFloat(normalUtilitiesHeat)).toFixed(2);
//    document.getElementById('total_NLE').value = additionNLE;
//}

//Example code listed above as I was experimenting with creating the calculator function for the app

//****************************************************************************/
//Create PDF Function
async function generatePDF(){
    document.getElementById("downloadButton").innerHTML = "Currently Downloading Your PDF";
    
    //Downloading
    var downloading = document.getElementById("whatToPrint");
    var doc = new jsPDF('l', 'pt', 'a4' );

    await html2canvas(downloading, {
        width: 1450
        }).then((canvas) => {
            doc.addImage(canvas.toDataURL('image/png'), 'PNG', 5, 5, 930, 230);
        })
        doc.save("ale-worksheet.pdf");
    //End of Downloading

    document.getElementById("downloadButton").innerHTML = "Click to Download";
    }


//****************************************************************************/

//Create the variable to collect elements by class name for NLE
var nleItems = document.getElementsByClassName('nle')
//Create variable to hold the sum of NLE
var sumNle = 0;

//Create Function for NLE computation on screen
function computeNLE(){
sumNle = 0
for (i= 0; i < nleItems.length; i++){
    sumNle += parseFloat(nleItems[i].value);
    console.log(nleItems[i].value);
    console.log(sumNle);
    }
    document.getElementById('total_NLE').value = sumNle.toFixed(2);
}


//Create the variable to collect elements by class name for ALE
var aeItems = document.getElementsByClassName('ae')
//Create the variable to hold the sum of ALE
var sumAe = 0

//Create Function for AE computation on screen
function computeAE(){
    sumAe = 0
    for (i= 0; i < aeItems.length; i++){
        sumAe += parseFloat(aeItems[i].value);
        console.log(aeItems[i].value);
        console.log(sumAe);
        }
        document.getElementById('total_AE').value = sumAe.toFixed(2)
        return computeAE
    }


//****************************************************************************/

//Create Variables of the totals
var totalAe = document.getElementById('total_AE').value;
var totalNle = document.getElementById('total_NLE').value;

//Create a function to compute the total ALE claim

function computeALE(){
    var totalAe = document.getElementById('total_AE').value;
    var totalNle = document.getElementById('total_NLE').value;
    var totalALE = (parseFloat(totalAe) - parseFloat(totalNle)).toFixed(2);
    document.getElementById('total_ALE_claim').value = totalALE;
}

//*****************************************************************************/

