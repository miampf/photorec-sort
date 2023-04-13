# photorec-sort.py

This is a python script that's supposed to sort the output of [PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec) by file types and size. However, it should be able to recursively sort any folder by filetype and size.

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

## Example

Imagine you have the following folder structure:

```txt
test
├── asdf
│   ├── 1.txt
│   └── 2.txt
├── something
│   └── 1.png
└── uwu
    ├── 1.exe
    └── 2.bat
```

Here, `1.txt`, `2.txt` and `1.exe` are 1 GiB large, `2.bat` is 4 GiB large and `1.png` has a size of 2 GiB. If you now run `python photorec-sort.py 1 ./test ./out`, the `out` folder has the following structure:

```txt
out
├── bat
│   └── 3_4
│       └── 2.bat
├── exe
│   └── 0_1
│       └── 1.exe
├── png
│   └── 1_2
│       └── 1.png
└── txt
    └── 0_1
        ├── 1.txt
        └── 2.txt
```
