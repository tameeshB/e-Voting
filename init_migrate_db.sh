#!/bin/bash
set -e

python manage.py makemigrations
python manage.py migrate
if [[ $? -ne 0 ]]; then
    echo "Couldn't load migrations into DB."
    exit 1
fi
if [ $1 == "--load-template-data" ]; then
    if [[ ! -f /evoting/templateMigrationData.lock ]]; then
        python manage.py loaddata /evoting/templateMigrationData.json
        now="$(date)"
        echo "templateMigrationData loaded at $now" > /evoting/templateMigrationData.lock
        echo "Loaded templateMigrationData.json data into DB."
    else
        echo "Unable to load templateMigrationData.json as already loaded once:"
        cat /evoting/templateMigrationData.lock
        echo "Reloading would result in losing all generated data in the DB."
    fi
else
    echo "Not loading tempalte data. Use '--load-template-data'."
fi
