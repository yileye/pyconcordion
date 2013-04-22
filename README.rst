**This is no longer maintained. I am currently working on https://github.com/johnjiang/pyconcordion2 which is a pure python impementation of concordion.**

***************
pyconcordion
***************

Python port of concordion. Based on work by Jean-Christophe Plessis.
`http://code.google.com/p/pyconcordion/ <http://code.google.com/p/pyconcordion/>`_

Installation
******************

1. Download as zip, extract
2. Run: ``python setup.py install``

Usage
******************

``$ concordion_runner <path>``

Notable Differences
******************

1. Uses concordion 1.4.2 instead of 1.4.1
2. Has a single script to support both executing of folders and individual files
3. Server side exceptions are captured in the output for easy debugging
