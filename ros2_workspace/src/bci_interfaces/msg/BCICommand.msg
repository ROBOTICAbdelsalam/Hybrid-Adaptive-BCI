# Semantic gesture command produced by the EEG/AI pipeline bridge.
#
# This message is robot-INDEPENDENT: it names an intended gesture, not a
# joint configuration. Each robot's abstraction layer maps these gestures
# onto its own motion. A robotic hand, a UR5e or a Franka Panda all consume
# the same BCICommand without any change to the EEG or AI code.

std_msgs/Header header

# Gesture identifiers
uint8 REST=0
uint8 OPEN_HAND=1
uint8 CLOSE_HAND=2
uint8 PINCH_GRIP=3
uint8 POWER_GRIP=4
uint8 POINT=5

# Requested gesture (one of the constants above)
uint8 gesture

# Model confidence for this gesture in the range [0.0, 1.0]
float32 confidence

# Origin of the command, e.g. "eeg_ai_pipeline" or "manual_override"
string source
