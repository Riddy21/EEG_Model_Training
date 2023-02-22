
## 10th attempt - More recurrent layers larger sample

### Changes made
- Trying the model with different dataset found online
    - https://www.nature.com/articles/sdata2018211
- Using the LR hand paradigm
- Data inforamtion:
    - Original model, 170 samples per prediction
    - 4 Channels
- 4 Channels seperated didn't work, putting 4 channels together
- GRU Recurrent network
- learning rate of 0.01

### Expected results
- See if we can get more validation and training data correlation

### Issues noticed
- Worked well with larger batch size, however accuracy stuck at 50%
 
