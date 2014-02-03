# -*- coding: utf-8 -*-
from tori.controller           import Controller
from tori.decorator.controller import renderer

@renderer('messenger.view')
class Home(Controller):
    def get(self):
        self.render('index.html')
