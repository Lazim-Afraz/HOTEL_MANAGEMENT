set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Install whitenoise for static files
pip install whitenoise

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input