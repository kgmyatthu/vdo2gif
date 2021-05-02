![python version](https://img.shields.io/badge/python-3.8-blue)
![pip moviepy](https://img.shields.io/badge/pip-moviepy-blue)

# What is this
  vdo2gif is a command line tool convert to video file into gif. I find myself opening video editing software just to do simple gif which i use to show example in my readme.md on github. The tool is compitable with any python3 compitable system. Tested on windows 10 and linux-debian x86 machines.
### Features
 - custom fps, speed, size.
 
# Installation
  Install python3
  ```
  root@kali:~# sudo apt-get install python3
  ```
  After cloning this repo in your system, open terminal inside the repo directory and do
  ```
  root@kali:~# sudo python3 -m pip -r requirement.txt
  ```
  Above command line Install the python required python modules to run the vdo2gif.py
  
 # Usage
 ### Converting the whole video file
 To convert the whole video file to gif
 ```
 usage: python3 vdo2gif.py /path/to/input.mp4 /path/to/output.gif 
 ```
 example:
 
 ![image1](./example/example1.gif)
 
 
 ### Converting only a part of the video file
  ```
 usage: python3 vdo2gif.py /path/to/input.mp4 /path/to/output.gif -t hr:min:sec hr:min:sec 
 ```
  example:
  
 ![image1](./example/example2.gif)
  
  # REMINDER TO MYSELF ::
  -
