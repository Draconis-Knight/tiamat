import discord
from discord.ext import commands


command_tally = {

} 

class CommandEvents(commands.Cog):
    def __init__(self, client):
        self.client = client

        '''
        Command Error, Successful, and Invocation Handling
        '''

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx.command.name '+' 'was invoked incorrectly.')
        print(error)

    @commands.Cog.listener()
    async def on_command(self, ctx):
        if ctx.command is not None:
            if ctx.command.name in commands_tally:
                commands_tally[ctx.command.name] += 1
            else:
                commands_tally[ctx.command.name] = 1
            print(commands_tally)
    
    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(ctx.command.name '+' 'was invoked successfully.')

                  
def setup(client):
    client.add_cog(CommandEvents(client))
