# mkreportとは

日報の作成とRedmineへの作業時間の入力を楽にするツールです。

## 使い方

以下のコマンドで使うことができます。</br>
(`python3`をインストールしていることが前提です。)

```bash
$ git clone https://github.com/wawawatataru/mkreport.git
$ cd mkreport
$ pip3 install -e .
$ mkreport
```

## 環境変数

実行時に環境変数を設定してください。</br>
例えば`direnv`を利用している場合は`.envrc`ファイルを以下のように設定してください。

```.env
export REPORTER=七五三
export DEFAULT_START_TIME=0730
export DEFAULT_END_TIME=1630
export REDMINE_URL=https://redmine_url
export REDMINE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxx
```

`REPORTER`にはあなたの名前を入力してください。</br>
生成される日報に入力されます。

`DEFAULT_START_TIME` `DEFAULT_END_TIME`には勤務開始、終了時間を`hhmm`の数字4桁で入力してください。</br>
勤務開始、終了時間は日報を作成するたびに入力できますが、空欄で入力した場合にここで入力した値が使用されます。

`REDMINE_URL`にはRedmineのURLを入力してください。</br>
BASIC認証が設定されている場合は`http://user:password@redmine_url`とすることで認証可能になります。

`REDMINE_API_KEY`にはRedmineのAPIアクセスキーを入力してください。</br>
詳しくは[こちら](https://redmine.jp/glossary/r/rest-api/)

## mkreportコマンド

`mkreport`コマンドを実行すると対話式で入力を求められます。

```bash
 務開始時間を「hhmm」で入力してください(デフォルト「0730」)
0720
勤務終了時間を「hhmm」で入力してください(デフォルト「1630」)
1700
```

はじめに、勤務時間の入力を求められます。`hhmm`の形式で4桁の数字を入力してください。</br>
何もせずにエンターボタンを押すと環境変数で設定されたデフォルトの値になります。</br>
ここで入力した値は生成される日報の勤務時間に記載されます。

```bash
作業したチケットの番号を入力してください(qを入力すると終了)
100
「環境構築」でよろしいですか?(y/n)
y
```

次に作業したチケットの番号を求められるので、作業したRedmineのチケットの番号を入力してください。</br>
(もし作業したRedmineのチケットがなければ`q`を入力し次に進んでください。)</br>
番号を入力するとチケットのタイトルが表示されるので正しければ`y`を、間違っていれば`n`を入力してください。

```bash
日報に記載する作業内容を入力してください
着手開始
作業時間を入力してください
2
```

次に入力したチケットの作業内容と作業時間を求められので、それぞれ入力してください。</br>
作業内容に関しては生成される日報に記載されますが、それ以外には使用されません。</br>
作業時間に関しては該当するチケットの作業時間としてRedmineに登録されます。</br>
詳しくは[こちら](https://redmine.jp/glossary/t/time-tracking/)</br>

登録される**作業者はAPIアクセスキーのユーザー、それ以外の項目はデフォルトの値となる**のでご注意ください。</br>
作業時間はRedmineの作業時間登録にのみ使用し、生成される日報には記載されません。

```bash
他にも作業したチケットがあればチケットの番号を入力してください(qを入力すると終了)
q
```

他に作業したチケットがあればチケットの番号を入力し、なければ`q`を入力し次に進んでください

```bash
日報の最後に記載する一言を入力してください
今日も 一日お疲れさまでした。
```

最後に日報の最後に記載する一言の入力を求められます。

何も入力しない場合は記載されずに日報が生成されます。

```bash
日報を作成しました。
./daily_report/2020/1/1.txt
```

生成された日報のファイルパスが出力されます。

## 日報の内容

日報の内容は[report_content.txt](./report_content.txt)に記載されていますので自由に変更してください。</br>
上記の入力内容では下記のファイルが生成されます。

```txt
【日報】七五三 6/4(木)
お疲れさまです。
七五三です。

本日の日報です。

【勤務時間】
7:20-17:00

【作業内容】
#100 環境構築
  実装開始

【ひとこと】
一日お疲れさまでした。
```
