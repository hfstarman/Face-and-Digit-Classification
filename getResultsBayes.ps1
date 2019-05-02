"foo" >> naiveBayesResults.txt
rm naiveBayesResults.txt

$faceArray = 45,90,135,180,225,270,315,360,405,451
$digitArray = 500,1000,1500,2000,2500,3000,3500,4000,4500,5000

$start_faces = Get-Date

foreach ($amount in $faceArray) 
{
    "Running Faces: " + $amount
    python dataClassifier.py -c naiveBayes -d faces -t $amount -s 150 >> naiveBayesResults.txt
}

$end_faces = Get-Date
$start_digits = Get-Date

foreach ($amount in $digitArray) 
{
    "Running Digits: " + $amount
    python dataClassifier.py -c naiveBayes -d digits -t $amount -s 1000 -k .001 >> naiveBayesResults.txt
}

$end_digits = Get-Date

Write-host (New-TimeSpan -Start $start_faces -End $end_faces).TotalSeconds "seconds (faces)"
Write-host (New-TimeSpan -Start $start_digits -End $end_digits).TotalSeconds "seconds (digits)"