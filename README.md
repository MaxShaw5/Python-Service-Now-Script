This script can be used to open a SeviceNow queue of your choosing, take a screenshot and then save the screenshot to whatever directory you would like.

I personally am chooosing to save it to a OneDrive account connected to my Power Automate account so that I can have it attach the screenshot and a link to the SNow queue in an email to remind people when they have tickets without updates.

To adjust the URLs, login credentials, and file paths for the screenshots to be saved, simply add them to a seperate file named variables.py and then call them the way I have in my script after importing them.

If you have a different set of login pages for your SNow instance (this is almost certainly the case) you will need to adjust the script (and maybe remove or add a few lines) a bit to fit the elements present on the pages you are navigating.
