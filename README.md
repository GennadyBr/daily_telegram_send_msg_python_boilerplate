# Send msg to Telegram via GitHub Actions every day

This is boilerplate to send message to Telegram
I use GitHub Actions for free of charge daily sending message
GitHib Actions activate python program from workflow pipeline.yaml

## Installation && Run
### Git clone
```
https://github.com/GennadyBr/daily_telegram_send_msg_python_boilerplate.git
```

### Create .env file from .env.example
to get TELEGRAM_BOT_TOKEN 
please use 
```
https://core.telegram.org/bots/tutorial#obtain-your-bot-token)
```

to get TELEGRAM_MSG_RECEIVER
please use 
```
https://t.me/username_to_id_bot
```


### Run app
```
cd src && python main.py
```

### Run tests
```
cd ../tests && pytest test
```

### Logs you can find in console and logs file

### Logs file
```
cd ../src/logs/logs.log
```

## Features
### Get weather forescast from Open-Meteo API
- https://open-meteo.com/en/docs

### Telegram
- send message to Telegram

### GitHub Action
- define crone schedule at GitHub Action for daily service
