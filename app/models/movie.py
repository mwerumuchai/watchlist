class Movie:
    '''
    Movie class to define Movie objects
    '''

    def __init__(self,id, title,overview,image,vote_average,vote_count):
        self.id = id
        self.title = title
        self.overview = overview
        self.image = 'https://developers.themoviedb.org/3/getting-started/images'+image
        self.vote_average = vote_average
        self.vote_count = vote_count
