#!/bin/bash

# cleans out all the temporary files
PROJECT_ROOT=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )/..
cd $PROJECT_ROOT
rm -f `find -iname *~`
rm -f `find -iname .pyc`
rm -rf `find -iname __pycache__`
