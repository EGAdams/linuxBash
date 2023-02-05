#!/bin/bash
#
#
#
mysql -D mycustom_WP1 -u mycustom --password='f7Jh1jv27O' -h mycustombusinessapp.com -e "DELETE FROM wp_mcba_users WHERE isAdmin='0'"
