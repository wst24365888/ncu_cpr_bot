conda install selenium

$source = 'https://chromedriver.storage.googleapis.com/93.0.4577.63/chromedriver_win32.zip'
$filePath = './chromedriver.zip'
Invoke-WebRequest -Uri $source -OutFile $filePath

Expand-Archive -Path $filePath -DestinationPath './'

Remove-Item $filePath