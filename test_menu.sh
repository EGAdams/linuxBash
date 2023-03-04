#!/bin/bash

SCRIPT_RUNTHROUGH=$'\e[1;31mRUNTHROUGH\e[0;33m'
PROGRAM_QUIT=$'\e[1;31mQUIT\e[0;33m'
PATTERN_NEW=$'\e[1;31mNEW SEARCH PATERN\e[0;33m'
PATTERN_CLEAR=$'\e[1;31mCLEAR SEARCHES\e[0;33m'


sh$ for i in {1..12}; 
    do OPTIONS[$i]=$(printf "option-%02d" $i); 
done

sh$ select i in "${OPTIONS[@]}"; 
    do echo $i ; 
done

echo"
1) option-01    4) option-04   7) option-07  10) option-10
2) option-02    5) option-05   8) option-08  11) option-11
3) option-03    6) option-06   9) option-09  12) option-12
"

# draw another .sh menu
