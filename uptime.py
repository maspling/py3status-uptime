import subprocess
import time
import re

class Py3status:

	format = 'UP: %uptime'
	color = "#FFFFFF"
	pretty = False

	def uptime(self, i3s_output_list, i3s_config):
		text = ""
		if self.pretty:
			process = subprocess.Popen(["uptime","-p"],stdout=subprocess.PIPE)
			text = process.stdout.read().decode("UTF-8").rstrip("\r\n")
			text = re.search("up *?([^ ].*)",text).group(1)
		else:
		 	process = subprocess.Popen(["uptime"],stdout=subprocess.PIPE)
		 	text = process.stdout.read().decode("UTF-8").rstrip("\r\n")
		 	text = re.search("up *?([0-9].*?),",text).group(1)
		response = {
			'color': self.color,
			'full_text': self.format.replace("%uptime",text)
		}
		return response

if __name__ == "__main__":
	from time import sleep
	x = Py3status()
	while True:
		print(x.uptime([],{}))
		sleep(1)
