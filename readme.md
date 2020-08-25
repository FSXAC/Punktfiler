## Aliases

The aliases are stored as a dictionary object in Python
in the file `aliases.py`. To "compile" it into whatever shell aliases dotfiles, run the script `build_aliases.py`:

```shell
python3 build_aliases.py
```

Then an interactive menu/set up will do the rest. The output files will be in `output/`, one can then copy the files from this folder to the user root folder (`~`).

