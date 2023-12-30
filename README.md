# Mypkg

![test](https://github.com/Towa92/pkg1/actions/workflows/test.yml/badge.svg)

# Mypkgについて

このレポジトリはROS2のパッケージです。千葉工業大学で預かった授業にそった内容となります。

# talker.py と listener.py
このノードは mypkg パッケージの中にある　talker.py から発信する値を受け取り画面に表示します。

動作例


```
端末1
$ ros2 run mypkg talker

端末2
$ ros2 run mypkg listener

Listen : 1
Listen : 2
Listen : 3

```
# talk_listen.launch.py
このノードは二つの端末が立った後に画面表示することを一つにまとめたものです。

動作例

```
$ ros2 launch talk_listen.launch.py

Listen : 1
Listen : 2
Listen : 3

```

# テスト環境

* Ubuntu 22.04
* ROS2 Humble Hawksbill
テスト環境には問題ありません。

Github Actionsテストに千葉工業大学の上田隆一先生のコンテナを使用しています。

URL:https://hub.docker.com/repository/docker/ryuichiueda/ubuntu22.04-ros2

# LICENSE

このソフトウェアパッケージは3条項BSDライセンスの元、再配布及び使用が許可されています。

LICENSE:https://github.com/Towa92/Mypkg/blob/master/LICENSE

© 2023 Towa


