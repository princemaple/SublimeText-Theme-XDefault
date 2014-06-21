## Update

> This theme has not been maintained, so don't try/use it.
> I've been using Soda Dark 3 for a few months

### 2-May-2013
3031 added search bar drop down
catched up

### 9-April-2013
3024 doesn't add preivew file into the `OPEN FILES`	section in sidebar, so transient sidebar label is no longer needed.

### 4-April-2013
1. updated for dev 3023
2. updated theme3to2.py, bug fix

## Theme Info

Theme for [Sublime Text](http://www.sublimetext.com/). Intended to make default theme better. Actual work modified from [Night](https://github.com/mishu91/sublime-text-theme-Night).

## Installation

### Using Git

Go to your Sublime Text `Packages` directory and clone the theme repository using the command below:

    git clone https://github.com/princemaple/SublimeText-Theme-XDefault "Theme - XDefault"

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `Theme - XDefault`
* Copy the folder to your Sublime Text `Packages` directory

## Activating the theme

To configure Sublime Text to use the theme:

* Open your User Settings Preferences file `Sublime Text X -> Preferences -> Settings - User` where X can be 2 or 3
* Add (or update) your theme entry to be `"theme": "XDefault.sublime-theme"`

### Example User Settings

    {
        "theme": "XDefault.sublime-theme"
    }

## SublimeText 2 User!! Note!!

### To make it work in ST2
*You have to run the python script [`theme3to2.py`](https://raw.github.com/princemaple/workspace/master/theme3to2.py) in the theme folder before you actually use the theme. There is slight difference between the themes for the 2 versions of ST. You will have to deleted theme3to2.py afterwards, otherwise ST will consider it as a plugin.*
