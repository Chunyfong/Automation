# Create an instance of Outlook.Application
$outlook = New-Object -ComObject Outlook.Application

# Get the namespace
$namespace = $outlook.GetNamespace("MAPI")

# Specify the folder you want to access (Inbox in this case)
$inbox = $namespace.GetDefaultFolder(6)
#set the target folder
$folder = $inbox.Folders.Item(" ")

# Loop through each item in the folder
foreach ($item in $folder.Items) {
    # Check if the email has attachments
    if ($item.Attachments.Count -gt 0) {
        # Loop through each attachment
        foreach ($attachment in $item.Attachments) {
            # Check if the attachment is a pdf, 
            if ($attachment.FileName -like "*.pdf" -or $attachment.FileName -like "*.PDF") {
                # Output the email details and attachment path
                Write-Output "$($item.Subject),$($item.ReceivedTime),$($attachment.FileName)"

                # Save the attachment, your path
                $attachment.SaveAsFile("  $($attachment.FileName)")
            }
        }
    }
}
