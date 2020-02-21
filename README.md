# IndexWatcher
A quick and dirty watcher for the valve index. It essentially watches the index page for changes in the number of times "Notify Me" appears in the html (it's a lot) and this application also watches the @Valve account on twitter for new tweets. I wanted to know anytime _anything_ happened so I didn't put filtering of any kind on it. I'd also like to point out that it's best to run this on a raspberry pi so you don't have to keep a terminal window open on your own machine. 

## Setup 
Okay, so this is not easy to setup. In my case it's not terrible because I already had a twitter and twilio dev account. I will provide instructions on how to get a Twilio account setup but I will not be going through the Twitter steps yet. If you'd like to contribute them please let me know or make a pull request. I also don't know if Twilio offers services in Europe or other regions so just something to consider. This may only work for US phone numbers. 

Lastly, this guide is targeted to someone who is at least somewhat tech savvy. If you're already familiar with Python it might be a bit of a slog and I'm sorry. 

### Get a Twilio Account
- Visit https://twilio.com
- "Sign up for free"
- Verify your email
- Verify your phone (It's CRITICAL that you do this)
- Once you've reached the dashboard, click the 3 dot circle menu thing off to the left
- Select "Phone Numbers" 
- Hit "Get Started" 
- Hit "Get your first Twilio phone number"
- Use the one they suggest OR pick one, doesn't matter
- Hit "Buy Phone Number" (Don't worry, you're on a trial and will not be charged, you get $15 in credit when you sign up)
- Write down the phone number with the country code (ex: +15555555555)
- Now on the left, go to "Verified Caller IDs" 
- Check that your number is on that list. If it isn't, add it.
- After that, click the menu dots on the left again and go to "Programmable SMS"
- Hit "Get Started" 
- You'll have a section that says "Send A Message" 
- Put your phone in "TO"
- Make sure your new number is "FROM" 
- Write a simple message and send it.
- If you got it, GREAT, we're almost done here.
- Now, go back to the home screen (Top left, house icon)
- Copy your Account SID and Auth Token somewhere SAFE. 
- Close Twilio, you're good. The credits should last you a while so no worries.


### Installing the thing (Windows)
Depending on how setup you are already and how techsavvy you are, this might be a pita. I will look into making it easier for sure especially if this round of preorders gets sold out instantly again. 

- First up, go to https://www.python.org/
- Download and install Python (3.8.1 is latest as of writing this)
- It's faily straight forward *BUT MAKE SURE THAT YOU CHECK ALL THE BOXES RELATED TO "PATH" or "ENVIRONMENT VARIABLES"*
- Restart your computer.
- You can check that it's installed by opening either powershell or cmd and typing "python -v". 
- There is much better documentation than I could ever write on troubleshooting and using python so I will keep it at that.
- Once you have that download the code from this page (get a zip to make it easier). After that, place it in a folder on your machine, I'd use somewhere in Documents if you aren't sure where to put it. 
- Now in the IndexWatcher folder open up config.json in Notepad (or anything besides word and wordpad, I'd recommend VSCODE)
- Now if you're unfamiliar with JSON left of the _:_ is setting name, right of it is the value. 
- You want to paste your access keys etc into the left side in the quotes. 
- If you don't want to use twitter, set "checkValveTwitter" to "0" (ex: "checkValveTwitter":"0",)
- After you have the config.json all set, you can save and close the file.
- Now, open a terminal/CMD/Powershell window in this folder (Shift + Right Click in the folder to get the option)
- Now we run the command `python IndexWatcher.py` and it should send us at least one text as it starts up as a test. 
- If you got said text, you're all set. Keep this window open and it will keep doing it's job. 

I'll eventually refine this a bit, but it really depends on how this restock goes. Also, VIAC is already a superior product, I just wanted texts. 


### Info on Twitter Dev Account
I'm not going to make the instructions at this time for Twitter. It's a bit of a PITA but just know that none of the questions are trick questions and we ONLY WANT TO READ tweets so just be honest and you'll be fine. If you want to skip twitter you can by setting the "checkValveTwitter" setting to "0" instead of "1"