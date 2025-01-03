from django.shortcuts import render, redirect

class Fav():
    def __init__(self, request):
        self.session = request.session
        
        fav = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            fav = self.session['session_key'] = {}
            
        self.fav = fav 
        