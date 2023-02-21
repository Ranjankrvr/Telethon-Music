import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5613609672:AAHfMv9npUuWr8qih_UgIVBV2qeKDjXCLqs")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLABu56Ysxeqf6ulcZaQ9vixgTGj4ypX2Xb-BkTIW_R5zVR1bLafCc5yV5_5JBQeqJGmCx8tSpE7KSc1IDD3kUaa-JeOpWd6tkygYZualvVaZN7TVSTw3HRd0Grp10L4QbPYO8M0BBOGd9-qW8nRknLz0mgRHJLnPaBfR7QEBiY-C9vKV60bi_NQwroJ17AG2DroCM2215RhruuNldwZviw9lJc-EzYOJqdHz160_DTtgVN-05IOn_EshBlvvjhqTnHNHpgfv67LHdflZSlR1U9YUIzH515FJs3gwPami2DIs6alZzjnMu5vwRfi6wiz6D1zTfu6pvy4SUgJTu2Ag5PWLmk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
