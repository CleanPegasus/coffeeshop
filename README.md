# Coffeeshop

This package sends your deep learning training loss and accuracy to your slack channel after every specified epoch.
It uses slackclient and keras python packages.

### Installation

>$ **pip install coffeeshop**


### Code sample

```python
from coffeeshop.coffeeshop import Coffeeshop

secret = 'xoxp-slacktoken'

# For sending metrics to channel.
channel_name = 'name_of_channel_to_be_posted'

histories = coffeeshop(token = secret, channel_name = channel_name, epoch_num = 5)

# For sending metrics to user.

user = 'User Name'

histories = coffeeshop(token = secret, user_name = user, epoch_num = 5)

## Add histories in the callbacks.

model.fit(X_train, Y_train, epochs = epochs, batch_size = batch_size,callbacks = [histories])

```

### Output sample

<img src="readme_resources/sample_output.jpeg">
</img>



#### Contact

[E-mail](arunk609@gmail.com)

[Github](https://github.com/CleanPegasus)

[LinkedIn](https://www.linkedin.com/in/arunkumar-l/)

