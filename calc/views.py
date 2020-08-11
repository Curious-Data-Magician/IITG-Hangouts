from django.shortcuts import render 
from .forms import UserForm
from django.http import HttpResponse
from .matcher import Ret_Name
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

# Create your views here.
NAME = []
AGE = []
GENDER = []
SOCIAL_MEDIA = []
INTELLIGENCE = []
INTROVERSION = []
FREE_TIME = []
IDEAL_VACATION = []
GENRE = []
DRESSING_SENSE = []
COMPELLING = []
REJECTING = []
SUB_DUB = []
length = 0
matches = []
MOVIE_CHOICE = []

# DATAFRAME = pd.DataFrame(data={'NAME':NAME, 'AGE';AGE, 'GENDER';GENDER, 'SOCIAL_MEDIA';SOCIAL_MEDIA, 
#                                 'INTELLIGENCE';INTELLIGENCE, 'INTROVERSION';INTROVERSION, 'FREE_TIME';FREE_TIME, 
#                                 'IDEAL_VACATION';IDEAL_VACATION, 'GENRE';GENRE, 'DRESSING_SENSE';DRESSING_SENSE, 
#                                 'COMPELLING';COMPELLING, 'REJECTING';REJECTING, 'SUB_DUB';SUB_DUB})


# Any results you write to the current directory are saved as output.
def recommendation_system(movie_user_2,movie_user_1):

    df =pd.read_csv('clean_movies.csv')
        

    df1 = df.copy()
    from sklearn.feature_extraction.text import TfidfVectorizer
    tfidf_vectorizer = TfidfVectorizer()

    from sklearn.metrics.pairwise import cosine_similarity
    tfidf = tfidf_vectorizer.fit_transform(df1["details"])

    import operator

    movies=list(df["Title"])
    #years=list(df["Year"])

    movie_name=list(df1["Title"].to_numpy())

    def similar_func(movie_in_func):
        
        similarity={}
        for f in range(len(movies)):
            if movie_in_func == movies[f] :
                index=f

        for f in range(len(movies)):
            if f!=index:
                score= cosine_similarity(tfidf[index], tfidf[f]).astype("float")[0][0]
                similarity[f]=score

        similarity_sort=sorted(similarity.items(), key=operator.itemgetter(1),reverse=True)
        return(similarity_sort)

    def recommended_movies(movie_in):
        rating={}
        for f in range(len(movies)):
            rating[f]=[] 
            
        for f in range(len(movie_in)):
            
            movie_list = similar_func(movie_in[f])

            for x in range(len(movie_list)):
              rating[movie_list[x][0]].append(movie_list[x][1])

            for y in range(len(movies)):
              if movie_in[f] == movies[y] :
                index=y
    
        rating[index].append(-100)

        rating_sum={}                                            
        for f in range(len(movies)):
            rating_sum[f]= []
            
        for f in range(len(movies)):
            
            a= rating[f]
            sum_=0
            for x in range(len(a)):
                sum_ = sum_ + a[x]
  
            rating_sum[f] = sum_

        similarity_sort=sorted(rating_sum.items(), key=operator.itemgetter(1),reverse=True)
        return similarity_sort

    #movie_user_1=['Badla','Super 30','Article 15'] 
    #movie_user_2=['Article 15','Kesari','Andhadhun']

    user1=recommended_movies(movie_user_1)
    user2=recommended_movies(movie_user_2)

    u=1 #number of movies to be recommended

    def similar_movie(similarity_sort,similarity_sort1):
        list_of_movies=[]
        list_of_movies_index=[]
        r=0
        i=0
        for f in range(10,558,50):
            for x in range(r,f):
                for y in range(r,f):
                    if similarity_sort[x][0] == similarity_sort1[y][0] and i<u:
                        list_of_movies_index.append(similarity_sort[x][0])
                        i=i+1

            if i==3:
                break
            r=f
    
        list_of_movies = [movies[x] for x in list_of_movies_index]
        return list_of_movies

    movies_list = similar_movie(user1,user2)

    return(movies_list)
    
