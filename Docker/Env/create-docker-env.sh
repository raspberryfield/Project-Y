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
  echo "Usage: $0 -u <my@example.com> -p <my_password> [-o]"
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


#CREATE ENVIRONMENT FILES

file_suffix="-variables.env"

## If new env file, add function here, also add function name to env_files array.
## name the function as you want the first part of the file to be named.
function dummy {
 # -n no trailing new line feed.
 echo -n "" > ${FUNCNAME[0]}$file_suffix # > create if not exists else overwrite, >> append.
 echo "<Your content goes here>" >> ${FUNCNAME[0]}$file_suffix
 echo "[INFO] - file: '${FUNCNAME[0]}$file_suffix' created."
}
function postgres {
 echo -n "" > ${FUNCNAME[0]}$file_suffix
 echo "POSTGRES_PASSWORD=$password" >> ${FUNCNAME[0]}$file_suffix
 echo "[INFO] - file: '${FUNCNAME[0]}$file_suffix' created."
}
function pgadmin {
 echo -n "" > ${FUNCNAME[0]}$file_suffix
 echo "PGADMIN_DEFAULT_EMAIL=$user" >> ${FUNCNAME[0]}$file_suffix
 echo "PGADMIN_DEFAULT_PASSWORD=$password" >> ${FUNCNAME[0]}$file_suffix
 echo "PGADMIN_LISTEN_ADDRESS=0.0.0.0" >> ${FUNCNAME[0]}$file_suffix
 echo "PGADMIN_LISTEN_PORT=80" >> ${FUNCNAME[0]}$file_suffix
 echo "[INFO] - file: '${FUNCNAME[0]}$file_suffix' created."
}
function mysql {
 echo -n "" > ${FUNCNAME[0]}$file_suffix
 echo "MYSQL_ROOT_PASSWORD=$password" >> ${FUNCNAME[0]}$file_suffix
 echo "[INFO] - file: '${FUNCNAME[0]}$file_suffix' created."
}
## add new env file to this array.
env_files=(postgres pgadmin mysql)

## loop files to create
for file in ${env_files[@]}
 do
  filename=$file$file_suffix
  if [ -e $filename ] && [ ! -w $filename ] # -e exists, -w writable
   then
    echo "[WARNING] - file '$filename' is not writable."
    echo "Change permission with $ chmod +w <filename> and run script again."
    continue
  fi
  if [ $overwrite = "true" ]
   then
    eval $file
    continue
   else
    if [ -f $filename ] # check if file already exists
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

