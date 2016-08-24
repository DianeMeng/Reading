for file in `ls data`
do
    cat data/$file  |awk -F ';' '{if ( $3 >= "2013-06-01" ) print $0}' >> output/$file
    sort -u output/$file >>output/1_$file
    rm output/$file
    #gzip output/$file
done
