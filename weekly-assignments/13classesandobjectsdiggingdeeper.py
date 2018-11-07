# WEEKLY GRADED ASSIGNMENT
# The code below contains a Chatbot class. A Chatbot is an object that can
# engage in rudimentary conversation with a human. You will be asked to
# define a subclass that inherits from this Chatbot superclass.

# First, run the code below to talk to the chatbot. Then look over the code
# to make sure you understand it.

# _________________________________________________________________________

# Your job is to make a subclass called BoredChatbot that inherits from
# Chatbot, but acts a little differently, in the following way:
#
# ----- A bored chatbot has a short attention span. When the human says
# ---------- something that is longer than 20 characters, it should respond
# ---------- by saying:
# ---------- "zzz... Oh excuse me, I dozed off reading your essay."
# ----- If, on the other hand, the human says something with a length of 20
# ---------- characters or less, then the bored chatbot should respond just
# ---------- like a normal chatbot would.
#
# Note that we are requiring you to use inheritance. Your new BoredChatbot
# class must be a subclass of the Chatbot class, and your subclass should
# only implement the things that make it distinct. (See the Inheritance
# chapter for a review of how this works.)

class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself."""
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"

class BoredChatbot(Chatbot):

    def response(self, prompt_from_human):
        if len(prompt_from_human) > 20:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return Chatbot.response(self, prompt_from_human)

sandy = BoredChatbot("Sandy")
human_message = input(sandy.greeting())
print(sandy.response(human_message))