import os
import re

dirname = 'C:/data/jenkins_home/jobs/Selenium_Jenkins_GitHub/builds/'
files = os.listdir(dirname)
folder_number = re.findall('[0-9]+', str(files))
max_folder_number = max(folder_number)
f_read = open(f'C:/data/jenkins_home/jobs/Selenium_Jenkins_GitHub/builds/{max_folder_number}/log', 'r')
text = f_read.read()
f_read.close()
pass_txt = 'PASSED'
test_start_txt = 'TEST START'
count_pass_txt = text.count(pass_txt)
count_test_start_txt = text.count(test_start_txt)
if count_test_start_txt > count_pass_txt:
    os.system('curl -s -X POST https://api.telegram.org/bot5698947661:AAFmFW1PEUa7STMd6yXq9x91tJ2oyavqKAE/sendMessage -d chat_id=-746480341 -d text="Selenium_Jenkins_GitHub Build %BUILD_NUMBER% finish with FAILURE"')
elif count_test_start_txt == count_pass_txt:
    os.system('curl -s -X POST https://api.telegram.org/bot5698947661:AAFmFW1PEUa7STMd6yXq9x91tJ2oyavqKAE/sendMessage -d chat_id=-746480341 -d text="Selenium_Jenkins_GitHub Build %BUILD_NUMBER% finish with SUCCESS"')
else:
    print('ERROR')
    
    
