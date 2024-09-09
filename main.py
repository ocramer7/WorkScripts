import subprocess
import sys
import webbrowser
from tkinter import messagebox


print(webbrowser._browsers) # List available browser
print("OS Platform:", sys.platform)
urls = ['https://mail.google.com', 'https://support.sdsmt.edu/TDNext/Home/Desktop/Default.aspx',
        'https://support.sdsmt.edu/TDClient/30/Portal/Home/?ToUrl=',
        'https://ngsp.lenovo.com/dashboard',
        'https://sdmines.sdsmt.edu/cgi-bin/global/adprotected/its_review_tablet_repairs.cgi?reviewid=95&perpage=25&pagenum=1']


ques = messagebox.askquestion("WorkScripts", "Edit url file?")

if ques == 'no':
    def windows_os(urls):
        # Windows spesific code here
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        for url in urls:
            webbrowser.get(chrome_path).open(url,new=1)


    def macos_os(urls):
        chrome_path = 'open -a /Applications/Google\\ Chrome.app %s'
        #outlook_path = 'open -a /Applications/Microsoft Outlook.app'
        subprocess.Popen(['open', '/Applications/Microsoft Outlook.app/'])
        for url in urls:
            webbrowser.get(chrome_path).open(url,new=1)
    # Linux to be added later
    # def linux_os():
    #     chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    #     return webbrowser.get(chrome_path).open(url)


    if sys.platform.startswith('darwin'):
        macos_os(urls)
    elif sys.platform.startswith('win32'):
        windows_os(urls)
    # elif sys.platform.startswith('linux'):
    #     linux_os()
    else:
        print('Unsupported operating system')
        exit(0)
else:
    messagebox.showinfo("showinfo","Editing files is to be added later")
    print("Editing files is to be added later")
    exit(0)