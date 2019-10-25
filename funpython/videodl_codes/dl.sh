dest="QMSM_SJTU"
pypath="videodl_codes/dlpy.py"
vidid=51954299
dlis=(1 20 21 40 41 60 61 80 81 100)
#(101 120 121 140 141 160 161 180 181 200 201 220 221 240 241 253)
for i in $(seq 0 2 ${#dlis[@]})
do
	echo ${dlis[$i]} ${dlis[$((i+1))]}
        python3 $pypath https://www.bilibili.com/video/av$((vidid))/?p= ${dlis[$i]} ${dlis[$((i+1))]} $dest &
done
