#!/bin/bash

# NOTES
# ls -al ; see all files, even secret.
# chmod +x <my_bash_file>.sh ; make executable.
# ./<my_bash_file>.sh ; execute
# https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script
# ($@ build in variable to get arguments as array.)
# ($# build in variable to get numbers of arguments.)
# Use double quotes around variables when it can contain spaces or special characters,
#  avoids bash from splitting it.

# Variables.
$user
$password

# READ ARGUMENTS
## see if user wants help / no arguments passed.
if [ $# -eq 0 ] 
 then # print help message to user.
  echo "[ERROR] - no arguments passed."
  echo "Help: $0 --help"
  exit 1
elif [[ $1 == "--help" ]] || [[ $1 == "-h" ]]
 then
  echo "[HELP]"
  # echo -e enables to use \n and other special commands.
  echo "Usage: $0 -u <my@email.com> -p <my_password>"
  echo "Description: Creates docker environment files locally with user and password from this script."
  echo "-u, --user: Specify username (a valid email address)."
  echo "-p, --password: Your secret password."
  echo "-o, --overwrite: overwrites any already existing files."
  exit 1
fi #END help section.

# Read arguments for user and password.
for arg in $@
 do
  if [ $arg == "--user" ] || [ $arg == "-u" ]
   then
    user=$2
  elif [ $arg == "--password" ] || [ $arg == "-p" ]
   then
    password=$2
  fi
 shift 1 # shift index argument $2 >> $3. read +1 from arguments list compared with args.
done

# Check that user and password are assigned values. (-z check empty)
if [ -z $user ] || [ -z $password ]
 then
  echo "[ERROR] arguments not properly set."
  echo "Help: $0 --help"
  exit 1
fi

# Create files
#
postgres="postgres-variables.env"
pgadmin="pgadmin-variables.env"
#
files=($postgres $pgadmin)
for file in ${files[@]}
 do
  echo $file
 if [ -e $file ]
  then
   echo "File '$file' already exists."
   echo "Do you want to overwrite it?"
   echo -e "[y/n]: \c" # -e allows special commands. \c cursor stays on same line.
   read answer
   echo $answer
 fi
done

