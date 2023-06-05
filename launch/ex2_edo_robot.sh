source /home/emanuele/Desktop/source_noetic.sh
. /home/emanuele/rpc_ws/devel/setup.bash
cd /home/emanuele/rpc_ws
roslaunch edo_description edo_upload.launch & roslaunch edo_description test.launch
