#!/bin/bash
#
#
#
echo "Deleting all but admin users from mycustom_WP1 ... "
echo "running command: mysql -D mycustom_WP1 -u mycustom --password='f7Jh1jv27O' -h mycustombusinessapp.com -e \"DELETE FROM wp_mcba_users WHERE isAdmin='0'\""

mysql -D mycustom_WP1 -u mycustom --password='f7Jh1jv27O' -h mycustombusinessapp.com -e "DELETE FROM wp_mcba_users WHERE isAdmin='0'"

echo "Deleting all but admin users from awmstag2_car ... "
echo "Running command: mysql -D awmstag2_car -u awmstag2_car --password='.&#CL=}2W$EO' -h floridascarwash.com -e \"DELETE FROM wp_mcba_users WHERE isAdmin='0'\""
mysql -D awmstag2_car -u awmstag2_car --password='.&#CL=}2W$EO' -h floridascarwash.com -e "DELETE FROM wp_mcba_users WHERE isAdmin='0'"
