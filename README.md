# Baldurs_Gate_Data_Collection
This repository may contain some information related to the old game called BG.

Please do take note that this repository may only be very rarely updated. Right
now I only use it to publish the .yml files I use to track remote mods (BG2
mods for the most part). That way others can look at the information and 
adjust it for their own case.

I also use a few ruby classes to help download this; these are currently
not published. I may eventually publish them, but I can not promise when.

As this may take some time, let me thus briefly explain the two .yml files.

The first .yml file, called **array_mod_installation_order.yml**, will show which mods
are tracked. This is a simple Array - first entries will be installed first. The name
given here must be unique, and defined in the second .yml file. Either way the first
.yml file is very simple.

The second .yml file is much larger and more complex. It contains all 
information needed to download the mod. The idea is that from this
dataset, we can build external tools, such as in ruby or python, that
will do the actual download-and-repackage work. You may also need
a copy of weidu.exe, though most external mods bundle such an .exe
anyway.
