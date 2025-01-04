#!/bin/bash

#activates virtual environment
. ./venv/bin/activate

#
pytest
my_var=$?

if [[ $my_var -eq 0 ]]; then
    exit_code=0
else
    exit_code=1
fi

echo Exited status: $exit_code


