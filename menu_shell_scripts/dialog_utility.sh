#!/bin/sh
#http://unstableme.blogspot.com/
#A sample application using UNIX/Linux dialog utility
#Auto-size with height and width = 0 of the dialog controls

file='conf.txt'
tempfile1=dialog_1_$$
tempfile2=dialog_2_$$
tempfile3=dialog_3_$$

trap _exit_procedure 0 1 2 5 15

_edit () {
   items=$(awk -F\: '{print $1,$2}' $file)
   dialog --title "Command Menu" \
          --menu "What you want to change :" 0 0 0 $items 2> $tempfile1

   retval=$?
   parameter=$(cat $tempfile1)

   [ $retval -eq 0 ] && tochange=$parameter || return 1

   # /// input box /// 
   val=$(awk -F\: -v x=$tochange '$1==x {print $2}' $file)
   dialog --clear --title "Enter new command value" \
          --inputbox "Enter new value($tochange)" 0 0 $val 2> $tempfile2

   # /// confirmation ///
   dialog --title "Confirmation"  --yesno "Commit ?" 0 0
   case $? in
       0) newval=$(cat $tempfile2)
          awk -v x=$tochange -v n=$newval '
               BEGIN {FS=OFS=":"}$1==x {$2=n} {print}
               ' $file > $file.tmp
          mv $file.tmp $file
       ;;
       1|255) dialog --infobox "No Changes done" 0 0
              sleep 2
   ;;
   esac
   dialog --textbox $file 0 0
}

_main () {
   dialog --title "View or Edit config file" \
           --menu "Please choose an option:" 15 55 5 \
                   1 "View the config file" \
                   2 "Edit config file" \
                   3 "Exit from this menu" \
                   4 "change directory" 2> $tempfile3

   retv=$?
   choice=$(cat $tempfile3)
   [ $retv -eq 1 -o $retv -eq 255 ] && exit

   case $choice in
       1) dialog --textbox $file 0 0
          _main
           ;;
       2) _edit
          _main ;;
       3) return ;;
       4) cd /mnt/c
   esac
}

_exit_procedure() {
    echo "removing temp files..."
    rm -f $tempfile1 $tempfile2 $tempfile3
    cd /mnt/c   
}

_main
