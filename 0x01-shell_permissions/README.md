su betty -switches the current user to the user betty
whoami - prints the effective username of the current user
groups -prints all the groups the current user is part of
chown betty hello -changes the owner of the file hello to the user betty
touch hello -creates an empty file called hello
chmod u+x hello - adds execute permission to the owner of the file hello
chmod 754 hello -adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.
chmod 751 hello - adds execution permission to the owner, the group owner and the other users, to the file hello
chmod 007 hello -sets the permissions for the file hello as follows: owner with no permissions, group with no permissions, and other users with all permissions
chmod 753 hello -sets the mode of the file hello to -rwxr-x-wx
chmod "$$(state -C "%a" olleh)" hello -sets the mode of the file hello the same as olleh’s mode
find . - type d -exec chmod 755 {}\; -execute permission to all subdirectories of the current directory for the owner, the group owner and all other users
mkdir my_dir chmod 751 my_dir -creates a directory called my_dir with permissions 751 in the working directory
chgrp school hello -changes the group owner to school for the file hello
