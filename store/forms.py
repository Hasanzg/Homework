from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['movie_id', 'movie_title', 'actor1_name', 'actor2_name', 'director_name', 'movie_genre', 'release_year','DurationMinutes', 'Country', 'Rating']

'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            '''