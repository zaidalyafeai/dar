# datasets_auto_wrapper

The main script can be ran using the following commands 

```bash
python src/main.py
```

## Arguments 
`--pal`: this argument is used for datasets that have labels as part of the foulder/file names. Upon 
choosing this command the use is prompted to enter the `levels` which represents an integer that is used to extract the labels names from the full path. For example in `base_path/label/**.txt`, we define leveels = -2 which means that `label` will be given for all the files inside the label foulder. We can also define `base_path/label.txt` with levels = -2 which will remove the file extension `.txt`. 

## Supported Links Types 
Mainly after entering the dataset name, the user will be prompted to enter the dataset link. The user can either enter one link or mutliple links separated by comma. The supported links are the following 

* `GitHub` The user can enter a link from GitHub without using `raw` as it will be converted automatically. The user can also either choose to enter a link to the repository in the following format `https://github.com/user/repo` which will download and extract the full directory or `https://github.com/user/repo/foulder` which will download all the files from that foulders as individual links. 
* `Google Drive` The user can also enter a link from google drive in the following form `https://drive.google.com/file/d/id/view` which will directly download and extract the foulder to the local disk. 
* `Direct links` The user can enter direct links for files i.e `https://domain/**.ext` with any extension and the file will be downloaded. Multilple lins can be concatenated using comma `https://domain/file1.ext,https://domain/file2.ext,...,https://domain/filen.ext`

## Filteration
The user can use glob structures to filter out some files from being used in the dataset. For example, the user is prompted with `Enter a glob structure: ` the user can enter something like `glob('foulder/**.txt')` which will only extract `.txt` files from the chosen `foulder`. The user will be prompted to enter multiple glob structures unless an empty `Enter` key is pressed. 

## Supported file types
Mainly the user will enter the file type when asked for `Enter the type:`, the supported file formats can be only one of the following 

* `txt` mainly for reading the file as a whole or separated by lines. To differentiate between such options the user enters `set lines (y/n) ?` which if `y` the file will be separated into multiple lines or if `n` it will be read as a whole. 
* `csv` this is used for files with sepcial separator, for example `.tsv` and `.txt` can be part of such family if a special separator is used. The program will try to guess the best separator but the user can also choose the separator using the command `Set a separator for {csv}`. The user can enter the separtors as `\t`,`,`,`;`,`|`, etc.
* `json` can be used for dictionary like files. The use can choose `set lines (y/n) ?` as well which will decide whether to split the file by new lines or read the file as a whole. Also some datasets can have a parent dictionary for example `{'data':{'col1': [...], 'col2': [...]}}`, to support that the user can `set json key: ` whcih is `data` in this example. 
* `xml` can be used for files that contain tags, for example `html` files as well. The user will be prompted to enter the column names for example `<s>this is good</s><l>positive</l> .....` then upon getting the prompt `enter the columns: ` the user can choose `s,l` such tags as columns. 
* `wav` this is used for audio files like `.mp3,.wav` files. Upon choosing that the program will automatically create the following features as columns `{'path':path_to_file, 'audio':np.array(...)}`

## File Processing 
All the files will be processed using `pandas`. The user can modify some contents when prompted to 

* `Enter rows to skip: ` this is used to skip some lines from the beginning of all the files. Mainly used to remove some metadata that is usually put as the header of files. The user can enter `0` which indicates that no lines will be skipped. 
* `Data has a column? (y/n)` used to deal with files that have no column names, the user can set that `n` and enter the column names in the next step. 
* `Enter new columns separated by comma:` used to creat different names for the columns or add columns if non exist. 
* `Enter label column name:` used to choose the column that contains the labels. For example in sentiment anlaysis we will have the contents in a column as `positive` or `negative`. The user can put the name of that column to recognize that as the label. `datasets` will convert that to an integer which can be easily procssed by nlp model pipleines. 
* `push to hub:` used to upload the dataset to hub. 

