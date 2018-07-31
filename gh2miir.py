#!/usr/bin/env python3
#coding: utf-8
'''
fork 使う方が早いかも (何故？)
data.jsonにはサンプルデータ
Environment variables:
MIIR_IP
MIIR_TOKEN
MQTT_TOKEN
data.json
device: none は性質上Google Assistant で使うないデバイス名を使用時
'''
import json
import sys
import ipaddress
from typing import Any
from miio import ChuangmiIr,DeviceException
import time
import os.path
import paho.mqtt.client as mqtt
import json
import os
import re

ip = os.environ['MIIR_IP']
token = os.environ['MIIR_TOKEN']
TOKEN = os.environ["MQTT_TOKEN"]
HOSTNAME = 'mqtt.beebotte.com'
PORT = 8883 #SSLの場合は8883, そうでない場合は1883
CA_CERTS = 'mqtt.beebotte.com.pem'
TOPIC = 'IFTTT_RaspberryPi_IR/IRSignal'

ir =  ChuangmiIr(ip,token)
f = open('data.json', 'r')
devices = json.load(f)
f.close()

def check_or(message, orList):
    for ckWord in orList:   #orList
        if ckWord in message:    return True
        else: continue
    return False

def check_and(message, andList):
    for ckWord in andList:  #andList
        if ckWord in message:    continue
        else: return False
    return True

def check_num(ckStr):
    for i in ckStr:
        if i.isdigit():
            print("True")
            return True
    print("False")
    return False

def send_ir(device, message):
    if device in devices.keys():            #デバイス名
        for tmp in devices[device].keys():  #tmp: ON OFF
            if(len(devices[device][tmp]["andList"]) > 0):
                if(not check_and(message, devices[device][tmp]["andList"])): continue   #コマンド切替
            if(check_or(message, devices[device][tmp]["orList"])):
                if "回" in message:
                    try:
                        repeatNum = re.search(r'(\d+)回', message.replace(" ", "")).groups()
                        if len(repeatNum) == 1: repeatNum = int(repeatNum[0])
                    except: repeatNum = int(1)
                else: repeatNum = int(1)
                for i in range(repeatNum):
                    ir.play(devices[device][tmp]["command"])
                    time.sleep(0.5)
                #sys.exit()
            else:   continue

# 接続中処理
def on_connect(client, userdata, flags, respons_code):
    print('status {0}'.format(respons_code))
    client.subscribe(TOPIC)

# メッセージ受信時
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode("utf-8"))["data"][0]
    print(data["device"])
    print(data["message"])
    if "終了" in data["message"]:
        client.disconnect()
    else:
        send_ir(data["device"], data["message"])
        '''
        if (os.fork() == 0):    send_ir(data["device"], data["message"])
        else:   os.wait()
        '''

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("token:%s"% TOKEN)
    client.tls_set(CA_CERTS)
    client.connect(HOSTNAME, port=PORT, keepalive=60)
    client.loop_forever()