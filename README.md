This program runs on at least Python 3.7
The order of commands for this program are:
python dirwatcher.py (-e, --ext [extension]{.txt}) (-i, --interval [interval]{2}) [directory] [magic key-phrase]
    where the directory is the directory path the program will
    search for, even notifying you if it does not exist yet,
    and the magic key-phrase is the phrase that will trigger the
    program to point to a file that has that phrase.

    The optional arguments in the parenthesis; extension is the 
    file extension to look out for. If none is given, .txt is the
    assumed extension, all other files are excluded.
    Interval is the interval between looking for the directory/
    files/phrase. The default is two seconds

It works by first checking if the given path and directory exists.
When it finds the directory, it lists the files and read the lines
until it finds the key. If a key is found, the program tells you which file has the key, and then exits. Else, it starts over