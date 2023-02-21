
## 8th attempt - CNN Experimentation

### Attempt Info
- Trying the model with different dataset found online
    - https://www.nature.com/articles/sdata2018211
- Using the LR hand paradigm
- Data inforamtion:
    - Original model, 34 samples per prediction
    - 4 Channels
- Changing the input data shape
    - from (frame, sample, height, channel)
    - to (channel, frame, sample, height)
- Experimenting different CNN architectures to find the optimal
    - Trying to add more layers to the CNN
    - Changing CNN sizing to see effect
    - Changing CNN stride size and kernel size and see effect

### Expected results
- See if we can get more validation and training data correlation

### Issues noticed
- Looks like it's training slower
- Higher correlation between training and validation
- Longer training time
- Same final validation accuracy
