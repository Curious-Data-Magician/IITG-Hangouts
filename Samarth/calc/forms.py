from django import forms 


GENDER_CHOICES =(
    (1, "Male"),
    (2, "Female")
)
     
SOCIAL_MEDIA =(
    (1, "Not At all"), 
    (2, "Ocassionaly"),
    (3, "Quite Often"),
    (4, "Quite Frequently"),
    (5, "Very Much")
)

VALUED_INTELLIGENCE =(
    (1, "Creative"), 
    (2, "Logical"),
    (3, "Interpersonal")
)

FREE_TIME =(
    (1, "Sports"),
    (2, "E-Games"), 
    (3, "Reading"), 
    (4, "Travelling"), 
    (5, "Watching Movies and TV-Series"),
    (6, "Sleeping")
)

IDEAL_VACATION =(
    (1, "Adventure in Leh"),
    (2, "Chilling out in Goa"), 
    (3, "Netflix at home"),    
)

MOVIE_GENRE =(
    (1, "Drama"),
    (2, "Comedy"), 
    (3, "Horror"), 
    (4, "Romance"), 
    (5, "Mystery"),
    (6, "Other")
)

INTROVERSION =(
    (1, "I Don't Really like to Mingle"),
    (2, "I face problems mingling with people"), 
    (3, "I'm sometimes social"), 
    (4, "I'm usually social"), 
    (5, "I can talk to anyone")
)

DRESSING_SENSE =(
    (1, "I am usually in a casual and decent dress"),
    (2, "I can go to lectures in shorts"), 
    (3, "I like to dress well and sophisticated")
)

COMPELLING_FACTOR =(
    (1, "Star Cast"),
    (2, "Rating and Reviews"), 
    (3, "Genre Of the Movie"), 
    (4, "Other"), 
)

REJECTING_FACTOR =(
    (1, "Star Cast"),
    (2, "Rating and Reviews"), 
    (3, "Genre Of the Movie"), 
    (4, "Other"), 
)

SUB_DUB =(
    (1, "Orignal"),
    (2, "With Subtitles"), 
    (3, "Dubbed")
)

MOVIES =(
    ("Ford v Ferrari", "Ford v Ferrari"),
    ("Alita: Battle Angel", "Alita: Battle Angel"), 
    ("Midsommar", "Midsommar"), 
    ('Article 15', "Article 15"), 
    ("Uri: The Surgical Strike", "Uri: The Surgical Strike"),
    ("K.G.F: Chapter 1", "K.G.F: Chapter 1"),
    ("Dear Zindagi", "Dear Zindagi"),
    ("M.S. Dhoni: The Untold Story", "M.S. Dhoni: The Untold Story")
)

class UserForm(forms.Form):
    Name = forms.CharField(max_length=100, label='Name')
    Age = forms.IntegerField(required=True, label='Age')
    Gender = forms.MultipleChoiceField(choices =GENDER_CHOICES, label="Gender")
    Social_media = forms.MultipleChoiceField(choices =SOCIAL_MEDIA, label="How often do you use Social Media?",)
    Intelligence = forms.MultipleChoiceField(choices =VALUED_INTELLIGENCE, label="What type of intelligence do you value most?",)
    Free_time = forms.MultipleChoiceField(choices =FREE_TIME, label="How do you like to spend your free time?",)
    Ideal_vacation = forms.MultipleChoiceField(choices =IDEAL_VACATION, label="What is your Ideal vacation like?",)
    Genre = forms.MultipleChoiceField(choices =MOVIE_GENRE, label="Which Movie Genre do you prefer to watch?",)
    Introversion = forms.MultipleChoiceField(choices =INTROVERSION, label="How easily do you mingle with people?",)
    Dressing_sense = forms.MultipleChoiceField(choices =DRESSING_SENSE, label="How important is dressing and grooming in your life?",)
    Compelling = forms.MultipleChoiceField(choices =COMPELLING_FACTOR, label="Which factor compels you the most to watch a movie?",)
    Rejecting = forms.MultipleChoiceField(choices =REJECTING_FACTOR, label="Which factor compels you the most to reject a movie?",)
    Sub_dub = forms.MultipleChoiceField(choices =SUB_DUB, label="How do you like to watch a movie?",)
    Movies_select = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                    choices=MOVIES, label="Your Preferred Movies", required=False)