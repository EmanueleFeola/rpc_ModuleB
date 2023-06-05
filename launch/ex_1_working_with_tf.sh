cd /home/emanuele/rpc_ws
source devel/setup.bash
roslaunch learning_tf start_demo.launch & rosrun rviz rviz -d `rospack find turtle_tf`/rviz/turtle_rviz.rviz