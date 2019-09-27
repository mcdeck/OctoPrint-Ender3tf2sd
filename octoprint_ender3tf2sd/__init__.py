# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin

class Ender3tf2sdPlugin(octoprint.plugin.OctoPrintPlugin):

	def convert_tf_to_sd(self, comm, line, *args, **kwargs):
		if "TF" not in line:
			return line
		return line.replace("TF","SD")

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			ender3tf2sd=dict(
				displayName="Ender3tf2sd Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="mcdeck",
				repo="OctoPrint-Ender3tf2sd",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/mcdeck/OctoPrint-Ender3tf2sd/archive/{target}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Ender3tf2sd Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = Ender3tf2sdPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information,
		"octoprint.comm.protocol.gcode.received": __plugin_implementation__.convert_tf_to_sd,
	}

