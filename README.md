<h1 align="center">
Pocket with Tags recipe for Calibre
</h1>

<span class="badge-paypal"><a href="https://www.paypal.me/MarcinMagnus" title="Donate to this project using Paypal"><img src="https://img.shields.io/badge/paypal-donate-yellow.svg" alt="PayPal donate button" /></a></span> 
<span class="badge-flattr"><a href="https://flattr.com/profile/mmagnus" title="Donate to this project using Flattr"><img src="https://img.shields.io/badge/flattr-donate-yellow.svg" alt="Flattr donate button" /></a></span>
</p>

Table of contents:

  * [Settings](#settings)
  * [Installation](#installation)
  * [Changelog](#changelog)

[Pocket](https://getpocket.com/), previously known as Read It Later, is an application and service for managing a reading list of articles from the Internet. The application allows the user to save an article or web page to the cloud for later reading. The article is then sent to the user's Pocket list (synced to all of their devices) for offline reading. Pocket removes clutter from articles and allows the user to adjust text settings for easier reading [Source](https://en.wikipedia.org/wiki/Pocket_%28application%29).

[Calibre](http://calibre-ebook.com/) is a free and open source e-book library management application developed by users of e-books for users of e-books. The programs also allows users to create own e-books and syncing with a variaty of e-book readers (e.g. Kindle, that's how I got the screenshots below) [Source](https://en.wikipedia.org/wiki/Calibre_%28software%29). Calibre has a plugin management system and ..

**This plugin allows users to get their Pocket-ed articles with Calibre and send them as an e-book to their prefered e-book reader. You can schedule this process and every day get the freshest e-book with your Pocket-ed articles!**

Follow the discussion at https://www.mobileread.com/forums/showthread.php?t=270602

This is a fork of the original plugin and a merge of a fix by @dlo9.

I modified the plugin to get an e-book including:

* The latest (more or less as the original version of the plugin)
* your content organized by tags!

Now, you get **The latest** and **The content organized by your tags**:

<table><tr><td><img src="doc/02.png" alt="" style="width: 200px;"/></td><td><img src="doc/03.png" alt="" style="width: 200px;"/></td></tr></table>

.. before:

<img src="doc/01.png" alt="" style="width: 200px;"/>

At the moment you have to define your own tags in the code (variable `self.tags`). It should be changed at some point.

This is a fork of the original 2011 Calibre ReadItLater plugin.

# Settings

```python

    # User-configurable settings -----------------------------------------------
    tags = [''] # get The latest, this is pretty much how the original version of the plugin works
    # !! comment out this and put your tags !!
    #tags = ['', 'iphone'] #get "The latest" and articles tagged with `iphone` 
    title_with_tags = True # if True then the ebook filename will be like Pocket: INVEST P2P [Sun, 05 Jan 2020]

```

To change settings, click on:

	Fetch news -> Add custom news source -> Pocket (Edit this recipe)

and edit the Python code.

![](doc/settings.png)

# Installation

* Under the "Fetch News" drop down select "Add a Custom Source"
* Click "Load Recipe From File" and choose the Pocket.recipe file
* Edit max_articles_per_feed & minimum_articles to set your max and minimum articles downloaded per eBook
* Save and Close
* Under "Schedule News Download" Select the new Pocket recipe under custom and fill out your credential

If you have any problem read more [at Pocket](https://help.getpocket.com/customer/portal/articles/361724-how-to-configure-calibre-with-pocket)

# Changelog
## Current

* 200104 Incorporate code from David Orchard (https://github.com/dlo9/calibre-recipes) to fix an issue with Pocket Authentication API
* 170503 Download all images from every article by Stefan Wagner (@bompo)
* 170503 Decide what to pull (all vs unread)
* 170502 `Pocket + [Mon, 05 Dec 2016]`
* 160817 Add links to articles.

<img src="doc/screenshot_2016_08_29T20_43_53_0200.png" alt="" style="width:100px;"/>

* 160205 Modified version of the plugin to get (1) The latest (more or less as the original version of the plugin) (2) and your content organized by tags! 
# Development
Links on development of recipes:

* https://manual.calibre-ebook.com/news.html
* https://manual.calibre-ebook.com/news_recipe.html
* https://manual.calibre-ebook.com/creating_plugins.html#more-plugin-examples

The default Calibre plugin is here https://github.com/kovidgoyal/calibre/blob/master/recipes/readitlater.recipe

`calibre-debug --paths --gui-debug ~/Library/Preferences/calibre/custom_recipes/Pocket__1004.recipe`
