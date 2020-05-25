set -x
date
cd /Users/magnus/workspace/Pocket-Plus-Calibre-Plugin/pocketX
rm PocketX.mobi
ebook-convert PocketX.recipe .mobi # && ../Pocket-send-to-amazon.py PocketX.mobi; cd -'
# calibre-smtp -a PocketX.mobi -u magXXXX --password XXXXXXXXXXXX XXXXXXXXx XXXXXXXXX BODY --encryption-method SSL -v -r poczta.o2.pl
