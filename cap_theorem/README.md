***CAP theorem***

[Youtube Tutorial - What is CAP theorem](https://youtu.be/jBgN5g_FaOs)

如果你有接觸到分散式系統 ( distributed system )，就一定要認識 CAP 定理 ( CAP theorem )，

CAP 的定義分別為，

* Consistency ( 一致性 )
* Availability ( 可用性 )
* Partition tolerance ( 分區容錯 )

( 疑 :question: 是不是感覺似曾相識，沒錯，之前也有介紹過一個 [ACID](https://github.com/twtrubiks/django-transactions-tutorial#transaction)，但要注意的是，

雖然英文字母一樣，但代表的意思是不一樣的哦 :smiley: )

通常來說，這三個定義不可能同時滿足，如下圖，

![img](https://i.imgur.com/CEsfjSG.png)

* Partition tolerance ( 分區容錯 )

大部分的分散式系統，節點之間的網路本來應該是相通的，但是很有可能因為一些原因故障了，

所以導致網路被切分了很多塊，這就是所謂的分區。

假設你的資料只儲存在某個節點上，這樣在發生分區後，某些節點之間的網路不通了，就會拿不到你要的資料，

為了解決上述這個問題，我們就必須將資料複製到多個節點上，這樣就算發生了分區，需要的資料也就有更高

的機率被拿到 ( 資料在自己的分區內 )，容錯率也就提高了。

這就是所謂的 Partition tolerance ( 分區容錯 )，基本上 Partition tolerance ( 分區容錯 ) 算是

分散式中最基本的原則，如果一定要保留 P，勢必要在 C 和 A 之間選擇一個。

* Consistency ( 一致性 )

簡單說 Consistency 就是每個節點中的資料要一致，

假設 A1 以及 A2 的初始值都是 0 ，看下面這張圖，

![img](https://i.imgur.com/T97pc5E.png)


client 端將 A1 中的 0 更新為 1，但是此時 A2 的值還是 0 ，

![img](https://i.imgur.com/OL8W9qO.png)


這樣如果有用戶向  A2 取資料時，就會拿到 0，發生 A1 以及 A2 不一致的現象，

![img](https://i.imgur.com/b6MQw18.png)

所以為了要保持一致性，A1 必須發送一個 request 將 A2 也更新為 1，

換個角度思考，也就是訪問的任何節點都必須是最新的資料 ( 如下圖 )。

![img](https://i.imgur.com/eny1Grb.png)

* Availability ( 可用性 )

當節點收到用戶的 request 時，必須馬上給出 response，像是 client 端不管向 A1 還是 A2 發送 request，

節點必須馬上回應是 0 或是 1，換個角度思考，也就是每次的 request 都能得到不是 ERROR 的 response，

但是不保證資料都是最新的。

了解 CAP 分別的定義之後，讓我們再來回頭看三個指標不可能同時滿足這點，

首先，Partition tolerance ( 分區容錯 ) 通常無法避免，

***CP***

假如選擇 C ( Consistency )，A ( Availability ) 就無法滿足，原因是因為為了滿足一致性，就必須將其他的節點鎖定更新，

避免這個時間有客戶去取資料 ( 導致拿到的資料不是最新的 )，然而我們鎖定其他的節點後，就會導致無法滿足可用性 ( Availability )，

因為分散式系統通常都有很多區要更新資料，所以需要時間更新。

***AP***

假如選擇 A ( Availability )，C ( Consistency ) 就無法滿足，原因是要滿足 Availability ( 可用性 )，要立即的 response，

所以勢必就無法鎖定更新，也就沒辦法滿足一致性。

如果我想要同時滿足 C 和 A 呢 ?

***CA***

但這就放棄 P 了，也就是放棄了最基本分散式的概念。

介紹到這邊算是一個段落了，大家還是要去想想看自己的情境比較適合使用哪一種，沒有絕對好的東西，只有最適合的方法。

基本上 CAP 基本的介紹就到這邊，如果你想更進一步的了解 ( 接觸分散式的東西 )，可以玩玩看 docker swarm，

請參考 [Docker Swarm 基本教學 - 從無到有 Docker-Swarm-Beginners-Guide📝](https://github.com/twtrubiks/docker-swarm-tutorial)。