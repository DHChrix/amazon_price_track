from bs4 import BeautifulSoup
import requests
import smtplib

my_email = "hongchengda6@gmail.com"
password = "uuihrbktddfpbeco"



TARGET = 230
HEADERS = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
}

response = requests.get(url="https://www.amazon.co.uk/LG-UltraWide-34WR50QC-compatible-Displayport/dp/B0CCFYGNMX/ref=sr_1_4?crid=GKEFEH1EDZGZ&keywords=curved+monitor+4k&qid=1696256028&s=computers&sprefix=curved+monitor%2Ccomputers%2C78&sr=1-4&ufe=app_do%3Aamzn1.fos.cc223b57-2b86-485c-a85e-6431c1f06c86",
                        headers=HEADERS)
website = response.text
soup = BeautifulSoup(website, "html.parser")
find_price = soup.find(name="span", class_="a-price-whole")
find_price_after_decimal = soup.find(name="span", class_="a-price-fraction")
decimal_price = find_price_after_decimal.getText()
price = float(find_price.getText()) + float(decimal_price)/100

if price <= TARGET:
    message = f"The monitor you want is {price} now"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="chrisdhc02@gmail.com", msg=message)