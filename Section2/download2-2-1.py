# Atom 에서 한글을 출력하기 위해서는 아래 설정이 필요

import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxNzAzMjZfMjk0%2FMDAxNDkwNTIxMDgzODc4.Fri8m4XBP2IwwBAhoDZK0OseDMBQfwm3sBUGasHb4QQg.fS-Kjx1RmJmuZzp8uGmF-ID7UBuDfM5FfGGXfaYvJTcg.JPEG.areum5252%2FIMG_1121.JPG&type=sc960_832"
htmlUrl = "http://google.com"

savePath1 = "T:/dev/Download_Destination/test1.jpg"
savePath2 = "T:/dev/Download_Destination/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print('다운로드 완료.')
