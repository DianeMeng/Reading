#!/bin/bash
filename=$1

cat $filename |grep 'image|dates' > dates/images
imageresult=$(~/lib/python/bin/python2.7 dates.py dates/images )
echo -e $imageresult >> result/$filename

cat $filename |grep 'video|dates' > dates/video
videoresult=$(~/lib/python/bin/python2.7 dates.py dates/video )
echo -e $videoresult  >> result/$filename


cat $filename |grep 'audio|dates' > dates/audio
audioresult=$(~/lib/python/bin/python2.7 dates.py dates/audio )
echo -e $audioresult  >> result/$filename

cat  $filename | grep 'contacts' > dates/contacts
contactsresult=$(~/lib/python/bin/python2.7 contacts.py dates/contacts )
echo -e $contactsresult  >> result/$filename

#split event field
cat  $filename | grep -v 'dates\|contacts' > dates/splitevent
spliteventresult=$(~/lib/python/bin/python2.7 splitevent.py dates/splitevent )
echo -e $spliteventresult  >> result/$filename
