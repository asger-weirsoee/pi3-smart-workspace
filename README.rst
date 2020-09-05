About
-----

Simple program that looks through the i3 config and finds the bound workspaces for each output, and then opening that workspace on the output, that the mouse is currently on.

Allowing for a more seameless interaction with how workspaces are openend. 

Usage
-----

::

   usage: pi3-smart-switch [-h] -i num
   Openens the [i] number of workspace assigned in the config, on the output the cursor is currently on.


   requred arguments:
     -i, --index      the number index of the workspace that should be openend. 1 =  first workspace in config etc.

Current limitations
--------------------
The way this script is set up, it is sending commands in strings. and thus we cannot keep track of each workspace other than by its name. This is a limmitiaion as there is no way for us to know if the workspace "1" is reffering to the workspace 1 assigned to output DS-1 or output HDMI-2..

So in order to differentiate between these, you need to name your workspaces new names for each output. See example configuration under #Installation.


Installation
------------

Install using pip (recommended):

::

   pip install pi3-smart-workspace

Example config to be inserted into your i3 config.

::

    	# Displays
	set $primary DP-2
	set $left HDMI-0
	set $right HDMI-1

	# Workspaces
	set $ws1 1:1:Code
	set $ws2 2:2:Code
	set $ws3 3:3:Code
	set $ws4 4:4:Code
	set $ws5 5:5:Code
	set $ws6 6:6:Code
	set $ws7 7:7:Code
	set $ws8 8:8:Code

	set $LeftWs1 1:1:Browser
	set $LeftWs2 2:2:Left
	set $LeftWs3 3:3:Left
	set $LeftWs4 4:4:Left
	set $LeftWs5 5:5:Left
	set $LeftWs6 6:6:Left
	set $LeftWs7 7:7:Left
	set $LeftWs8 8:8:Left

	set $RightWs1 1:1:Right
	set $RightWs2 2:2:Right
	set $RightWs3 3:3:Right
	set $RightWs4 4:4:Right
	set $RightWs5 5:5:Right
	set $RightWs6 6:6:Right
	set $RightWs7 7:7:Right
	set $RightWs8 8:8:Right

	# Workspace assignments
	workspace $ws1 output $primary
	workspace $ws2 output $primary
	workspace $ws3 output $primary
	workspace $ws4 output $primary
	workspace $ws5 output $primary
	workspace $ws6 output $primary
	workspace $ws7 output $primary
	workspace $ws8 output $primary

	workspace $LeftWs1 output $left
	workspace $LeftWs2 output $left
	workspace $LeftWs3 output $left
	workspace $LeftWs4 output $left
	workspace $LeftWs5 output $left
	workspace $LeftWs6 output $left
	workspace $LeftWs7 output $left
	workspace $LeftWs8 output $left

	workspace $RightWs1 output $right
	workspace $RightWs2 output $right
	workspace $RightWs3 output $right
	workspace $RightWs4 output $right
	workspace $RightWs5 output $right
	workspace $RightWs6 output $right
	workspace $RightWs7 output $right
	workspace $RightWs8 output $right

	# Shift workspace
	bindsym $mod+1 exec pi3-smart-workspace -i 1
	bindsym $mod+2 exec pi3-smart-workspace -i 2
	bindsym $mod+3 exec pi3-smart-workspace -i 3
	bindsym $mod+4 exec pi3-smart-workspace -i 4
	bindsym $mod+5 exec pi3-smart-workspace -i 5
	bindsym $mod+6 exec pi3-smart-workspace -i 6
	bindsym $mod+7 exec pi3-smart-workspace -i 7
	bindsym $mod+8 exec pi3-smart-workspace -i 8

	# Move focused container to workspace
	bindsym $mod+Ctrl+1 exec pi3-smart-workspace -i 1 -s
	bindsym $mod+Ctrl+2 exec pi3-smart-workspace -i 2 -s
	bindsym $mod+Ctrl+3 exec pi3-smart-workspace -i 3 -s
	bindsym $mod+Ctrl+4 exec pi3-smart-workspace -i 4 -s
	bindsym $mod+Ctrl+5 exec pi3-smart-workspace -i 5 -s
	bindsym $mod+Ctrl+6 exec pi3-smart-workspace -i 6 -s
	bindsym $mod+Ctrl+7 exec pi3-smart-workspace -i 7 -s
	bindsym $mod+Ctrl+8 exec pi3-smart-workspace -i 8 -s

	# Move to workspace with focused container
	bindsym $mod+Shift+1 exec pi3-smart-workspace -i 1 -sk
	bindsym $mod+Shift+2 exec pi3-smart-workspace -i 2 -sk
	bindsym $mod+Shift+3 exec pi3-smart-workspace -i 3 -sk
	bindsym $mod+Shift+4 exec pi3-smart-workspace -i 4 -sk
	bindsym $mod+Shift+5 exec pi3-smart-workspace -i 5 -sk
	bindsym $mod+Shift+6 exec pi3-smart-workspace -i 6 -sk
	bindsym $mod+Shift+7 exec pi3-smart-workspace -i 7 -sk
	bindsym $mod+Shift+8 exec pi3-smart-workspace -i 8 -sk


Credits
-------

Thanks to Michał Wieluński for an inspiration (`pi3-switch`_) and
Tony Crisci for an easy-to-use i3 python library (`i3ipc-python`_).

.. _pipsi: https://github.com/mitsuhiko/pipsi
.. _pi3-switch: https://github.com/landmaj/pi3-switch
.. _i3ipc-python: https://github.com/acrisci/i3ipc-python
