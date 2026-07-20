# Feedback published by a robot abstraction layer describing what the robot
# is currently doing in response to BCI commands. Robot-independent.

std_msgs/Header header

# Execution status values
uint8 IDLE=0
uint8 EXECUTING=1
uint8 SUCCEEDED=2
uint8 REJECTED=3
uint8 ERROR=4

# Identifier of the robot producing this state, e.g. "robotic_hand"
string robot_id

# Gesture currently held or being executed (BCICommand gesture constant)
uint8 current_gesture

# One of the status constants above
uint8 status

# Human-readable detail for logging and debugging
string message
