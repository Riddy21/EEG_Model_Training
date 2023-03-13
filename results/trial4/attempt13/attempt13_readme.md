
## 13th attempt

### Changes made
- Trying new model new training data from interactive movement dataset
- Window Size experiment
- Improving the model by adding more spacial and feature filters
- Shifting window to be more forwards before action
- SEGMENT_WINDOW_SIZE = 300 #  1.5s
- ACTIVE_WAIT_PERIOD = 400 # 3s
- ACTIVE_HOLD_PERIOD = 200 # 1s for dealing with accidental presses
- Balanced
- Have disconnect
- 2000 epochs, learning rate of 0.0001

### Expected results
- See if it performs any worse with our Muse model or better than recorded data
- See if it adapts to taking off the headset

### Issues noticed
