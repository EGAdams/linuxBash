#!/bin/bash
#
#
#
#
echo; echo "executing mysql -D commands... "
mysql -D mycustom_WP1 -u mycustom --password='f7Jh1jv27O' -h mycustombusinessapp.com -e "SELECT ID, first_name, last_name, rewards, device, email, uid, isAdmin FROM wp_mcba_users"
mysql -D mycustom_WP1 -u mycustom --password='f7Jh1jv27O' -h mycustombusinessapp.com -e "SELECT * FROM wp_mcba_chat_messages;"
mysql -D mycustom_WP1 -u mycustom --password='f7Jh1jv27O' -h mycustombusinessapp.com -e "SELECT * FROM wp_mcba_chat_conversations;"
mysql -D mycustom_WP1 -u mycustom --password='f7Jh1jv27O' -h mycustombusinessapp.com -e "SELECT * FROM debug_log;"
# mysql -D awmstag2_car -u awmstag2_car --password='.&#CL=}2W$EO' -h floridascarwash.com -e "SELECT ID, first_name, last_name, rewards, device, email, uid, isAdmin FROM wp_mcba_users"
# mysql -D awmstag2_car -u awmstag2_car --password='.&#CL=}2W$EO' -h floridascarwash.com -e "SELECT * FROM wp_mcba_chat_messages;"
# mysql -D awmstag2_car -u awmstag2_car --password='.&#CL=}2W$EO' -h floridascarwash.com -e "SELECT * FROM wp_mcba_chat_conversations;"
# mysql -D awmstag2_car -u awmstag2_car --password='.&#CL=}2W$EO' -h floridascarwash.com -e "SELECT * FROM debug_log;"

echo "finished showing all tables."; echo;