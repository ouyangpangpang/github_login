#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:09:25 2018

@author: oyc
"""

import requests
from lxml import etree

class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/login',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.session = requests.Session()
        
    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div[@id="login"]//input[2]/@value')
        #print(token)
        return token
    
    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token()[0],
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)
        '''
        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)
        '''
    
    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[@class="container"]//div[@id="dashboard"]//div[@class="dashboard-sidebar column one-third pr-5 pt-3"]//div[@class="Box-body"]//ul//li//div//a/@href')
        print(dynamics[0])
        
        
    

    
if __name__ == "__main__":
    login = Login()
    login.login(email='', password='')
    #login.token()