# SigilPlugin_EndNotesToParagraphs
In an epub, transforms an ordered list of endnotes in static numbered paragraphs, adds backlinks from notes to references, updates css

This plugin has been tested with Sigil v. 0.8.6 on Windows 7, Ubuntu 15.04 and Mac OS X 10.10.5 (all 64 bit).

To run the plugin:
1) If you haven't already, install Python interpreter v3.4 (downloadable from www.python.org), then install BeautifulSoup4 (in Windows you can, from the command line, go to the folder "Scripts" inside the installation folder of python and type "pip install beautifulsoup4"; on Mac and Ubuntu probably you'll have to type "pip3 install beautifulsoup4" without worrying about the folder - except if you're using virtual environments or you have installed multiple versions of python3, but if it's so I assume you know what to do. More on pip: https://pip.pypa.io/en/stable/). If you don't want to do all these installations, you must be patient: Sigil 0.8.9 will come shortly (I hope) with python and beautifulsoup out of the box.
2) Download all the files from this repository.
3) Pack the files in a zip archive named endNotesToParagraphs.
4) Open Sigil, go to menu Plugins -> Manage Plugins. If it hasn't already, set the path for python3.4, then click on Add Plugin and select the zip file.
5) Launch the plugin from menu Plugins -> Edit -> endNotesToParagraphs.

The default language of the plugin is english. If you prefer italian, you can change one of the first lines of plugin.py with a text editor, from "language = languages.english" to "language = languages.italiano".

All the html entities in the epub will be converted to respective unicode characters, except &amp;nbsp;, &amp;ensp;, &amp;emsp;, &amp;thinsp;, &amp;shy; (xml entities will be preserved, too: &amp;lt;, &amp;gt;, &amp;quot;, &amp;apos;, &amp;amp;). If you want to preserve other html entities, you must add them in plugin.py: more or less 25 lines before the end of the file, you must update the dictionary preserveEntities (if you don't know how to do, just look at the other entries of the dictionary and make the same).
