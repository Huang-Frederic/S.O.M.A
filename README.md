
# 📍 S.O.M.A (Shiba Observe Monitoring Assistant)

S.O.M.A (Shiba Observe Monitoring Assistant) is a tool designed to monitor and track new litters of Shiba Inu puppies available on various breeder websites in France. The primary function of this project is to scrape these websites for information about new litters and send notifications when new puppies are available. 

## 🔮 Stack

![Static Badge](https://img.shields.io/badge/Docker-gray?style=for-the-badge&logo=Docker)
![Static Badge](https://img.shields.io/badge/Wechat-gray?style=for-the-badge&logo=Wechat)
![Static Badge](https://img.shields.io/badge/python-gray?style=for-the-badge&logo=Python)
![Static Badge](https://img.shields.io/badge/git-gray?style=for-the-badge&logo=git)
![Static Badge](https://img.shields.io/badge/render-gray?style=for-the-badge&logo=render)
![Static Badge](https://img.shields.io/badge/playwright-gray?style=for-the-badge&logo=playwright)
![Static Badge](https://img.shields.io/badge/bs4-gray?style=for-the-badge&logo=bs4)

## 🚀 Getting Started 

System Requirements:

- Python 3.10+ 
- Package manager/Container: pip, docker

## 🛰️ Environnement Variables

### Wechat

> [!TIP]
> You can create a Wechat interface account from [this link](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)

These environnement variables are required for WeChat integrations :
```env
WX_APP_ID='your_wechat_app_id'          # In the first section of the web when you log in
WX_SECRET_ID='your_wechat_secret_id'    # In the first section of the web when you log in
WX_KF_ACCOUNT='your_wechat_kf_account'  # identifier of the service account, must be "x@x" format
WX_NICK_NAME='your_wechat_nickname'     # nickname of the service account, the one displayed when you receive a message
WX_PASSWORD='your_wechat_password'      # password of the service account, not very important
WX_TOUSER='your_wechat_touser_id'       # 3 sections below, you can scan the qr_code with your Wechat on mobile, you will receive an unique id for each user, add every account you wan't to be notified separated by a comma (id1,id2...)
```
## 💻 Installation

### From source

>Clone the repository
```bash
$ git clone https://github.com/Huang-Frederic/S.O.M.A
$ cd S.O.M.A
```

>Install Python Dependencies
```bash
$ python -m venv env
$ env/bin/activate  # On Windows, use `env\Scripts\activate`
$ pip install -r requirements.txt
```

>Set Up Environment Variables
```bash
# Create a .env file in the root directory of your project and add the following environment variables

WX_APP_ID='your_wechat_app_id' 
WX_SECRET_ID='your_wechat_secret_id'
WX_KF_ACCOUNT='your_wechat_kf_account'
WX_NICK_NAME='your_wechat_nickname'
WX_PASSWORD='your_wechat_password'
WX_TOUSER='your_wechat_touser_id'
```

>Run the project
```bash
$ python main.py
```

### From Docker



>Build the Docker Image:
```bash
$ docker pull -t hisshiden/soma:latest

# if you cannot found the image on DockerHub, build it from the source from the Dockerfile

$ docker build -t whatever_name .
```

>Run the Docker container:
```bash
$ docker run -it \
    -e WX_APP_ID='your_wechat_app_id' \
    -e WX_SECRET_ID='your_wechat_secret_id' \
    -e WX_KF_ACCOUNT='your_wechat_kf_account' \
    -e WX_NICK_NAME='your_wechat_nickname' \
    -e WX_PASSWORD='your_wechat_password' \
    -e WX_TOUSER='your_wechat_touser_id' \
    hisshiden/soma:latest # or whatever_name
```

### Github Actions

Go to your repository, navigate to "Secrets" and add the following secrets :
- WX_APP_ID
- WX_SECRET_ID
- WX_KF_ACCOUNT
- WX_NICK_NAME
- WX_PASSWORD
- WX_TOUSER

Now you can set up Github Actions workflow from `./workflows/main.yml` that is configured to be manually activated, you can uncheck the comented code for schedule functionality.

## 🗺️ Roadmap

- [x]  Scrap Sakura Kensha 
- [ ]  Scrap Chuken Kikusou
- [x]  Add Wechat Notifications
- [ ]  Add Discord Notifications

## 🚶‍♂️ Author

- [@Huang-Frederic](https://github.com/Huang-Frederic)


## 🔗 Acknowledgements

Shiba Breeding Websites :
 - [Sakura Kensha](https://www.sakura-kensha.com/)

Usefull Documentations :
 - [Wechat Documentation](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html)
