ebook-convert Pocket.recipe .pdf #& open Pocket.mobi
#ebook-convert Pocket.recipe .mobi #& open Pocket.mobi

# this will overwrite a file there ! add something to the name if you want to prevent that
mv  -v Pocket.pdf "/Users/magnus/Dropbox/boox/Pocket `date +'%b %d %Y %H%M'`.pdf"
# --backup=numbered --suffix '.pdf'# go to a folder and clean up naming
#cd /Users/magnus/Dropbox/boox
#mmv -v "*.*~*~" "#1_#3.#2"
#cd -

# credits <https://serverfault.com/questions/267255/mv-rename-if-exists>
#                     "*.*~*~" "#1_#3.#2"
# Pocket Mar 08 2021.pdf.~1~ -> Pocket Mar 08 2021_1.pdf. : done
# Pocket Mar 08 2021.pdf.~2~ -> Pocket Mar 08 2021_2.pdf. : done

# sync
boox.py
