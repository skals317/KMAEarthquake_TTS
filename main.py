from requests import get
from bs4 import BeautifulSoup
import requests
import time
 

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)

url = 'https://www.weather.go.kr/w/eqk-vol/search/korea.do?dpType=a'
          
response = requests.get(url)
      
if response.status_code == 200:
          html = response.text
          soup = BeautifulSoup(html, 'html.parser')
          time = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(2) > span')
          time = time.get_text()
          mag = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(3) > span')
          mag = mag.get_text()
          dep = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(4) > span')
          dep = dep.get_text()
          maxint = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(5) > span')
          maxint = maxint.get_text()
          area = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(8) > span')
          area = area.get_text()
          map = soup.select_one('#excel_body > tbody > tr:nth-child(1) > td:nth-child(9) > a')
          map = str(map)[9:86]
        
          if mag<"2.0":
            miso = "미소"
          else:
            miso = ""
  
          print("발생시각 : "+time)
          print("규모 : M"+mag)
          print("깊이 : "+dep+"km")
          print("최대진도 : "+maxint)
          print("발생지역"+area)
          print("지도 : "+map)
          ttsdabon = (f"한국에서 {miso}지진정보를 수신하였습니다. {time}에 {area}에서 규모,{mag}의 지진이 발생하였습니다. 깊이는 {dep}km이며, 최대진도는{maxint}입니다.")
          tts = 'https://playentry.org/api/expansionBlock/tts/read.mp3?text='+ttsdabon+'&speed=0&pitch=0&speaker=hana&volume=1'
          print(tts)  
else:
    print(response.status_code) 

if __name__ == '__main__':
	url = tts
	download(url,"tts.mp3")
