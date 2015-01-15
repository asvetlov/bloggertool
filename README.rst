Bloger Tool
===========

Command line tool to communicate with blogger.com and blogspot.com.

This project contains single (and simple enough) console command named 'blog'.
Typical usage scenario:

Init project::

   $ blog init path/to/blog/articles
   $ cd path/to/blog/articles

Sorry, Google change the rules at 2014 and you have to register your
blog to use Blogger API.

You should go to https://console.developers.google.com first and ask
for "Blogger API v3" access. Manager will grant required rights. If
you don't override quotas it's free, I don't pay for my personal
http://asvetlov.blogspot.com blog for example.

After that you need to open "Credentials" page in
https://console.developers.google.com, press "Download Json" button
and save the file as .client_secret.json in the root of your blog
project (the directory used for blog init call).




Make and edit article file::

   $ touch article.md

Add post to local database::

   $ blog add article.md

Open in browser locally generated html file for article.md::

   $ blog open article.md

Publish post on blosgspot.com::

   $ blog publish article.md

Edit `article.md` by making some changes

Synchronize remote presentation with local markdown file ::

   $ blog push article.md

For other available commands please see::

   $ blog --help
