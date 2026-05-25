---
title:     "Comparing Two Excel Files with Openpyxl"
date:      2014-08-28 10:31:08
zhUrl: /compare-excel-using-openpyxl
aliases:
  - /compare-excel-using-openpyxl-en
---

## Background

Recently I keep having to do Excel report comparison work, so I wanted to write a small Python script to do this job.
For Python Excel processing, I had only used the xlrd library before, which handles Office03 .xls files.
Writing this little tool is also an opportunity to learn something new.

<!--more-->

## Preparation

Since the reports to be compared this time are Office07 .xlsx files, I searched online for the best Python approach.
After reading a few articles, I settled on Openpyxl (see the link below:)

>[Four tools for processing Excel in Python][4toolForPythonExcel]

So next was installing Openpyxl. I followed the process on the official site:

>[A Python Library: Openpyxl][Openpyxl]

Since the source code was pulled from BitBucket, I also installed SourceTree along the way.
I heard SourceTree also has Git-related features, I can try it out next time.


## Using Openpyxl

Once Openpyxl is installed you can just import and use it:

```python
from openpyxl import *
```

Openpyxl also provides a really nice tutorial~~(a bit too simple~~

>[Openpyxl Tutorial][OpenpyxlTutorial]

Openpyxl also has a downside in that its docs aren't very detailed, you can only dig through the source code.


## Final Code

You can find my version in the PythonScripts I wrote:

[PythonScripts - ExcelComparer][ExcelComparer]

[4toolForPythonExcel]:https://www.gocalf.com/blog/python-read-write-excel.html
[Openpyxl]:https://pythonhosted.org/openpyxl/
[OpenpyxlTutorial]:https://pythonhosted.org/openpyxl/tutorial.html
[ExcelComparer]:https://github.com/LKI/PythonScripts/tree/master/ExcelComparer
