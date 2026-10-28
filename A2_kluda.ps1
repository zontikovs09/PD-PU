Get-Service | Select-Object -Property Name,Status,StartType | Where-Object {$_.Status -eq "Running" -and $_.StartType -eq "Automatic"}
