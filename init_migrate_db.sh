#!/bin/bash
set -e

python manage.py makemigrations
python manage.py migrate
if [[ $? -ne 0 ]]; then
    echo "Couldn't load migrations into DB."
    exit 1
fi
if [[ ! -f templateMigrationData.lock && $1 -eq "--load-template-data" ]]; then
    python manage.py loaddata templateMigrationData.json
    now="$(date)"
    echo "templateMigrationData loaded at $now" > templateMigrationData.lock
else
    echo "Unable to load templateMigrationData.json as already loaded once:"
    cat templateMigrationData.lock
    echo "Reloading would result in losing all generated data in the DB."
fi
