Set-PSReadlineOption -HistorySaveStyle SaveNothing
$env:PYTHONIOENCODING="utf-8"


function ActivateIcu {
    $env:OLDPWD = $PWD.Path  # Store the current location in $OLDPWD
    $envPath = "D:\\eyeseeu\Scripts"
    Set-Location $envPath
    .\activate
    Set-Location $oldLocation
    Remove-Variable oldLocation
    Remove-Variable envPath

}
Set-Alias -Name icu -Value ActivateIcu

function ActivateOro {
    $oldLocation = $PWD.Path  # Store the current location
    $envPath = "D:\\oracle\Scripts"
    Set-Location $envPath
    .\activate
    Set-Location $oldLocation
    Remove-Variable oldLocation
    Remove-Variable envPath
}
Set-Alias -Name oro -Value ActivateOro

function Activategcp {
    $oldLocation = $PWD.Path
    $envPath = "D:\Murmur\gcpcx\Scripts"
    Set-Location $envPath
    .\activate
    Set-Location $oldLocation
    Remove-Variable oldLocation
    Remove-Variable envPath
}
Set-Alias -Name gcp -Value Activategcp



function DailyQuote {
    $pythonScriptPath = "D:\\sql_querry.py"
    $output = python $pythonScriptPath
    $output
}
Set-Alias -Name quo1 -Value DailyQuote 
