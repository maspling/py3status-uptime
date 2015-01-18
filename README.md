# py3status-uptime
Uptime module for py3status

## Installation
To install the module you must first get the py3status sources and insert the module into the modules directory.

```
cd ~
mkdir -p src
cd src
git clone https://github.com/ultrabug/py3status.git
git clone https://github.com/Yugge/py3status-uptime
cp py3status-uptime/uptime.py py3status/py3status/modules/
```
Then build/install py3status as per usual
```
cd py3status
sudo python setup.py install
```

## Configuration
Configure the module [as per usual.](https://github.com/ultrabug/py3status/wiki/Load-and-order-py3status-modules-directly-from-your-current-i3status-config)

The following configuration options are available:
- **color** - Color of the output, as hexstring (Default: #FFFFFF)
- **format** - Format string for the output, the uptime text will be inserted at *%uptime* (Default: "UP: %uptime")
- **pretty** - Sends the -p flag to the uptime command, giving a prettified output. (Default: False)

## What is left to do?
An improvement would be to parse uptime -s and make it available with the [strftime](http://strftime.org/) syntax.

## Why haven't you made this a pull request for py3status?
Well, I probably will when I feel the module is completed.
