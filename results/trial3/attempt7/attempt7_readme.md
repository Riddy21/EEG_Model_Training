
## 7th attempt - new model

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

### Expected results
- See if we can get more validation and training data correlation

### Issues noticed
- Training seems to be unstable, goes back down to 40% after a while
- Trying with smaller learning rate
