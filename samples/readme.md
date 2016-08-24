#firmata_sample.py

##Description
Arduinoのdigital IOピンを使ってサーボを制御する場合のサンプルプログラムです。

##Requirement
* ArduinoにはあらかじめFirmata/ServoFirmataのスケッチを書き込んでおく必要があります。
* サンプルプログラムのソース内に記述されたArduinoのデバイスファイル名を、実際の環境にあわせた適切なものに変更してから使ってください。

##Usage
1. python firmata_sample.py で起動します。エラーが出ていないことを確認してください。
2. ServoDesignerを起動します。
3. 共有メニューからJoin Meshを選び、127.0.0.1 と入力してOKを押してください。
4. サーボスプライトを作成して、適当なサーボ値を設定し、'servo changedを送る'を押してください。

##Circuit
![firmata_sampleで利用した回路例](https://raw.githubusercontent.com/wiki/EiichiroIto/ServoDesigner/images/firmata_sample.png)
