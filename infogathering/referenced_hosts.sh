#!/bin/bash
#PARSER TO FIND HOSTS IPS REFERENCED ON A HTML PAGE

file="tmp_file"
if [ "$1" == "" ];
then
	echo "MODO DE USO"
	echo "$0 <URL>"
else
	curl $1 > $file
	for url in $(cat $file | egrep -o 'https?://[^ ]+' | cut -d '"' -f 1 | cut -d "/" -f 3);
		do nslookup $url
	done

fi

rm $file
