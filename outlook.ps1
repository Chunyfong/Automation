# Create an Outlook instance
$outlook = New-Object -ComObject Outlook.Application
$namespace = $outlook.GetNamespace("MAPI")

# Access the Inbox
$inbox = $namespace.GetDefaultFolder(6)
$targetfolder = $inbox.Folders | Where-Object {$_.Name -eq "Damon_Automation"}

# Loop through each mail item in the folder
foreach ($mail in $targetfolder.Items)
{
    Write-Host ("Email Title: " + $mail.Subject)
    Write-Host ("Received Time: " + $mail.ReceivedTime)
    Write-Host ("Sender: " + $mail.SenderName)
    Write-Host ("Attachments Count: " + $mail.Attachments.count)
    # Loop through each attachment and print its name
    foreach ($attachment in $mail.Attachments)
    {
        Write-Host ("Attachment Name: " + $attachment.FileName)
    }
    Write-Host ("----------------------------------")
}
