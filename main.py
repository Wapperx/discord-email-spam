import requests, sys
from time import sleep

class Email_Spam:
    def __init__(self, token):
        self.token = token
        self.headers = {"authorization": self.token, "user-agent": "Mozilla/5.0"}

    def emal_remove(self):
        requests.get(
            "https://canary.discordapp.com/api/v8/guilds/0/members", 
            headers=self.headers
        )

    def email_onay(self):
        r = requests.post(
            "https://discord.com/api/v8/auth/verify/resend", 
            headers=self.headers
        )
        if r.status_code == 204:
            print("Başarıyla email gönderildi.")
        else:
            print("Ratelimit, Lütfen bekleyin...")

    def spam_token_email(self):
        self.emal_remove()
        while True:
            sleep(2)
            self.email_onay()

def main():
    if len(sys.argv) < 2:
        print(f'Kullanım: python {sys.argv[0]} "Token"')
        sys.exit()
    token = sys.argv[1]
    r = requests.get('https://discord.com/api/v9/users/@me', headers={"authorization": token})
    if r.status_code == 200:
        pass
    else:
        print(f"Hatalı Token, Lütfen geçerli bir token girin.")
        sys.exit()
    Email_Spam(token).spam_token_email()

if __name__ == '__main__':
    main()
