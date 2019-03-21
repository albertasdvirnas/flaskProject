# This is a readme file for the project analizing 
# Non discriminatory barcodes

# Simple way to run the project is
conda create env -f env.yml
source activate projenv

# And then we need to set up flask:
export FLASK_APP=flaskr
export FLASK_ENV=development
# And initiate database to store user data
flask init-db
# Now we run flask
flask run

# Finally, open the following url in web-browser
firefox http://127.0.0.1:5000/

# Folder structure:
