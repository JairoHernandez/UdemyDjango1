import os

print(os.path.abspath(__file__))
# /home/jairomh/WORK/django/UltimateBeginner1.11/piglatin/BASEDIR.py

# Where manage.py and app(s) lives.
print(os.path.dirname(os.path.abspath(__file__))) # parent folder
# /home/jairomh/WORK/django/UltimateBeginner1.11/piglatin

# BASE_DIR where project lives.
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # parent of parent folder
# /home/jairomh/WORK/django/UltimateBeginner1.11

print(__name__) # __main__