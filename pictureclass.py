import webbrowser
class jesusmovies:
    def __init__(self,title,story_line,img_url,trailer_url):
        self.title=title
        self.story=story_line
        self.image=img_url
        self.trailer=trailer_url
    def trailer(self):
        webbrowser.open(self.trailer)
