# rofi-visa

A bash script to lookup [Passport Index Dataset](https://github.com/ilyankou/passport-index-dataset)
for visa status by using [rofi](https://github.com/DaveDavenport/rofi).

## Installation

```
git clone
pip install -r requirements.txt
chmod +x rofi-visa
rofi-visa -c Sweden -s

```

## Usage

```
Usage:
rofi-visa
         -c  Current Resident Country - Required
         -s  Visa status for selected Countries in config.yaml
         -f  Countries not requiring visa
         -r  Countries requiring Visa
         -o  Countries offering Visa on arrival
         -e  Countries offering Electronic Travel Authority
         -n  Countries offering visa free days
         -h  help

```

* Lookup  all Countries offering visa-free travel given a resident Country.
```
rofi-visa  -c Germany -f

```
* Lookup all Countries requiring visa given a resident Country.
```
rofi-visa  -c China -r

```
* Lookup all Countries offering visa-on-arrival given a resident Country.
```
rofi-visa  -c Vatican -o

```
* Lookup all Countries offering ETA(Electronic Travel Authority) given a resident Country.
```
rofi-visa  -c Vatican -e

```
* Lookup specific Countries and their visa status given a resident Country. Specify the Countries in config.yaml
```
config.yaml

 Countries:
  [Austria
  ,Belgium
  ,Canada
  ,Denmark
  ,Switzerland
  ,Vatican]

```

```
rofi-visa  -c Vatican -s
```
## Requirements

* [rofi](https://github.com/DaveDavenport/rofi)
* git
* python
* bash
