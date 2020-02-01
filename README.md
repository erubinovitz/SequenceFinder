# SequenceFinder
Web project with Django backend and JS frontend to search for certain substrings of DNA Sequences.

This program allows the user to input a substring. The site checks its list of known dna sequences (check dnaSequenceFinder/homePage/proteinList.txt )
and sees if the string that the user inputted is a substring if any of these sequences. If it is, it returns the full string, along with
the index that it was found. If not, it informs the user that no matching strings were found. 

On the front page, the user can see all  searches that he or she has made, with the searches sustaining even if the windows are closed. The user can also go to the search history page to see all searches made by all users, 
along with the proper information. These searches are stored on the server and as such will sustain regardless of cookies, and will not be lost on restart.

To run, cd to SequenceFinder/dnaSequenceFinder in your command prompt, and enter
```
$ python manage.py runserver
```
If Django is not installed, be sure to run 
```
$ pip install Django
```
beforehand.
