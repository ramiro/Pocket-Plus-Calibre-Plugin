function prepare {
ebook-convert Pocket.recipe .mobi # --debug-pipeline debug  #; & open Pocket.epub
}

function sent {
    # Keep these values in secret.sh for your settings
    # mail_username=XXXX
    # mail_from=XXXX
    # mail_passwd=XXXX
    # kindle_mail=XXXX
    # mail_server=XXXX
    # pocketx_path=/Users/magnus/workspace/Pocket-Plus-Calibre-Plugin/pocketX
    source secret.sh
    echo 'mail: sending...'
    Calibre-smtp -a Pocket.mobi -u $mail_username --password $mail_passwd $mail_from $kindle_mail BODY --encryption-method SSL -r $mail_server
}

#archive
#dev
# rm /Users/magnus/Dropbox/feed.xml # reset feed ;-)
export pocketx_archive=False # not dev does not work at all
rm Pocket.mobi
prepare
if test -f "Pocket.mobi"; then
    open Pocket.mobi # check of missing images or problems
    # sent
    sleep 30
fi
