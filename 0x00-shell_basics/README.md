#!/bin/bash – Execute the file using the Bash shell
pwd -It shows the name of working directory
ls -Display the contents list of your current directory
cd ~ -Change the working directory to the user's home directory
ls -l -Display current directory contents in a long format
ls -la -Display current directory contents, including hidden files in long format
ls -aln -Display current directory contents in long format with user and group IDs displayed numerically, and hidden files (starting with . ) 
mkdir /tmp/my_first_directory -create a directory named my_first_directory in the /tmp/ directory:
mv /tmp/betty /tmp/my_first_directory/ - move the file betty from /tmp/ to /tmp/my_first_directory
rm /tmp/my_first_directory/betty -delete the file betty located in /tmp/my_first_directory
rm -r /tmp/my_first_directory -delete the directory my_first_directory located in /tmp
cd - -changes the working directory to the previous one
ls -al . ../ /boot -lists all files (even hidden ones) in the current directory, parent of the working directory, and /boot directory in long format
file /tmp/iamafile -prints the type of the file named iamafile located in the /tmp directory
ln -s /bin/ls __ls__ - create a symbolic link to /bin/ls named __ls__ in the current working directory
copy _html cmd -copies all .html files
