import os
import re

dirname = 'C:/data/jenkins_home/jobs/Selenium_Jenkins_GitHub/builds/'
files = os.listdir(dirname)
folder_number = re.findall('[0-9]+', str(files))
f_read = open(f'C:/data/jenkins_home/jobs/Selenium_Jenkins_GitHub/builds/{max(folder_number)}/log', 'r')
last_line = f_read.readlines()[-1]
if 'SUCCESS' in last_line:
    os.system('curl -s -X POST https://api.telegram.org/bot5698947661:AAFmFW1PEUa7STMd6yXq9x91tJ2oyavqKAE/sendMessage -d chat_id=-746480341 -d text="Finish with SUCCESS"')
else:
    os.system('curl -s -X POST https://api.telegram.org/bot5698947661:AAFmFW1PEUa7STMd6yXq9x91tJ2oyavqKAE/sendMessage -d chat_id=-746480341 -d text="Finish with FAILURE"')

