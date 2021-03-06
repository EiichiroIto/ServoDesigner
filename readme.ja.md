ServoDesigner
====

# Overview
ServoDesignerは、複数のサーボを同時に制御するための支援を行うScratch拡張です。

最大30個までのサーボ値を同時に設定したり、切り替えたりすることができます。ServoDesignerにはサーボを直接制御する機能はありませんが、サーボを制御するプログラムと[Remote Sensor Protocol](https://wiki.scratch.mit.edu/wiki/Remote_Sensors_Protocol)でネットワーク接続することにより、間接的に制御します。

# Description
ServoDesignerは、Based on Scratchでサーボ制御を行うスプライトとして組み込まれます。プロジェクトにサーボのスプライトを追加すると、サーボ値に対応するch1〜ch20までの変数が自動的に作成されます。サーボのスプライトのコスチュームを編集することで、複数のサーボ値を一度に指定します。コスチュームを切り替えるとサーボ値に対応する変数の内容が変わり、同時にブロードキャストメッセージが送信されます。

ServoDesignerはBased on ScratchのMESH機能を有効にするので、サーボ値に対応する変数の内容やブロードキャストメッセージが自動的に送られます。ただし、ServoDesignerからRemote Sensor Protocol経由でサーボ値を受け取り、サーボを制御するプログラムは、実際に利用する機器に応じて作成する必要があります。

サンプルとしてArduinoでfirmataを使ってサーボ制御を行うPythonプログラムの例と、Raspberry piでwiringpiを用いたi2C通信によりサーボ制御を行うPythonプログラムの例を用意していますので、それぞれの環境に応じて、適切なプログラムを用意してください。

## 構成図
ServoDesigner/Based on Scratch

--> Programs that controls servo motors (Remote Sensor Protocolによる通信)

--> Servo Controller (GPIO, firmata, i2c 等)

--> Servo Motors (最大30個までのサーボモータ)

# Demo
![サーボスプライトの作成とサーボ値の設定](https://raw.githubusercontent.com/wiki/EiichiroIto/ServoDesigner/images/sd1.gif)
![見た目ブロックによるサーボスプライトの変更](https://raw.githubusercontent.com/wiki/EiichiroIto/ServoDesigner/images/sd2.gif)
![ブロードキャストメッセージの利用](https://raw.githubusercontent.com/wiki/EiichiroIto/ServoDesigner/images/sd3.gif)

# Requirement
* Scratch 1.4
* Scratch Source Code 1.4 -- csファイルからのインストールの場合

## 実際にサーボを動かす場合には以下が必要
* サーボモータ
* サーボコントローラ
* Python環境(Python 2.7)

# Usage
## サーボ制御プログラムへの接続
1. Remote Sensor Protocolを処理してサーボを制御するプログラムを起動する。
2. 共有メニューをクリックして、'Meshに加わる'を選ぶ。
3. サーボ制御プログラムが動作しているPCのIPアドレスを入力する。

## サーボスプライトの作成とサーボ値の設定
1. ステージを右クリックして、"サーボスプライトを作る"を選ぶ。
2. "コスチューム"タブを選び、表示されているコスチュームでEditボタンを押す。
3. "サーボエディタ"を開いて、各サーボに対応した変数ウォッチャーのスライダーを変更する。
4. 変数ウォッチャーをクリックすると、ダイアログボックスが現れるので直接サーボの値を入力する。
5. "servo changedを送る"ボタンを押すと、servo changedがブロードキャストメッセージとして送られる。
6. "常に送る"を選べば、変数ウォッチャーを変更するたびに自動的にブロードキャストメッセージが送られる。
7. "全て〜を設定"ボタンを押せば、0, 128, 255 または入力した値が、全ての変数ウォッチャーに設定される。

## 見た目(Looks)ブロックを使う
1. "見た目"のブロックカテゴリを選ぶ。
2. "2秒でコスチュームをservoにする"のブロックをスクリプトに置く。
3. 2秒のところを適当な秒数に変える。
4. servoのところを適当なコスチュームに変える。

# Install
## イメージからのインストール
1. インストーラを使わず、新たにScratch 1.4をインストールする。
2. このパッケージに付属するServoDesigner.imageとServoDesigner.changesを、インストールしたScratch 1.4のフォルダにコピーする。
3. ServoDesigner.imageをScratchアプリケーションにドラッグ＆ドロップしてScratchを起動する。

## csファイルからのインストール
1. インストーラを使わず、新たにScratch 1.4をインストールする。
2. ScratchSourceCode1.4を展開して、インストールしたScratch 1.4のフォルダに展開した内容をコピーする。
3. ScratchSourceCode1.4.imageをScratchアプリケーションにドラッグ＆ドロップしてScratchを起動する。
4. WorkspaceとSystem Browserのウィンドウを両方とも閉じる。閉じる際にChanges have not been saved...のダイアログが出たらYesを選ぶ。
5. シフトキーを押しながらデスクトップをクリックして"find window"メニューを出し、Scratch Frameを選ぶ。
6. Scratchのウィンドウの左上に現れたクローズボタンをクリックして閉じる。
7. 空になったデスクトップをクリックしてopen...を選び、file listのメニュー項目を選ぶ。
8. File Listウィンドウの右上のペインで、ServoDesigner.*.csを選ぶ。（*は何らかの数値）
9. 右上のペインの左端にスクロールバーが現れるので、その上にあるメニューボタンを押して、fileInを選ぶ。
10. デスクトップをクリックしてopen...を選び、Scratchのメニュー項目を選ぶ。
11. Based on Scratchが起動するので、シフトキーを押しながらFileメニューを選び、Save Image in User Modeを選ぶ。
12. Close non-Scratch windows...のダイアログでYesを選ぶ。
13. 自動的にScratchが閉じて完了する。

# License
The MIT License (MIT)

# Option
Scratch.iniで設定するサーボ数を変更することができる。（以下は例）

`ServoChannels=28`


