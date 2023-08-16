#!/bin/bash
#
#
#
#
mysql -D mycustom_MCBA -u mycustom --password='f7Jh1jv27O' -h mycustombusinessapp.com -e "select _id, name, baseURL, gcm_api_key  from clients"
echo; echo;