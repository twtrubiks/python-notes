# 透過 pika 操作 Rabbitmq

rabbitmq 簡易架構圖

![alt tag](https://i.imgur.com/nHkscz6.png)

安裝指令

```cmd
pip inatsll pika
```

## 教學

先把 Rabbitmq 啟動

```cmd
docker-compose up -d
```

Hello World! 模式

![alt tag](https://i.imgur.com/NKtsUQV.png)

參考 code [hello_world](https://github.com/twtrubiks/python-notes/tree/master/pika_tutorial/hello_world)

官方文件可參考 [https://www.rabbitmq.com/tutorials/tutorial-one-python.html](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)

Work queues 模式

![alt tag](https://i.imgur.com/SWxPPS5.png)

參考 code [work_queues](https://github.com/twtrubiks/python-notes/tree/master/pika_tutorial/work_queues)

官方文件可參考 [https://www.rabbitmq.com/tutorials/tutorial-two-python.html](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)

Publish/Subscribe 模式

![alt tag](https://i.imgur.com/Uzkszaa.png)

參考 code [pub_sub](https://github.com/twtrubiks/python-notes/tree/master/pika_tutorial/pub_sub)

官方文件可參考 [https://www.rabbitmq.com/tutorials/tutorial-three-python.html](https://www.rabbitmq.com/tutorials/tutorial-three-python.html)

Routing 模式

![alt tag](https://i.imgur.com/68FCveH.png)

參考 code [routing](https://github.com/twtrubiks/python-notes/tree/master/pika_tutorial/routing)

官方文件可參考 [https://www.rabbitmq.com/tutorials/tutorial-four-python.html](https://www.rabbitmq.com/tutorials/tutorial-four-python.html)

Topics 模式

![alt tag](https://i.imgur.com/4dZJkcg.png)

參考 code [topic](https://github.com/twtrubiks/python-notes/tree/master/pika_tutorial/topic)

官方文件可參考 [https://www.rabbitmq.com/tutorials/tutorial-five-python.html](https://www.rabbitmq.com/tutorials/tutorial-five-python.html)

RPC 模式

![alt tag](https://i.imgur.com/rX4AFa8.png)

參考 code [rpc](https://github.com/twtrubiks/python-notes/tree/master/pika_tutorial/rpc)

官方文件可參考 [https://www.rabbitmq.com/tutorials/tutorial-six-python.html](https://www.rabbitmq.com/tutorials/tutorial-six-python.html)

## Reference

* [https://www.rabbitmq.com/getstarted.html](https://www.rabbitmq.com/getstarted.html)