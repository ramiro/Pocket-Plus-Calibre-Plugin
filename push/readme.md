Push
-------------------------------------------------------------------------------

## Create a Shortcut to create a file in given folder

Here I use Shortcut for iPhone, the trigger phrase is "Push".

<table><tr><td><img src="imgs/1.png" alt="" ></td><td><img src="imgs/2.png" alt="" /></td><td><img src="imgs/3.png" alt="" ></td></tr></table>

## This Shortcut will make a file in iCloud/Shortcuts

![](imgs/trigger-file.png)

## This new file will be detected by this script and my calibre push script will be executed

    * * * * * /Users/magnus/workspace/Pocket-Plus-Calibre-Plugin/push/push-crontab.sh
    # this is just fancy wrapper to get cron run every 5 s
