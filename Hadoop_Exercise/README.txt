For this exercise, I just used the Hadoop Streaming API with Python, haven't
use java for a while.
The command I am using is like following:

bin/hadoop jar contrib/streaming/hadoop-*streaming*.jar \
-file /home/fu/workspaces/hpy/ex3/mapper.py  -mapper /home/fu/workspaces/hpy/ex3/mapper.py \
-file /home/fu/workspaces/hpy/ex3/reducer.py -reducer /home/fu/workspaces/hpy/ex3/reducer.py \
-input /home/fu/workspaces/hadoop/input/wikipedia.txt -output /home/fu/workspaces/hpy/output3

