#2016-2017 PERSONAL PROJECTS: TurtleChat!
#WRITE YOUR NAME HERE!

#####################################################################################
#                                   IMPORTS                                         #
#####################################################################################
#import the turtle module
import turtle
from turtle_chat_client import Client
from turtle_chat_widgets import Button, TextInput
#import the Client class from the turtle_chat_client module
#Finally, from the turtle_chat_widgets module, import two classes: Button and TextInput
luna=turtle.Screen()
luna.bgpic("luna.gif")
#####################################################################################
#####################################################################################

#####################################################################################
#                                   TextBox                                         #
#####################################################################################
#Make a class called TextBox, which will be a subclass of TextInput.
#Because TextInput is an abstract class, you must implement its abstract
#methods.  There are two:
#
#draw_box
#write_msg
#
#Hints:
#1. in draw_box, you will draw (or stamp) the space on which the user's input
#will appear.
#
#2. All TextInput objects have an internal turtle called writer (i.e. self will
#   have something called writer).  You can write new text with it using code like
#
#   self.writer.write(a_string_variable)
#
#   and you can erase that text using
#
#   self.writer.clear()
#
#3. If you want to make a newline character (i.e. go to the next line), just add
#   \r to your string.  Test it out at the Python shell for practice
class TextBox(TextInput):
    def draw_box(self,pos=(0,-200),width=200,height=100):
        self.box=turtle.clone()
        self.box.speed(0)
        self.box.hideturtle()
        self.box.penup()
        self.box.goto(-100,-200)
        self.box.pendown()
        self.box.goto(-100,-100)
        self.box.goto(100,-100)
        self.box.goto(100,-200)
        self.box.goto(-100,-200)
       
        
    def write_msg(self):
        
        '''self.writer=turtle.clone()
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(-80,0)
        self.writer.showturtle()
        self.writer.pendown()'''
        self.writer.hideturtle()
        self.writer.goto(-90,-120)
        self.writer.clear()
        self.writer.write(self.new_msg)
        

        
        
        
        


        
        
        
        
        
        
        
#####################################################################################
#####################################################################################

#####################################################################################
#                                  SendButton                                       #
#####################################################################################
        
#Make a class called SendButton, which will be a subclass of Button.
#Button is an abstract class with one abstract method: fun.
#fun gets called whenever the button is clicked.  It's jobs will be to
#
# 1. send a message to the other chat participant - to do this,
#    you will need to call the send method of your Client instance
# 2. update the messages that you see on the screen
#
#HINT: You may want to override the __init__ method so that it takes one additional
#      input: view.  This will be an instance of the View class you will make next
#      That class will have methods inside of it to help
#      you send messages and update message displays.
class SendButton(Button):
    def __init__(self,view,my_turtle=None,shape=None,pos=(0,-210)):
        if my_turtle ==None :
            self.turtle=turtle.clone()
        else:
            self.turtle=my_turtle

        self.turtle.speed(0)
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(pos)
        screen=turtle.Screen()

        if shape is None:
            self.turtle.shape('square')
            self.turtle.shapesize(1,5)
        else:
            turtle.addshape(shape)
            self.turtle.shape(shape)
        self.turtle.showturtle()
        self.turtle.onclick(self.fun) 
        turtle.listen()
        self.view=view
    def fun(self,x=None,y=None):
        self.view.send_msg()
        
        
        
        
#####################################################################################
#####################################################################################


##################################################################
#                             View                               #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.
#
#Read the comments below for hints and directions.
##################################################################
##################################################################
class View:
    turtle.setup(width=400, height=600, startx=None, starty=None)


    def __init__(self,username='Me',partner_name='Partner',):

        _MSG_LOG_LENGTH=5
        _SCREEN_WIDTH=300
        _SCREEN_HEIGHT=600
        _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))
        '''
        :param username: the name of this chat user
        :param partner_name: the name of the user you are chatting with
        '''
        ###
        #Store the username and partner_name into the instance.
        ###
        self.username=username
        self.partner_name=partner_name
        

        ###
        #Make a new Client object and store it in this instance of View
        #(i.e. self).  The name of the instance should be my_client
        ###
        

        my_client=Client()
        self.my_client=my_client
        
        
        
        

        ###
        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.
        ###

        #turtle.setup(width=400, height=600, startx=None, starty=None)
        
        

        ###
        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.msg_queue=[]
        ###

        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase
        #and write messages for each
        ###
        import turtle
        turtle.clear()
        self.luna_msg=turtle.clone()
        self.luna1=turtle.clone()
        self.luna2=turtle.clone()
        self.luna3=turtle.clone()
        self.luna4=turtle.clone()
        

        ###
        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###
        Text_Box=TextBox()
        Send_Button=SendButton(view=self)
        self.Text_Box=Text_Box
        self.Send_Button=Send_Button
        turtle.write(Text_Box.new_msg)
         
        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###

    def send_msg(self):
        '''
        You should implement this method.  It should call the
        send() method of the Client object stored in this View
        instance.  It should also update the list of messages,
        self.msg_queue, to include this message.  It should
        clear the textbox text display (hint: use the clear_msg method).
        It should call self.display_msg() to cause the message
        display to be updated.
        '''
        
        self.my_client.send(self.Text_Box.new_msg)
        self.msg_queue.append(self.Text_Box.new_msg)
        self.Text_Box.clear_msg()
        self.display_msg()
        

    def get_msg(self):
        return self.textbox.get_msg()

    

    def setup_listeners(self):
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''
        pass

    def msg_received(self,msg):
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''
        print(msg) #Debug - print message
        show_this_msg=self.partner_name+' says:\r'+ msg
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
        #
        #Then, call the display_msg method to update the display
        self.msg_queue.append(new_msg)
        

    def display_msg(self):
        #self.display_msg=display_msg()
        self.luna_msg.clear()
        self.luna_msg.penup()
        self.luna_msg.speed(0)
        self.luna_msg.goto(-90,0)
        self.luna_msg.write(self.msg_queue[-1])
        self.luna_msg.hideturtle()
        

    def get_client(self):
        return self.my_client
##############################################################
##############################################################


#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################
if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        #msg_in=my_view.my_client.receive()
        msg_in=my_view.get_client().receive()
        if not(msg_in is None):
            if msg_in==Client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()
