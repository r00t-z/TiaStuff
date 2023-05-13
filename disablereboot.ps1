$sessionManagerKeyPath = "HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager"
$runOnceKeyPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"
$propertyName = "PendingFileRenameOperations"

while ($true) {
    Write-Host "`nMenu Options:"
    Write-Host "1. Check if you can Install Siemens Software" -ForegroundColor Cyan
    Write-Host "2. Enable Siemens Software Install without Rebooting" -ForegroundColor Cyan
    Write-Host "3. Exit" -ForegroundColor Cyan

    $choice = Read-Host "Enter your choice (1-3)"

    switch ($choice) {
        1 {
            # Check Session Manager key
            if (Test-Path -Path $sessionManagerKeyPath) {
                $sessionManagerPropertyValue = Get-ItemProperty -Path $sessionManagerKeyPath -Name $propertyName -ErrorAction SilentlyContinue

                if ($sessionManagerPropertyValue) {
                    Write-Host "You need to reboot or use option 2" -ForegroundColor Red
                } else {
                    Write-Host "You can Install Siemens Software without reboot" -ForegroundColor Green
                }
            } else {
                Write-Host "You need to reboot or use option 2" -ForegroundColor Red
            }
        }
        2 {
            # Remove Session Manager property
            if (Test-Path -Path $sessionManagerKeyPath) {
                Remove-ItemProperty -Path $sessionManagerKeyPath -Name $propertyName -ErrorAction SilentlyContinue
            }

            # Remove RunOnce key
            if (Test-Path -Path $runOnceKeyPath) {
                Remove-Item -Path $runOnceKeyPath -Recurse -ErrorAction SilentlyContinue
            }

            Write-Host "All Done!" -ForegroundColor Green
        }
        3 {
            break
        }
        default {
            Write-Host "Invalid choice. Please select a valid option." -ForegroundColor Red
        }
    }

    if ($choice -eq "3") {
        Write-Host "Exiting..." -ForegroundColor Red
        break
    }
}
