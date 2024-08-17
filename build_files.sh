
echo "BUILD START"
# Install the required packages from requirements.txt
python3.10 -m pip install -r requirements.txt
# Collect static files and clear out the existing ones
python3.10 manage.py collectstatic --noinput --clear
echo "BUILD END"
