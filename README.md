gh2miir
====
## 簡単な説明
「安価に」擬似的なスマートホームを構築。  
Google Home シリーズや Amazon Echo シリーズでは家電の操作において細かいことができない（らしい）。  
例えば、エアコンは1台だけの登録しかできなかったり、2つ以上の機器を同時に点けることができない。前者の問題については照明に偽装して登録するという解決法が存在するが、後者の問題については機能改善待ちの状態である。使用言語が英語なら、一気に2つ以上の命令をすることができるそう……。  
カスタムスキルとスマートホームスキルとIFTTT  
一長一短  
スマートホームスキルはON / OFFだけ    
https://chasuke.com/alexa-remo-shome/  
という状況下で、使用言語が日本語であっても、赤外線リモコンを使用する家電（非スマート家電？）をある程度自由に操作できる仲介プログラムを作成（中）。  

## 目標
OK, Google / ねえ Google / Alexa / Clova 等（以下<ウェイクワード>）  
* (実装済) 照明を点けたいとき: 「<ウェイクワード> リビングの照明を点けて」  
* (未実装) エアコンが複数台あり、エアコン1を点けたいとき: 「<ウェイクワード> エアコン1を点けて」  
* (未実装) テレビとスピーカを点けたいとき: 「<ウェイクワード> リビングのテレビとスピーカを点けて」
* (未実装) レコーダを点けて、テレビの入力を変えたいとき: 「<ウェイクワード> リビングのレコーダを点けて、テレビの入力をHDMI1に変えて」  

上記の4種類

## 要求条件
* スマートスピーカ等 (Google Assistant が使用可能な端末でも可、Alexa はよく分からない)
* Xiaomi Universal IR Remote Controller (中国語のオリジナル名称: 小米万能遥控器)
* Python 3系列の実行環境 (Raspberry Pi 等)
* IFTTT (Web サービス連携ツール) のアカウント
* MQTTメッセージブローカー (例: Beebotte)
* paho-mqtt (MQTT クライアントライブラリ)
* python-miio (Xiaomi の製品を操作するための Python ライブラリ)



## 確認済み動作環境
<製作者環境>
* Google Home
* Xiaomi Universal IR Remote Controller
* Raspberry Pi 3B
  * Python 3 (Version)
  * paho-mqtt (Version)
  * python-miio (Version)
* IFTTT
* Beebotte



## 使い方
Python プログラム gh2miir をデーモン化し、常に起動して待機させておく。
http://singyestarday.hatenablog.com/entry/2018/03/07/131927

## FAQ
Q. スマートスピーカ用のスキル開発した方がいいのでは  
A. 自分の能力的な問題を論ずる前に、リアルタイム性に問題が……。  

Q. こんな ぷろぐらむに てこずっちゃって どうするの  
A. ｳｯ
