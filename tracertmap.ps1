# Ask for user input
$target = Read-Host "Enter the domain or IPv4 to trace: "

# Define output file
$outputFile = "trace.txt"

# Start tracert process
Write-Host "Running tracemap on $target..."
$process = Start-Process tracert -ArgumentList "-4 -d $target" -NoNewWindow -PassThru -RedirectStandardOutput $outputFile

# Display a loading bar while tracert runs
$counter = 0
$maxLength = 5
while (!$process.HasExited) {
    $current = $counter % ($maxLength + 1)
    $loadBar = "." * $current
    $padding = " " * ($maxLength - $current)
    Write-Host "`rCollecting Traces$loadBar$padding" -NoNewline
    Start-Sleep -Milliseconds 500
    $counter++
}

# Ensure the process is done
Write-Host "`nTrace complete. Output saved to $outputFile"

# Run Python script
Write-Host "Running tracemap.py..."
Start-Process python -ArgumentList "tracertmap.py" -NoNewWindow -Wait
