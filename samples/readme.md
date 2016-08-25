#firmata_sample.py

##Description
Arduinoのdigital IOピンを使って2個のサーボを制御する場合のサンプルプログラムです。

##Requirement
* ArduinoにはあらかじめFirmata/ServoFirmataのスケッチを書き込んでおく必要があります。
* サンプルプログラムのソース内に記述されたArduinoのデバイスファイル名を、実際の環境にあわせた適切なものに変更してから使ってください。
* 2個以上のサーボを使う場合はサンプルを適宜修正してください。

##Usage
1. python firmata_sample.py で起動します。エラーが出ていないことを確認してください。
2. ServoDesignerを起動します。
3. 共有メニューからJoin Meshを選び、127.0.0.1 と入力してOKを押してください。
4. サーボスプライトを作成して、適当なサーボ値を設定し、'servo changedを送る'を押してください。

##Circuit
![firmata_sampleで利用した回路例](https://raw.githubusercontent.com/wiki/EiichiroIto/ServoDesigner/images/firmata_sample.png)

#i2c_sample.py

##Description
Raspberry piにi2cで接続したサーボドライバを使って2個のサーボを制御する場合のサンプルプログラムです。

##Requirement
* Adafruit_Python_PCA9685 パッケージが必要です。 ![Adafruit_Python_PCA9685](https://github.com/adafruit/Adafruit_Python_PCA9685)
* PCA9685を使った16ch 12bitのPWMサーボドライバが必要です。 ![使用したもの](https://www.amazon.co.jp/gp/product/B00WBYELB2/)
* サーボドライバのi2cアドレスはデフォルトとなっていますので、変更した場合は適切なものに変えてから使ってください。
* 2個以上のサーボを使う場合はサンプルを適宜修正してください。

##Usage
1. python i2c_sample.py で起動します。エラーが出ていないことを確認してください。
2. ServoDesignerを起動します。
3. 共有メニューからJoin Meshを選び、127.0.0.1 と入力してOKを押してください。
4. サーボスプライトを作成して、適当なサーボ値を設定し、'servo changedを送る'を押してください。

##Install
1. `sudo pip install adafruit-pca9685`

##Circuit
![i2c_sampleで利用した回路例](https://raw.githubusercontent.com/wiki/EiichiroIto/ServoDesigner/images/i2c_sample.png)
