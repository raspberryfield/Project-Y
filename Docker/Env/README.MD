## Docker Environment files

This folder contains files with **usernames** and **passwords** that are needed for various docker containers.

These files are ignored by gitignore. (You should never have passwords stored in a repository, even if they only are for test purpose.)

To make it easier to create all different files that are needed, there is a script for it: **create-docker-env.sh** .

Example:

    `$ ./create-docker-env.sh --help`
*Prints info about the script.*

    `$ ./create-docker-env.sh --user <valid@email.com> --password <my_secret>`
How to create the files.

    `$ ./create-docker-env.sh --user <valid@email.com> --password <my_secret> --overwrite`
Use the [optional] overwrite flag to overwrite already existing files.

> NOTE! You might need to give the script execution permission. You can do it as this:
>    `$ chmod +x  create-docker-env.sh`
> To see permissions, use:
>    `$ ls -al [<file name>]`
