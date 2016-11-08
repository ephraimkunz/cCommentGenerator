# cCommentGenerator
Good old ECEN 330 - Embedded Programming makes us have 90% comment coverage. This should get the easy cases.

# Options:
* Run with `python generateComments.py` from the command line.
* The following options can follow this basic command:
  * No options. All `.h` and `.c` files in the directory will have a new file created with the default postfix that contains the inserted comments.
  * `filename.h` or `filename.c`. A copy of this file only will be commented witht default postfix.
  * `inputfilename.h1` or `.c`, `outputfilename.h` or `.c`. The output file name will be used to name the copy with the comments inserted.
