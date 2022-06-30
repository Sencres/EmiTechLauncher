# EmiTech

An updater script made for the Emicord server utilizing MultiMC's pre-launch command function and GitPython.
This script was designed to pull updates to the EmiTech modpack without requiring a redownload or re-import of the modpack itself, i.e. it only downloads changes and works directly inside the instance folder.
Minor modifications to this script can allow it to be used with other repositories, along with a rebuild of main.exe if needed.
It is currently set to update from https://github.com/Aririi/EmiTech/

**Installation steps:**
- If you do not have MultiMC already, follow the instructions here to download it: https://multimc.org/#Download%20&%20Install
- Click on the green "*Code*" button, then "*Download ZIP*"
  - Warning: Do not clone this repo, just pull or download it. It's a bit... busted. It takes up more space than it should, couldn't fix it :(
- Drag the "*EmiTech-master*" zip folder into MultiMC's GUI, it should open the "*Import from zip*" window. Click "*OK*" to extract it.
- Configure your instance settings, if needed or preferred. You should know if the instance is configured correctly if there is an icon for it, and when you launch the game the updater script should also run.
- That's it! Launch the instance and the script should download the content from the configured repository and update every launch (if an update is available).  
- Depending on your internet download speed and disk performance, this can take a few minutes. However, it should take no longer than 10 minutes for the first time, and about a minute for every update. If any errors occur and the game does not launch, please contact the authors.
- If you get a **"java.lang.reflect.InvocationTargetException" error on launching the pack, see below: 
  - You need the latest version of Java Runtime Environment (JRE) 8, the latest right now is **u333*, which you can obtain here https://www.java.com/en/download/. Note, if you play multiple versions of MC, install this alongside your current Java, then in MultiMC just configure which version to use by going *Edit Instance* > *Settings* > *Auto-detect* and selecting the right version. 
- Note: If you're on Linux and have Git installed, you can configure the *Pre-launch Command* under *Settings* for the instance to use **"main.sh"**, but you shouldn't need to as the main.exe will auto-run the .sh script anyways.
