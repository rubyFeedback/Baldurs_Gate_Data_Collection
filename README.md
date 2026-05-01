# Baldurs_Gate_Data_Collection
This repository may contain some information related to the old game called BG
(Baldur's Gate). Though, I personally focus more on BG2 only - thus, BG1 or SoD and
so forth, are at best **secondary focus points**. For the time being we could
therefore call this repository a BG2 repository only.

Please do take note that this repository may only be very **rarely updated**. Right
now I only use it to publish the .yml files I use to track remote mods (BG2
mods for the most part), as well as one .rb (ruby) file that evaluates the 
logic in these .yml file. That way others can look at the information and 
adjust it for their own case; and may adjust the .rb file to their own
use cases. Take note that the remaining part of the ruby code is unfortunately
not distributed here; it used to be published on rubygems.org, but for several
reasons taking too long to explain, I am currently not using rubygems.org. I
may republish at spinel or at github here, but right now this is not the case
(it requires quite many local adjustments, and right now I can not commit 
due to other time constraints - so for the most part, the two .yml files
are the most important parts of this repository).

What follows next is a partial explanation how these two .yml files are used.

The first .yml file, called **array_mod_installation_order.yml**, will show which mods
are tracked. This is a simple Array - first entries will be installed first. The name
given here must be unique, and defined in the second .yml file. Either way the first
.yml file is very simple, so let's consider the second file.

The second .yml file, called **detailed_mod_installation_instructions.yml**, is much larger
and more complex. It contains all information needed to download the mod. The idea is that
from this dataset, we can build external tools, such as in ruby or python, that
will do the actual download-and-repackage work. You may also need a copy of weidu.exe,
though most external mods bundle such an .exe anyway.

If a change is made to a remote-hosted MOD, then this second .yaml file should be
updated, to provide a "pointer" to that remote MOD. This is currently manual work,
so it may become outdated in a little while. But the "git clone" command that I
use, always ties to github (at the least for mods hosted at github), which then
fetches the most recent source. I also found that one may need to distribute the
weidu.exe, named the same as the corresponding .tp2 file. At the least I do this
for now in the ruby code.
