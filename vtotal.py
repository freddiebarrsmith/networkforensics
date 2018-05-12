
#fuck these guys  and their piece of shit api, it doesn't even work with the sample code they've given on the site, morons

import requests
#hash = "bork"
#need to modify this piece of shit code to take parameters
params = {'apikey': '6578e4386c6d850f55cbeaefd9f29fcf580f313378c794eca07bda6ec94596a8', 'hash': '44cda81782dc2a346abd7b2285530c5f'}
response = requests.get('https://www.virustotal.com/vtapi/v2/file/download', params=params)
print(response)
#downloaded_file = response.content
#file = open(hash, "w+")
#file.write(downloaded_file)
#file.close()
