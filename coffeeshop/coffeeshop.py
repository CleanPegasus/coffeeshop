import keras
from slackclient import SlackClient



class NoSlacksForYou(Exception):
    pass

class Slacker(object):

    
    connection = None

    def __init__(self, token = None):

        try:

            connection = SlackClient(token)
            

        except:

            raise NoSlacksForYou("Could not authenticate with this token")

    def sendMessage(self, channel_name = None, message = None, token = None):

        if channel_name == None:
            raise NoSlacksForYou("Please specify valid channel")

        if message == None:
            raise NoSlacksForYou("Please Specify the message")

        try:

            connection = SlackClient(token)

            api_call = connection.api_call("channels.list", exclude_archives = 1)
            channels = api_call.get('channels')

            for channel in channels:

                if channel.get('name') == channel_name:

                    channel_id = channel.get('id')

            api_call = connection.api_call("chat.postMessage", channel = channel_id, text = message, username = "Coffeeshop")


        except:
            raise NoSlacksForYou('Could not send this message')
        


SCLK = Slacker()

            


class Coffeeshop(keras.callbacks.Callback):

    @staticmethod

    def __init__(self, token = None, channel_name = None, epoch_num = 1):

        self.token = token
        self.channel_name = channel_name
        self.epoch_num = epoch_num

    def on_train_begin(self, logs={}, secret = None):
        
        self.losses = []
        self.accuracy = []
        self.num_epochs = []


        

    def on_epoch_end(self, epoch, logs={}):

        self.losses.append(logs.get('loss'))
        self.accuracy.append(logs.get('acc'))
        self.num_epochs.append(epoch)
        
        
        if(epoch % self.epoch_num == 0):

            self.loss = float("{0:.6f}".format(self.losses[-1]))
            self.acc = float("{0:.6f}".format(self.accuracy[-1]))

            self.message = " Epoch: {} \n Loss: {} \n Accuracy: {}".format(epoch, self.loss, self.acc)

            SCLK.sendMessage(channel_name = self.channel_name, message = self.message, token = self.token)

    def on_train_end(self, logs = {}):

        self.message = "Model Trained \n No. of epochs: {} \n Loss value: {} \n Accuracy : {}".format(self.num_epochs[-1]+1, self.losses[-1], self.accuracy[-1])

        SCLK.sendMessage(channel_name = self.channel_name, message = self.message, token = self.token)

