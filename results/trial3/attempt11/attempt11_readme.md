
## 11th attempt - Cutting the training samples to 70 Hz

### Changes made
- Trying the model with different dataset found online
    - https://www.nature.com/articles/sdata2018211
- Using the LR hand paradigm
- Data inforamtion:
    - Original model, 170 samples per prediction
    - 4 Channels
- Trying LSTM and original architecture
- Simple CNN network

### Expected results
- See if we can get more validation and training data correlation

### Issues noticed
- Cuttoff starts at about 40% accuracy doesn't work very well
- LSTM is very unstable to train
 
