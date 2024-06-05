# Read the values from the file
$inputValues = Get-Content -Path "input_values.txt"

# Extract the values
$email = $inputValues[0].Split(": ")[1]
$filePath = $inputValues[1].Split(": ")[1]
$number = $inputValues[2].Split(": ")[1]

# Use the values in your PowerShell script
Write-Host "Email: $email"
Write-Host "File Path: $filePath"
Write-Host "Number: $number"

