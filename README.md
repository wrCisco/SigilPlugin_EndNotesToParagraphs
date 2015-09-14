# SigilPlugin_EndNotesToParagraphs
In an epub, transforms an ordered list of endnotes in static numbered paragraphs, adds backlinks from notes to references, updates css

This plugin has been tested with Sigil v. 0.8.6 on Windows 7 and Ubuntu 15.04 (both 64 bit). I see no reason why it shouldn't work on Mac, though.

To run the plugin:
1) If you haven't already, install Python interpreter v3.4 (downloadable from www.python.org).
2) Download all the files from this repository.
3) Pack the files in a zip archive named EndNotesToParagraphs (if you are willing to test on Mac, then you must before add "osx" at the <oslist> tag in plugin.xml).
4) Open Sigil, go to menu Plugins -> Manage Plugins. If it hasn't already, set the path for python3.4, then click on Add Plugin and select the zip file.
5) Launch the plugin from menu Plugins -> Edit -> EndNotesToParagraphs

The default language of the plugin is english. If you prefer italian, you can change one of the first lines of plugin.py with a text editor, from "language = languages.english" to "language = languages.italiano".

All the html entities in the epub will be converted to respective unicode characters, except &amp;nbsp;, &amp;ensp;, &amp;emsp;, &amp;thinsp;, &amp;shy;, &amp;lt;, &amp;gt;, &amp;quot;, &amp;apos;, &amp;amp;. If you want to preserve other html entities, you must add them in plugin.py: more or less 25 lines before the end of the file, you must update the dictionary preserveEntities (if you don't know how to do, just look at the other entries of the dictionary and make the same).
