import os
import requests
import time


class WeChatNotifier:
    def __init__(self):
        # Load the environment variables
        self.WX_APP_ID = os.getenv("WX_APP_ID")
        self.WX_SECRET_ID = os.getenv("WX_SECRET_ID")
        self.WX_KF_ACCOUNT = os.getenv("WX_KF_ACCOUNT")
        self.WX_NICK_NAME = os.getenv("WX_NICK_NAME")
        self.WX_PASSWORD = os.getenv("WX_PASSWORD")
        self.WX_TOUSER = os.getenv("WX_TOUSER").split(",")
        self.access_token = self.get_wechat_token()

    # Get the access token
    def get_wechat_token(self):
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.WX_APP_ID}&secret={self.WX_SECRET_ID}"
        response = requests.get(url)

        if response.json().get("errcode"):
            print("Failed to get access token: ",
                  response.json().get("errcode"))
            return None
        else:
            print("Access token received successfully")
            return response.json()["access_token"]

    # Create the customer service account
    def create_customer(self):
        url = f"https://api.weixin.qq.com/customservice/kfaccount/add?access_token={self.access_token}"
        response = requests.post(url, json={
            "kf_account": self.WX_KF_ACCOUNT,
            "nickname": self.WX_NICK_NAME,
            "password": self.WX_PASSWORD
        })

        if response.json().get("errcode") and response.json().get("errcode") != 65406:  # 65406: account already exists
            print("Failed to create customer: ", response.json().get(
                "errcode"), response.json().get("errmsg"))
            return False
        else:
            print("Customer created successfully")
            return True

    # Send the notification
    def send_wechat_notification(self, name, web_url, new_litters):
        # Check if the access token has been successfully received and the customer service account has been created
        if not self.access_token or not self.create_customer():
            return None

        # Create the notification content
        content = f"ALERT: {name} new litters available\n"
        for litter in new_litters:
            content += (
                f"\nFather: {litter['father']}\n"
                f"Mother: {litter['mother']}\n"
                f"Pedigree: {litter['pedigree']}\n"
                f"Birthdate: {litter['birthdate']}\n"
                f"Litter Quantity: {litter['litter_quantity']}\n"
                f"Expected Races: {', '.join(race for race, flag in zip(['roux', 'sesame', 'noir et feu'], litter['expected_race']) if flag)}\n"
            )
        content += f"\n\n{web_url}"

        print(content)

        # Send the notification to each user
        for touser in self.WX_TOUSER:
            url = f"https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={self.access_token}"
            response = requests.post(url, json={
                "touser": touser,
                "msgtype": "text",
                "text": {
                    "content": content
                },
                "customservice": {
                    "kf_account": self.WX_KF_ACCOUNT
                }
            })

            if response.json().get("errcode"):
                print("Failed to send notification: ",
                      response.json().get("errmsg"))
                return None
            else:
                print("Notification sent successfully")

            time.sleep(5)
