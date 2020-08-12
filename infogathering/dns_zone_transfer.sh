#!/bin/bash
#TESTS ZONE TRANSFER ON DNS SERVERS

if [ "$1" == "" ];
then
        echo "HOW TO"
        echo "$0 <DOMAIN>"
else        
        for server in $(host -t ns $1 | cut -d " " -f4);
                do host -l -a $1 $server;
        done

fi

