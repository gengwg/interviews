 $ ip -o addr | awk '{print $2, $4}'
 lo 127.0.0.1/8
 lo ::1/128
 wlp3s0 192.168.1.77/24
 wlp3s0 2600:1700:9770:1e90:c0e7:171e:985b:e92d/64
 wlp3s0 fe80::9240:f51a:f76d:3d4b/64
 virbr0 192.168.122.1/24
 docker0 172.17.0.1/16
