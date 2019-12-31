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

    def sendMessage(self, channel_name = None, user_name = None, message = None, token = None):

        if (channel_name == None and user_name == None):
            raise NoSlacksForYou("Please specify valid channel or user")

        if message == None:
            raise NoSlacksForYou("Please Specify the message")

        try:

            connection = SlackClient(token)

            if(channel_name != None):

                api_call = connection.api_call("channels.list", exclude_archives = 1)
                channels = api_call.get('channels')

                for channel in channels:

                    if channel.get('name') == channel_name:

                        channel_id = channel.get('id')

            if(user_name != None):

                users = connection.api_call('users.list')

                users = users['members']

                for user in users:

                    if(user.get('real_name') != None):

                        if(user.get('real_name') == user_name):

                            channel_id = user.get('id')

            api_call = connection.api_call("chat.postMessage", channel = channel_id, text = message, username = "Coffeeshop")


        except:
            raise NoSlacksForYou('Could not send this message')
        


SCLK = Slacker()


class Coffeeshop(keras.callbacks.Callback):



    def __init__(self, token = None, channel_name = None, user_name = None, epoch_num = 1):

        self.token = token
        self.channel_name = channel_name
        self.epoch_num = epoch_num
        self.user_name = user_name

    def on_train_begin(self, logs={}, secret = None):
        
        self.losses = []
        self.accuracy = []
        self.val_losses = []
        self.val_accuracy = []
        self.num_epochs = []


    def on_epoch_end(self, epoch, logs={}):

        self.losses.append(logs.get('loss'))
        self.accuracy.append(logs.get('accuracy'))
        self.val_losses.append(logs.get('val_loss'))
        self.val_accuracy.append(logs.get('val_accuracy'))
        self.num_epochs.append(epoch)

        
        
        if(epoch % self.epoch_num == 0):

            self.loss = float("{0:.6f}".format(self.losses[-1]))

            if self.accuracy[-1] == None:
                self.acc = "Not Specified"
            else:
                self.acc = float("{0:.6f}".format(self.accuracy[-1]))

            if self.val_losses[-1] == None:
                self.val_loss = "Not Specified"
            else:
                self.val_loss = float("{0:.6f}".format(self.val_losses[-1]))

            if self.val_accuracy[-1] == None:
                self.val_acc = "Not Specified"
            else:
                self.val_acc = float("{0:.6f}".format(self.val_accuracy[-1]))
            
            #self.val_loss = float("{0:.6f}".format(self.val_losses[-1]))
            #self.val_acc = float("{0:.6f}".format(self.val_accuracy[-1]))


            self.message = " Epoch: {} \n Loss: {} \n Accuracy: {} \n Validation Loss: {} \n Validation Accuracy: {}".format(epoch, self.loss, self.acc, self.val_loss, self.val_acc)

            try:

                SCLK.sendMessage(channel_name = self.channel_name, user_name = self.user_name, message = self.message, token = self.token)

            except:

                NoSlacksForYou("Could not send the message")

    def on_train_end(self, logs = {}):

        if self.accuracy[-1] == None:
                self.acc = "Not Specified"
        else:

            self.acc = self.accuracy[-1]

        if self.val_losses[-1] == None:
                self.val_loss = "Not Specified"
        else:

            self.val_loss = self.val_losses[-1]

        if self.val_accuracy[-1] == None:
                self.val_acc = "Not Specified"
        else:

            self.val_acc = self.val_accuracy[-1]

        self.message = " Model Trained \n No. of epochs: {} \n Loss value: {} \n Accuracy Value: {} \n Validation Loss: {} \n Validation Accuracy: {}".format(self.num_epochs[-1]+1, self.losses[-1], self.acc, self.val_loss, self.val_acc)

        try:

            SCLK.sendMessage(channel_name = self.channel_name, user_name = self.user_name, message = self.message, token = self.token)

        except:

            NoSlacksForYou("Could not send the message")
