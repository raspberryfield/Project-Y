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
overwrite=false

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
  echo "Usage: $0 -u <my@email.com> -p <my_password> [-o]"
  echo "Description: Creates docker environment files locally with user and password from this script."
  echo "-u, --user: Specify username (a valid email address)."
  echo "-p, --password: Your secret password."
  echo "-o, --overwrite: overwrites any already existing files. [optional]"
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
  elif [ $arg == "--overwrite" ] || [ $arg == "-o" ]
   then
   overwrite=true
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


# CREATE ENVIRONMENT FILES

file_suffix="-variables.env"

## if new env file, add function here, also add function name to env_files array.
function postgres {
 echo "call from postgres"
}
function pgadmin {
 echo "call from pgadmin"
}
## add new env file to this array.
env_files=(postgres pgadmin)

## loop files to create
for file in ${env_files[@]}
 do
  if [ $overwrite = "true" ]
   then
    eval $file
    continue
   else
    filename=$file$file_suffix
    if [ -e $filename ] # check if file already exists
     then
      echo "[INFO] - File '$filename' already exists."
      echo "Do you want to overwrite it?"
      echo -e "[y/n]: \c" # -e allows special commands. \c cursor stays on same line.
      read answer
      if [ $answer = "y" ]
       then
        eval $file
      elif [ $answer = "n" ]
       then
        echo "[INFO] - skipped '$filename'."
      else
        echo "[WARNING] - input not recognized. No action taken for '$filename'."
      fi
    else # file does not already exists
     eval $file
    fi
  fi
done

exit 1 # also good to use when troubleshooting.

# TODO:
# 4. Add user choice for overwrite in loop.
# 5. Append values to files.
# 6. CLEAN CODE!

