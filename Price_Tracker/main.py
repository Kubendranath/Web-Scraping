import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
header = {
    "Accept-Language": "en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response  = requests.get(URL,headers= header)


soup = BeautifulSoup(response.text , "html.parser")
price = soup.select(".a-price-whole")[0].getText()
price_float =float(price)
print(price)

if price_float<100:
    with smtplib.SMTP(os.environ["SMTP_ADD"],port = 587) as connection:  #Here port 587 is used as it is the port for secure email transfer and by default it takes port 25 which is not meant to be secure and most of the ISPs tend to drop traffic from that port.

        connection.starttls()
        connection.login(user=os.environ["MAIL_ID"],password=os.environ["PASS"])
        connection.sendmail(from_addr=os.environ['MAIL_ID'],
                            to_addrs=os.environ['MAIL_ID'],
                            msg="SUBJECT : Hurry Amazon remainder \n\n This a remainder that the price of the product "
                                f"you have chosen has gone below 100$ ie ${price}.{URL}"
                            )

