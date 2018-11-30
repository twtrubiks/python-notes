***What happens when you type an URL in the browser and press enter***

[Youtube Tutorial - What happens when you type an URL in the browser and press enter](https://youtu.be/PDR-fIooaLE)

當我們在瀏覽器上輸入網址並且按下 enter 之後， 到底發生了什麼事情:question:

這邊我們一步一步來說明，

首先，在 browser 上的網址列輸入 URL 並且按下 ENTER，

browser 會先查看目前的 URL 是否有在快取之中以及快取是否有過期 ( 通常第一次不會有快取 )，

如果有快取也沒過期，就可以直接拿來使用，不需要再向 server 請求。

這邊假設沒有快取，所以我們必須再向 server 請求，而向 server 請求的這個過程中，就會牽扯

到 DNS 域名解析、TCP 連接建立之類的，我將會按照順序帶大家了解:smiley:

* DNS ( Domain Name System ) 域名解析

透過 DNS server 尋找對應的 URL IP，流程如下，

先查看 browser 快取是否有對應的 IP，如果有就直接回傳，

沒有的話，就查看使用者的 OS 系統中的 hosts 是否有對應的 DNS，

( Windows 通常在 `C:\Windows\System32\drivers\etc\hosts`，Linux 通常在 `/etc/hosts` )

如果在上述兩個步驟中都沒有找到，這時候就會向本地服務器 ( LDNS ) 尋找，

如果還是沒有找到，這時候則會再到 Root Server 域名服務器尋找，

( 這邊要有一個概念，有可能我們不會在第一台 DNS server 就找到對應的 IP，這時候會去更高一級的

DNS server 尋找，直到找到或超時 )

DNS 域名解析過程中的查詢方式有以下兩種，

* Recursive 遞迴式查詢

當主機訪問的域名服務器不知道被查詢的 IP 對應位址時，那麼域名服務器就會以 DNS 客戶端的身分代替主機

向其他的 DNS server 發出查詢請求，而不會讓主機自己進行下一步的訪問。

* Iterative 交談式查詢

當 DNS server 收到請求時，如果查到，則直接返回對應的 IP，否則會告訴本地主機下一步應該要向哪個

DNS server 查詢，由本機主機自己去查詢。

( 和遞迴式查詢不同的地方就在這邊，一個是域名服務器幫忙，一個是由本機自己去處理 )

找到對應的 DNS 之後，server 會將 IP 連同一個 TTL 回傳，本機會將他快取起來，以後就不用再跑那麼遠尋找 DNS 了。

得到 IP 之後，就會依據 IP 接著去建立 TCP 連接，也就是所謂的三次握手 ( 三方交握 )，

* 三次握手( three-way handshake )

![img](https://i.imgur.com/GBlzgS3.png)

從上圖可以觀察到，

Client 端，發送帶有 SYN ( synchronize ) 標誌的資料，第一次握手。

Server 端，發送帶有 SYN+ACK 標誌的資料，第二次握手。

Client 端，發送帶有 ACK ( acknowledegment ) 標誌的資料，第三次握手。

如果在中途出現問題，TCP 會再重新發送相同的資料，

TCP 和 UDP 的差別就是，使用 TCP 可以不用擔心傳輸中資料的遺失，因為 TCP 擁有可靠性，

會保證資料傳輸的完整性以及正確性。

這邊簡單用對話來說明三次握手，

```text
A: hello , 你聽的到我嗎?
B: yoyo, 我聽的到
A: ok , balabala......
```

你可能會問我為什麼 TCP 需要三次握手?

因為要防止已經失效的 request 突然又傳送到 server，導致錯誤。

假設今天 client 端發出一個 request，但因為網路的延遲，導致經過了一段時間之後才送到 server 端，

本來這個 request 因為已經超時所以失效了，但如果沒有三次握手，會導致 server 認為這是一個有效的

request，所以也回送一個 response，但 client 端早就認為這個 request 已經超時失效了，所以不會理

會 server 的回應，導致 server 以為已經和 client 端建立起連線 ( 假設是二次握手 )，然後一直在那邊

等待 client 端的資料，導致浪費資源。

如果有了三次握手，這樣當 server 沒有收到來自 client 端的回應 ( 第三次握手 )，就知道 clinet 端沒有

要求建立連線。

TCP 連線建立完畢之後，接著就是發起 http 請求，

請求方法包括 `GET`、`POST`、`PUT`、`PATCH`、`DELETE`、`OPTION`、`HEAD` 這些，

server 收到請求後，會回應 http 的請求，broswer 接收到 http 的 response，會收到

1xx、2xx、3xx、4xx、5xx 這類的 response code，

最後是 broswer 解析 html，頁面的呈現。

等待雙方傳輸都資料完畢之後，這時候就必須斷開連線，關閉 TCP 連接，有就是所謂的四次揮手。

* 四次輝手( Four-Way Wavehand )

![img](https://i.imgur.com/vER6ZBH.png)

從上圖可以觀察到，

Client 端，發送 FIN+ACK 標誌的資料請求斷開連接，第一次揮手。

Server 端，發送帶有 ACK 標誌的資料同意斷開連接，第二次揮手。

Server 端，發送帶有 FIN+ACK 標誌的資料請求斷開連接，第三次揮手。

Client 端，發送帶有 ACK 標誌的資料表示同意斷開連接，第四次揮手。

這邊簡單用對話來說明四次揮手，

```text
A: yoyo，我想要關閉連線了
B: ok，我收到關閉的請求了
B: yoyo，我也想關閉連線了
A: ok，我也不接收你的資料了
```

為什麼是四次揮手 ?

因為 TCP 是全雙工的雙向溝通，所以當 client 端第一次向 server 揮手時，server 端知道

client 端已經沒有資料要發送了，但是這時侯 client 端還是可以接受來自 server 端的資料，

當 server 端回傳 ACK 給 client 端時 ( 第二次揮手 )，此時 server 端還是可以發送資料給

client 端，所以要等到 server 端發送 FIN+ACK 給 client 端 ( 第三次揮手 ) 時，才能表示

server 端也沒有資料要發送給 client 端了，最後再進行第四次揮手結束 TCP 連線。

* 網際網路協定疊中的層

最後來看一下網際網路協定疊中的層，以下參考 wiki 中的 [TCP/IP協定](https://zh.wikipedia.org/wiki/TCP/IP%E5%8D%8F%E8%AE%AE%E6%97%8F)。

* OSI 模型

| 7 | 應用層 application layer   | 例如 **HTTP**、SMTP、SNMP、FTP、Telnet、SIP、SSH、NFS、RTSP、XMPP、Whois、ENRP          |
|---|----------------------------|-----------------------------------------------------------------------------------------|
| 6 | 表現層 presentation layer  | 例如 XDR、ASN.1、SMB、AFP、NCP                                                          |
| 5 | 會議層 session layer       | 例如 ASAP  、SSH、ISO 8327 / CCITT X.225、RPC、NetBIOS、ASP、IGMP、Winsock、BSD sockets |
| 4 | 傳輸層 transport layer     | 例如 **TCP**、**UDP**、TLS、RTP、SCTP、SPX、ATP、IL                                     |
| 3 | 網路層 network layer       | 例如 **IP**、ICMP、IPX、BGP、OSPF、RIP、IGRP、EIGRP、ARP、RARP、X.25                    |
| 2 | 資料連結層 data link layer | 例如 **乙太網路**、令牌環、HDLC、影格中繼、ISDN、ATM、IEEE 802.11、FDDI、PPP            |
| 1 | 實體層 physical layer      | 例如 線路、無線電、光纖                                                                 |

* TCP/IP 模型

在 TCP/IP 模型中會把 OSI 模型中的三層 ( 應用層、表現層、會議層 ) 歸類為 **應用層**。

| 4 | 應用層 application layer  | 例如 **HTTP**、FTP、**DNS**            |
|---|---------------------------|----------------------------------------|
| 3 | 傳輸層 transport layer    | 例如 **TCP**、**UDP**、RTP、SCTP       |
| 2 | 網路互連層 internet layer | 對於TCP/IP來說這是網際網路協定（IP）   |
| 1 | 網路埠層 link layer       | 例如 **乙太網路**、**Wi-Fi**、MPLS等。 |

更多詳細介紹可參考 wiki 中的 [TCP/IP協定](https://zh.wikipedia.org/wiki/TCP/IP%E5%8D%8F%E8%AE%AE%E6%97%8F)。
