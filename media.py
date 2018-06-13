class Video():
    
    """
    This Class is a Parent Class that other Class Inheritance it
    like Movie, tvShow, tvSeries and shortMovie
    but in this project i only use class Movie and i made
    video class Because if i want to add tvShow, tvSeries and shortMovie
    
    Attributes:
        - title(str):       The title of the video 
        - duration(str):    The duration of the video
        - year(str):        Year of the video released
    """
    
    def __init__(self , title , duration , year):
        self.title = title
        self.duration = duration
        self.year = year

class Movie(Video):
    # this named in python 'documentation'
    """
    This Class To define The Movie Content and store the movie information
    and inheritance from class movie this attributes title, duration, year
    and has its own following attributes
    
     Attributes:
        - movie_story_line:     Story of movie in a short line
        - movie_poster_url:     ulr of movie poster
        - movie_trialer_url:    Url of the youtube trailer 
    """ 
    
    # this is a constructor
    def __init__(self , movie_name , movie_duration , movie_year 
                 , movie_story_line, movie_poster_url 
                 , movie_trialer_url):
        
        Video.__init__(self, movie_name, movie_duration, movie_year)
        
        # this is instance variable
        # self mean the instance i currently used for example if i use
        # instance named avatar will  be like that avatar.title = movie_name
        
        self.storyline = movie_story_line
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trialer_url