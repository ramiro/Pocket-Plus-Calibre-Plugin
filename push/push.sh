#!/bin/bash

# configure
mail_username=
mail_passwd=
kindle_mail=
mail_from=
mail_server=
polityka_username=
polityka_passwd=
pocketx_path=/Users/magnus/workspace/Pocket-Plus-Calibre-Plugin/pocketX

set -x
date
cd $pocketx_path
yes | rm PocketX.mobi
ebook-convert PocketX.recipe .mobi
calibre-smtp -a PocketX.mobi -u $mail_username --password $mail_passwd $mail_from $kindle_mail BODY --encryption-method SSL -v -r $mail_server

sleep 15 # time to upload pseudo-feed to Dropbox

cd $pocketx_path/recipes

source='polityka.pl'
yes | rm $source.mobi
ebook-convert $source.recipe .mobi --username $polityka_username --password $polityka_passwd
calibre-smtp -a $source.mobi -u $mail_username --password $mail_passwd $mail_from $kindle_mail BODY --encryption-method SSL -v -r $mail_server
