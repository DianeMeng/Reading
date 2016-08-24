for i in `cat deletelist`
do
    x+=$i"\|"    
done
x=${x%\\|}
echo $x

for j in `cat completelist`
do
    y+=$j"\|"
done
y=${y%\\|}
echo $y

for file in `ls ../filterTime/output`
do
    echo $file
    finish=`ls filterout|grep $file`
    #echo $finish
    if [ ! $finish ];then
        echo '----------'
        echo $finish

        before=`date +%s`
        echo `date`
        cat ../filterTime/output/$file|grep -v "$x" >>  filterout/$file
        #cat filterTime/output/$file|grep  "$x" >>  filterout/$file'cc'
        cat ../filterTime/output/$file|grep  "$y"  >>  filterout/$file
        cat filterout/$file |sort -t ';' -k 3 > filesout/$file
        sh specialevent.sh filesout/$file 
        rm filterout/$file
        after=`date +%s`
        let "diff=${after}-${before}"
        echo $diff
        #mv filesout/$file filesout/${file%.gz}
        #gzip filesout/${file%.gz}
    else
        continue
    fi

done
