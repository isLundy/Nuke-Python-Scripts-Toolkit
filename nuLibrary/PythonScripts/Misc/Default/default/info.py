"""This module contains general information about this tool."""


TOOLNAME = "default"
AUTHOR = "Simon Jokuschies"
WEBSITE = "http://www.leafpictures.de"
WEBSITE_TOOL = "{}/{}".format(WEBSITE, TOOLNAME)
EMAIL = "info@leafpictures.de"
VERSION = "5.0.0"

ABOUT_INFO = """<h2>default version {version}</h2>
<b>Author:</b> {author}<br />
<b>email:</b> {email}<br />

<h3>Description</h3>
Default is a script that lets you create knobDefaults without any scripting.
<h4>add new knobDefault</h4>
Just right click a knob and choose default->set as new knob default.
The current value will be set to the new knob default.
<h4>Access all knobs</h4>
Drop down elements for some reason don't carry a right click menu. But you can still access
them if like to set a knobDefault to them as well. In fact you can access all knobs of each node. 
Just right click a knob and choose default->show knob list. A window pops up in which you will 
find a drop down and a text input. The drop down carries all knobs of the selected node. 
Just select a knob from the drop down and enter the new knob default into the text input.
<h4>Reset a knob default</h4>
If you like to revert the knob value to its original default value just right click the 
value and choose default->reset.
<h4>The default edit window</h4>
Choose Scripts->default->defaults window. A window appears showing all the custom knobDefaults 
that you have set. You can access all of them, edit and delete them and add new knobDefaults.<br /><br />
For more NUKE tools please visit {web}""".format(
    author=AUTHOR, email=EMAIL, version=VERSION, web=WEBSITE)