def matcher(DATAFRAME):
    data = DATAFRAME
    name = data.NAME
    
    data.GENDER = data.GENDER.astype(str).str.replace('[', '').str.replace(']', '')
    data.SOCIAL_MEDIA = data.SOCIAL_MEDIA.astype(str).str.replace('[', '').str.replace(']', '')
    data.INTELLIGENCE = data.INTELLIGENCE.astype(str).str.replace('[', '').str.replace(']', '')
    data.INTROVERSION = data.INTROVERSION.astype(str).str.replace('[', '').str.replace(']', '')
    data.FREE_TIME = data.FREE_TIME.astype(str).str.replace('[', '').str.replace(']', '')
    data.IDEAL_VACATION = data.IDEAL_VACATION.astype(str).str.replace('[', '').str.replace(']', '')
    data.GENRE = data.GENRE.astype(str).str.replace('[', '').str.replace(']', '')
    data.DRESSING_SENSE = data.DRESSING_SENSE.astype(str).str.replace('[', '').str.replace(']', '')
    data.COMPELLING = data.COMPELLING.astype(str).str.replace('[', '').str.replace(']', '')
    data.REJECTING = data.REJECTING.astype(str).str.replace('[', '').str.replace(']', '')
    data.SUB_DUB = data.SUB_DUB.astype(str).str.replace('[', '').str.replace(']', '')

    le = LabelEncoder()
    data_copy=data.drop(['AGE', 'NAME'],axis=1)
    for col in data_copy.columns:
        data_copy[col] = le.fit_transform(data_copy[col])
    data_copy['AGE'] = data['AGE']
    
    sc = StandardScaler()
    data_copy = sc.fit_transform(data_copy)
    data_copy = pd.DataFrame(data_copy)
    
    cosine = cosine_similarity(data_copy)
    cosine = pd.DataFrame(cosine)
    cosine.columns = name
    cosine['name'] = name
    cosine.set_index('name', inplace=True)
    
    for i in range(len(cosine)):
        for j in range(len(cosine)):
            if cosine.iloc[i, j] == cosine.iloc[j, i]:
                cosine.iloc[j, i] = -2
                
    matcher_arr = []
    for iters in range(len(cosine)//2):
        name1 ,name2 = cosine.max(axis=0).idxmax(), cosine.max(axis=1).idxmax()
        matcher_arr.append((name1, name2))
        cosine.drop(columns=[name1, name2], inplace=True)
        cosine.drop(labels=[name1, name2], axis=0, inplace=True)

    return matcher_arr

def home(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            name= form.cleaned_data.get("Name")
            age= form.cleaned_data.get("Age")
            gender= form.cleaned_data.get("Gender")
            social_media = form.cleaned_data.get("Social_media")
            intelligence = form.cleaned_data.get("Intelligence")
            introversion = form.cleaned_data.get("Introversion")
            free_time = form.cleaned_data.get("Free_time")
            ideal_vacation = form.cleaned_data.get("Ideal_vacation")
            genre = form.cleaned_data.get("Genre")
            dressing_sense = form.cleaned_data.get("Dressing_sense")
            compelling = form.cleaned_data.get("Compelling")
            rejecting = form.cleaned_data.get("Rejecting")
            sub_dub = form.cleaned_data.get("Sub_dub")
            movie_select = form.cleaned_data.get("Movies_select")
            
            # print(name, age, gender)
            NAME.append(name)
            AGE.append(age)
            GENDER.append(gender)
            SOCIAL_MEDIA.append(social_media)
            INTELLIGENCE.append(intelligence)
            INTROVERSION.append(introversion)
            FREE_TIME.append(free_time)
            IDEAL_VACATION.append(ideal_vacation)
            GENRE.append(genre)
            DRESSING_SENSE.append(dressing_sense)
            COMPELLING.append(compelling)
            REJECTING.append(rejecting)
            SUB_DUB.append(sub_dub)
            length = len(NAME)
            MOVIE_CHOICE.append(movie_select)

            DATAFRAME = pd.DataFrame(data={'NAME':NAME, 'AGE':AGE, 'GENDER':GENDER, 'SOCIAL_MEDIA':SOCIAL_MEDIA, 
                                'INTELLIGENCE':INTELLIGENCE, 'INTROVERSION':INTROVERSION, 'FREE_TIME':FREE_TIME, 
                                'IDEAL_VACATION':IDEAL_VACATION, 'GENRE':GENRE, 'DRESSING_SENSE':DRESSING_SENSE, 
                                'COMPELLING':COMPELLING, 'REJECTING':REJECTING, 'SUB_DUB':SUB_DUB})

            matches.append(matcher(DATAFRAME))
            # GENDER = np.array(GENDER).reshape(length)
            # SOCIAL_MEDIA = np.array(SOCIAL_MEDIA).reshape(length)
            # INTELLIGENCE = np.array(INTELLIGENCE).reshape(length)
            # INTROVERSION = np.array(INTROVERSION).reshape(length)
            # FREE_TIME = np.array(FREE_TIME).reshape(length)
            # IDEAL_VACATION = np.array(IDEAL_VACATION).reshape(length)
            # GENRE = np.array(GENRE).reshape(length)
            # DRESSING_SENSE = np.array(DRESSING_SENSE).reshape(length)
            # COMPELLING = np.array(COMPELLING).reshape(length)
            # REJECTING = np.array(REJECTING).reshape(length)
            # SUB_DUB = np.array(SUB_DUB).reshape(length)
            name_ = Ret_Name(NAME, AGE)
            print(length)
  
        return render( request, "return.html", { 'printname':name, 'length':length, 'printgender':AGE, 'printmatch': matches, 'printchoice': MOVIE_CHOICE})
    else:
        form = UserForm()  
        return render( request, "home.html", {'form':form})

def complete(request):
    matche = matches[-1]

    def movie_predictor(matche, NAME):
        recommended_movie = []
        for pair in matche:
            user1 = pair[0]
            user2 = pair[1]
            for i, namee in enumerate(NAME):
                if namee == user1:
                    user1_pos = i
                if namee == user2:
                    user2_pos = i
                else:
                    continue
            movie_user_1 = MOVIE_CHOICE[user1_pos]
            movie_user_2 = MOVIE_CHOICE[user2_pos]
            recommended_movie.append(recommendation_system(movie_user_2,movie_user_1))
        return recommended_movie
    list_of_movies = movie_predictor(matche, NAME)

    match1 = f'{matche[0][0]} and {matche[0][1]} and the movie for you is {list_of_movies[0][0]}'
    match2 = f'{matche[1][0]} and {matche[1][1]} and the movie for you is {list_of_movies[1][0]}'
    # match3 = f'{matche[2][0]} and {matche[2][1]} and the movie for you is {list_of_movies[2][0]}'
    # match4 = f'{matche[3][0]} and {matche[3][1]} and the movie for you is {list_of_movies[3][0]}'
    # match5 = f'{matche[4][0]} and {matche[4][1]} and the movie for you is {list_of_movies[4][0]}'
    # def final_matcher(matche, list_of_movies):
        
    #     for i in len(matche):
    #         user1 = matche[i][0]
    #         user2 = matche[i][1]
    #         movie_to_watch = list_of_movies[i][0]
            

    return render( request, "complete.html", { 'printname':NAME, 'printmatch': matche, 'match1':match1, 
                    'match2':match2})

 