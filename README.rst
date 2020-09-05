About
-----

Simple program that looks through the i3 config and finds the bound workspaces for each output, and then opening that workspace on the output, that the mouse is currently on.

Allowing for a more seameless interaction with how workspaces are openend. 

Usage
-----

::

   usage: pi3-smar-switch [-h] [-f] [-p | -m | -s] WORKSPACE_NAME

   Moves selected i3 workspace to the current output (by default determined by
   cursor location) and focuses it.

   positional arguments:
     workspace     name of the i3 workspace

   optional arguments:
     -h, --help    show this help message and exit
     -f, --focus   use focused window instead of cursor position to determine the
                   current output
     -p, --push    moves replaced workspace to the second output (works only if
                   there are two outputs, ignored otherwise)
     -m, --master  same as 'push' but will only move from primary output to the
                   secondary
     -s, --swap    (NOT IMPLEMENTED YET) behaves like xmonad, swaps workspaces if
                   they are on a different output

Installation
------------

Install using `pipsi`_ (recommended) or pip:

::

   pipsi install pi3-switch

Add keybindings to ~/.config/i3/config and reload i3 (remember to modify flags to your liking):

::

   bindsym $mod+1 exec pi3-switch -p 1
   bindsym $mod+2 exec pi3-switch -p 2
   bindsym $mod+3 exec pi3-switch -p 3
   bindsym $mod+4 exec pi3-switch -p 4
   bindsym $mod+5 exec pi3-switch -p 5
   bindsym $mod+6 exec pi3-switch -p 6
   bindsym $mod+7 exec pi3-switch -p 7
   bindsym $mod+8 exec pi3-switch -p 8
   bindsym $mod+9 exec pi3-switch -p 9
   bindsym $mod+0 exec pi3-switch -p 10

Credits
-------

Thanks to Travis Finkenauer for an inspiration (`i3-wk-switch`_) and
Tony Crisci for an easy-to-use i3 python library (`i3ipc-python`_).

.. _pipsi: https://github.com/mitsuhiko/pipsi
.. _i3-wk-switch: https://github.com/tmfink/i3-wk-switch
.. _i3ipc-python: https://github.com/acrisci/i3ipc-python
