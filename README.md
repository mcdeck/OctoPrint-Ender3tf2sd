# OctoPrint-Ender3tf2sd

A simple plugin to make OctoPrint recognize the SD card in your Ender 3 (Pro).

It seems that Marlin (depending on which version you use, I guess) sends ```TF card ok``` instead of ```SD card ok``` as OctoPrint expects. People in the OcotPrint community solved this by uploading a plugin via SSH (see [Thread on the forums](https://community.octoprint.org/t/octopi-not-reading-sd-card-or-print-progress-from-ender-3-solved/9821/5)). I wanted this to be installable via the WebUI, though, which is why I made this plugin.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/mcdeck/OctoPrint-Ender3tf2sd/archive/master.zip

## Configuration

No configuration necessary.
