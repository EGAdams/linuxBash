#!/usr/bin/expect

exec ssh dietpi@192.168.1.10
expect "Password:"
send "tinman88\n"

