# FindFile
Looks through whole device in order to find a specific file. Once done it proceeds to email it to you

<br>

**How to get/recieve emails using FindFile.py:**
- In FindFile.py, look for the three variables, <code>fromaddr</code>, <code>frompassword</code>, and <code>toaddr</code>
- Put the email you want to send the files from at <code>fromaddr</code> (make sure that you have the 'less secure app access' setting turned on)
- Put the password for the email at 'frompassword'
- Put the email you want to recieve the files at in 'toaddr'

**How to search for a specific file using FindFile.py:**
- In line 38, there should be a variable called files, to which it is assigned the result of the function 'findfile()'
- In the first parameter of the function, enter the term you want to search for
- In the second parameter, enter the extensions you want to search for as '.*insert extension*'
- If you want to search for any extension, leave it as a blank list
- In the third parameter, enter the directory from which you want to start searching from
- For mac, the root directory is simply '/', but I recommend to put '/Users' to search only in the personal files of the user, as the rest is mostly system files
- For windows, the root directory is '\', however be careful when you do this and also leave the extensions blank(for the second parameter), as windows generally has '.lnk' type files, which are against Google TnC's, meaning that there will be an error when the email is sent. To avoid this just be specific about the file type that you want to look for

<br>

**WARNING**  
The email I have put for the 'fromaddr' variable is randomly generated and is free to access as I have also included the password to it in the script, however I highly recommend you swap it out for your own. This is because I dont want my inbox flooded, and also because I will be able to see the location from which you have logged in from, and any file you send through the email.
