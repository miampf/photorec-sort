# photorec-sort.py

This is a python script that's supposed to sort the output of [PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec) by file types and size.

For that, it will create a folder structure that will be similair to this one:

```text
mp4
|__ 0_1
    |__ file.mp4
```

To use it, you need python installed, then run

```sh
python photorec-sort.py <SIZE_INCREASE> <PHOTOREC_FOLDER> <OUTPUT_FOLDER>
```

where `SIZE_INCREASE` is the size difference for sorting in GiB (in the folder structure above, this would correspond to a 1, since the subfolder is `0_1`, so 0-1 GiB), `PHOTOREC_FOLDER` is the folder of the PhotoRec recovery and `OUTPUT_FOLDER` is the folder where the new sorted filesystem will be generated and the files will be moved.

Note that the files of the `PHOTOREC_FOLDER` will be MOVED into the `OUTPUT_FOLDER`, not copied.
