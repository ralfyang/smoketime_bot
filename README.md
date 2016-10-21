# 담배 맴버들 모여라! 같이가자!
* This is a folk version of pyTelegramBot API(https://github.com/eternnoir/pyTelegramBotAPI)

* Requires Python, telebot lib of python
```
pip install pyTelegramBotAPI
pip install  telebot
```


1. telegram의 botfather를 통해 봇 등록 (웹 브라우저에서 https://telegram.me/botfather 주소로 접속)
2. ```/newbot``` 으로 봇 등록
3. 토큰 키 발급
4. smoking_bot.py open
 ``` vi smoking_bot.py```
5. 3에서 발급받은 토큰키 입력 
```
API_TOKEN = '<ADD YOUR TOKEN KEY HERE>'
```

* 모여서 담배 필 장소 메시지 변경
```
    bot.reply_to(message, """\
It's time to Smoke!!! let's go 장보명 \
""")
```

* 스크립트 실행
```
python ./smoking_bot.py
```
