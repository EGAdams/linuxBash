#
# MyQSL Questions
Here is the command to delete all:
``` 
mysql -D awmstag2_car -u awmstag2_car --password='.&#CL=}2W$EO' -h floridascarwash.com -e "DELETE FROM wp_mcba_chat_conversations"
```

What is the command to delete all except for the record with id 2291?

answer: 
```
mysql -D awmstag2_car -u awmstag2_car --password='.&#CL=}2W$EO' -h floridascarwash.com -e "DELETE FROM wp_mcba_chat_conversations WHERE conversation_id != 2291"
```
