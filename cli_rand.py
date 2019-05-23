from cmd import Cmd
import random
class MyPrompt(Cmd):
    prompt = 'random-cli> '
    intro = "Welcome To the Random CLi Application, please enter <rand> to print the random numbers from [1-10]" 
    def do_rand(self, inp):
        while True:
            print("Random Number from [1-10] : ", random.randint(1, 10))
        return True

MyPrompt().cmdloop()
