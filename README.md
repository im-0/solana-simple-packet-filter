# Examples:

Print commands to stdout:

```text
$ ./gencmds.py pubkeys 8003,8004
iptables -t raw -I PREROUTING -p udp -m multiport --dports 8003,8004 -m string --algo bm --hex-string "|092aee40bbdd631eeffb7c96f61565768465f3c19cf990cd7f748c8d79950820|" -j DROP
iptables -t raw -I PREROUTING -p udp -m multiport --dports 8003,8004 -m string --algo bm --hex-string "|092aee3dfc2d0e55782313837969eaf52151c096c06b5c2a82f086a503e82c34|" -j DROP
iptables -t raw -I PREROUTING -p udp -m multiport --dports 8003,8004 -m string --algo bm --hex-string "|052f21a9fe604e569e956f29223106fa26ce0a21520247a93a07a1489239c8ff|" -j DROP
```

Run commands immediately:

```text
$ ./gencmds.py pubkeys 8003,8004 | sh -x
+ iptables -t raw -I PREROUTING -p udp -m multiport --dports 8003,8004 -m string --algo bm --hex-string '|092aee40bbdd631eeffb7c96f61565768465f3c19cf990cd7f748c8d79950820|' -j DROP
+ iptables -t raw -I PREROUTING -p udp -m multiport --dports 8003,8004 -m string --algo bm --hex-string '|092aee3dfc2d0e55782313837969eaf52151c096c06b5c2a82f086a503e82c34|' -j DROP
+ iptables -t raw -I PREROUTING -p udp -m multiport --dports 8003,8004 -m string --algo bm --hex-string '|052f21a9fe604e569e956f29223106fa26ce0a21520247a93a07a1489239c8ff|' -j DROP
```
