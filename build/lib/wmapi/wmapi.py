# -*- coding: utf-8 -*-
import requests
import subprocess
from shutil import copyfile
import uuid
import xmltodict
import os
import json

class WMAPI(object):

    def __init__(self, client_id, private_key, channel_type):
        self.client_id = client_id
        self.private_key = private_key
        self.channel_type = channel_type
        self.url = "https://marketplace.walmartapis.com/v3"
        self.headers = {
            "WM_SVC.NAME": "Walmart Marketplace",
            "WM_QOS.CORRELATION_ID": uuid.uuid4().hex,
            "WM_CONSUMER.CHANNEL.TYPE": self.channel_type,
            "WM_CONSUMER.ID": self.client_id,
            "WM_TENANT_ID": "WALMART.CA",
            "WM_LOCALE_ID": 'en_CA',
            "Accept": "application/xml",
            "Content-Type": "application/x-www-form-urlencoded",
        }

    def send_request(self, method, path, params=None):
        url = self.url + path
        timestamp, auth_signature = self.get_auth(url)
        headers = self.headers
        headers.update({
            'WM_SEC.TIMESTAMP':timestamp,
            'WM_SEC.AUTH_SIGNATURE':auth_signature
            })
        if method == 'GET':
            response = requests.get(url, params=None, headers=headers)
        elif method == 'DELETE':
            response = requests.delete(url, params=None, headers=headers)
        elif method == 'POST':
            response = requests.post(url, params=None, headers=headers)

        return json.loads(json.dumps(xmltodict.parse(response.content)))

    def get_auth(self, url):
        d = os.path.dirname(os.path.realpath(__file__))+'/'
        copyfile(d+'walmart.jar', d+'walmart_copy.jar')
        process = subprocess.Popen(['java', '-jar', d+'walmart.jar', 'DigitalSignatureUtil', url, self.client_id, self.private_key, 'GET', d+'walmart.jar'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        ret = []
        while process.poll() is None:
            line = process.stdout.readline().decode('utf-8')
            if line != '' and line.endswith('\n'):
                ret.append(line[:-1])
        copyfile(d+'walmart_copy.jar', d+'walmart.jar')
        return ret[1].replace('WM_SEC.TIMESTAMP:','').strip(), ret[0].replace('WM_SEC.AUTH_SIGNATURE:','').strip()

class Items(WMAPI):
    
    def get_all_items(self):
        return self.send_request('GET', '/ca/items')

    def get_an_item(self, sku):
        return self.send_request('GET', '/ca/items/'+sku)

    def retire_an_item(self, sku):
        return self.send_request('DELETE', '/ca/items/'+sku)

    def upload_items(self, filepath):
        return self.send_request('POST', '/feeds')

