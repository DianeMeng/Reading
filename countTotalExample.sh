# author mengdan 
# time :2014-01-29
# purpose :get each file name of raw data 
# summary : get  the fila name as parameters, pass to countTotalExample.pig by turn 




count=0
echo "There are :"
for i in `hdfs dfs -ls /user/mengdan/data | awk '{print $8}' | awk -F '/' '{print $5}'`
do
    count=$(($count+1))
    echo $count
    wj=`cat countTotalExample.txt  | grep $i`    
    if [ ! $wj ];then 
        echo -e "\e[34m $i"+++++++"$j\e[37m"
        pig -p input=$i countTotalExample.pig >> countTotalExample.txt 
        if [ $? != 0 ];then
            echo \(${i} ,${j},0\) >> countTotalExample_failed.txt
        fi
    else
        continue 
    fi
done
