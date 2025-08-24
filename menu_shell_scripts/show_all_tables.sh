#!/bin/bash

echo
echo "executing mysql -D commands..."

mysql -D visionte_8 -e "SELECT ID, pushid, first_name, last_name, rewards, device, email, uid, isAdmin FROM wp_mcba_users;"
mysql -D visionte_8 -e "SELECT * FROM wp_mcba_chat_messages;"
mysql -D visionte_8 -e "SELECT * FROM wp_mcba_chat_conversations;"

echo "finished showing all tables."
echo
