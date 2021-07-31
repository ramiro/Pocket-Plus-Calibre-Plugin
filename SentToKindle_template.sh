function sent {
    # a secret.sh is a file with config for sending books to Amazon
    # polityka_username=ma..
    # polityka_passwd=KT..
    # mail_username=mag..
    # mail_from=mag..
    # mail_passwd=xa..
    # kindle_mail=mag..
    # mail_server=poc..
    source secret.sh
    echo 'mail: sending...'
    Calibre-smtp -a Pocket.mobi -u $mail_username --password $mail_passwd $mail_from $kindle_mail BODY --encryption-method SSL -r $mail_server
}

#archive
#dev
# rm /Users/magnus/Dropbox/feed.xml # reset feed ;-)
#export pocketx_archive=False # not dev does not work at all
rm Pocket.mobi
rm ~/Documents/My\ Kindle\ Content/Pocket.mobi
ebook-convert Pocket.recipe .mobi # --debug-pipeline debug  #; & open Pocket.epub
if test -f "Pocket.mobi"; then
    #open Pocket.mobi # check of missing images or problems
    /usr/local/bin/ebook-viewer Pocket.mobi
    # sent
fi
