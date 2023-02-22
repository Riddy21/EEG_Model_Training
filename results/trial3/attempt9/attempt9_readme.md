
## 9th attempt - Multi channel Test

### Changes made
- Trying the model with different dataset found online
    - https://www.nature.com/articles/sdata2018211
- Using the LR hand paradigm
- Data inforamtion:
    - Original model, 34 samples per prediction
    - 4 Channels
- Changing the input data shape
    - from (frame, sample, height, channel)
    - to (frame, channel, sample, height)
- Building a new model
    - Seperating model into 4 different channels before running
- Experimenting different CNN architectures to find the optimal
    - Trying to add more layers to the CNN
    - Changing CNN sizing to see effect
    - Changing CNN stride size and kernel size and see effect
- GRU Recurrent network
- learning rate of 0.01

### Expected results
- See if we can get more validation and training data correlation

### Issues noticed
- Looks like training could not pass 50% accuracy
    - likely means that model with multiple channels could not understand the data
- Increasing the sample size seems to improve the accuracy by can't do more than that
 
