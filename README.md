# bit composer
 自動作曲Webアプリケーション

# アプリの機能・特徴
ゲーム音楽を学習した作曲AIがユーザが入力した短いメロディに続いてハーモニーがあるメロディを作曲します。

# 使い方
1. Webページ上に表示されるピアノからメロディを入力していく
2. メロディをサーバに送信してAIが作曲
3. 曲のmp3を再生

# Webシステムについて
サーバプログラムはPythonのライブラリのFlaskを使っています。
 
 ![image](https://user-images.githubusercontent.com/43458963/143021077-12c72daf-c194-4914-8e4b-0b77dd9f3822.png)

# AIについて
自動作曲はRNN(Recurrent Neural Network)を使っています。

# 進捗
### ver 0.15
- 基盤となるWebサイト

![bc_main](https://user-images.githubusercontent.com/84367211/138039843-7c1eacbf-d8f5-46e5-b598-f8a70b40467c.png)

### ver 0.2
- 入力ページから音データを送信、結果出力画面に出力するプログラム

https://user-images.githubusercontent.com/43458963/140646112-cf224084-281a-49da-ac29-9407ec4a9067.mp4

### ver 0.3
- 入力画面のGUIのプログラム

### ver 0.4
- 短いメロディから続きのメロディを推測するAIの作成

### ver 0.5
- デザインとシステムの調整
- Webサーバの公開

### ver 1.0
- リリース!!
