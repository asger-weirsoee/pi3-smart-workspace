About
-----

Simple program that looks through the i3 config and finds the bound workspaces for each output, and then opening that workspace on the output, that the mouse is currently on.

Allowing for a more seameless interaction with how workspaces are openend. 

Usage
-----

::

    usage: pi3-smart-workspace [-h] [-d] -i INDEX [-s] [-k]

    Changes the workspace, based on what output your cursor is on.

    optional arguments:
      -h, --help            show this help message and exit
      -d, --debug           Turn on debug mode.

    Required:

      -i INDEX, --index INDEX
                            The indexed workspace for the output where the cursor is currently located

    Shift:
      manipulate the active window

      -s, --shift           Moves the active window to the index workspace
      -k, --keep-with-it    Moves the active window to the index workspace, and moves with it


Installation
------------

Install using pip (recommended):

::

   pip install pi3-smart-workspace

Example config to be inserted into your i3 config.

::

    # Displays
    set $primary eDP
    set $top HDMI-A-0
    set $bottom HDMI2

    # Workspaces
    set $ws1 1:1
    ... # And so on
    set $ws{n} {n}:{n}

    set $TopWs1 {n+1}:1
    ... # and so on
    set $TopWs{k} {n+1+k}:{k}

    set $BottomWs1 {k+1}:1
    ... # and so on
    set $BottomWs{q} {k+1+q}:{q}

    workspace $ws1 output $primary
    ... # and so on
    workspace $ws{n} output $primary

    workspace $TopWs1 output $top
    ... # and so on
    workspace $TopWs{k} output $top

    workspace $BottomWs1 output $bottom
    ... # and so on
    workspace $BottomWs{q} output $bottom

    # Shift workspace
    bindsym $mod+1 exec --no-startup-id pi3-smart-workspace -i 1
    bindsym $mod+2 exec --no-startup-id pi3-smart-workspace -i 2
    bindsym $mod+3 exec --no-startup-id pi3-smart-workspace -i 3
    bindsym $mod+4 exec --no-startup-id pi3-smart-workspace -i 4
    bindsym $mod+5 exec --no-startup-id pi3-smart-workspace -i 5
    bindsym $mod+6 exec --no-startup-id pi3-smart-workspace -i 6
    bindsym $mod+7 exec --no-startup-id pi3-smart-workspace -i 7
    bindsym $mod+8 exec --no-startup-id pi3-smart-workspace -i 8

    # Move focused container to workspace
    bindsym $mod+Shift+1 exec --no-startup-id pi3-smart-workspace -i 1 -s
    bindsym $mod+Shift+2 exec --no-startup-id pi3-smart-workspace -i 2 -s
    bindsym $mod+Shift+3 exec --no-startup-id pi3-smart-workspace -i 3 -s
    bindsym $mod+Shift+4 exec --no-startup-id pi3-smart-workspace -i 4 -s
    bindsym $mod+Shift+5 exec --no-startup-id pi3-smart-workspace -i 5 -s
    bindsym $mod+Shift+6 exec --no-startup-id pi3-smart-workspace -i 6 -s
    bindsym $mod+Shift+7 exec --no-startup-id pi3-smart-workspace -i 7 -s
    bindsym $mod+Shift+8 exec --no-startup-id pi3-smart-workspace -i 8 -s

    # Move to workspace with focused container
    bindsym $mod+Ctrl+1 exec --no-startup-id pi3-smart-workspace -i 1 -sk
    bindsym $mod+Ctrl+2 exec --no-startup-id pi3-smart-workspace -i 2 -sk
    bindsym $mod+Ctrl+3 exec --no-startup-id pi3-smart-workspace -i 3 -sk
    bindsym $mod+Ctrl+4 exec --no-startup-id pi3-smart-workspace -i 4 -sk
    bindsym $mod+Ctrl+5 exec --no-startup-id pi3-smart-workspace -i 5 -sk
    bindsym $mod+Ctrl+6 exec --no-startup-id pi3-smart-workspace -i 6 -sk
    bindsym $mod+Ctrl+7 exec --no-startup-id pi3-smart-workspace -i 7 -sk
    bindsym $mod+Ctrl+8 exec --no-startup-id pi3-smart-workspace -i 8 -sk


Future work
-----------
Here a few ideas on how to improve pi3-smart-workspace could be improved in the future.
If anyone wants to submit a pr that solves one of the problems stated below feel free to do so :)


-  Save the outputs and the mapped outputs in a json file, instead of looking through the config every time a button is pressed.
    This would greatly reduce the cost of running this program, if we could just look up the required value in the json instead of the whole i3 config.

    In order for this to be a thing, we need to transition away from looking at active display, have the user set a exec_always and out indexer in their i3 config.

-

Credits
-------

Thanks to Michał Wieluński for an inspiration (`pi3-switch`_) and
Tony Crisci for an easy-to-use i3 python library (`i3ipc-python`_).

.. _pipsi: https://github.com/mitsuhiko/pipsi
.. _pi3-switch: https://github.com/landmaj/pi3-switch
.. _i3ipc-python: https://github.com/acrisci/i3ipc-python
