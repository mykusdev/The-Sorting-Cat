import discord
import os
import random
from replit import db
from keep_alive import keep_alive
#from replit import db


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
##client = discord.Client(intents=discord.Intents.default())



@client.event
async def on_ready():
  print('I have finally arrived. It\'s me, {0.user}'.format(client))
  # game = discord.Game(name='!help')
  # await client.change_presence(activity=game)
  activity = discord.Activity(type=discord.ActivityType.listening, name='!help')
  await client.change_presence(activity=activity)
 

@client.event
async def on_guild_available(guild):
    krill_role = discord.utils.get(guild.roles, name='House Krill')
    manta_role = discord.utils.get(guild.roles, name='House Manta')
    crab_role = discord.utils.get(guild.roles, name='House Crab')
    jelly_role = discord.utils.get(guild.roles, name='House Jellyfish')

    if not krill_role:
        krill_role = await guild.create_role(name='House Krill', color=discord.Color(0xEC7063))
    if not manta_role:
        manta_role = await guild.create_role(name='House Manta', color=discord.Color(0x82E0AA))
    if not crab_role:
        crab_role = await guild.create_role(name='House Crab', color=discord.Color(0x3498DB))
    if not jelly_role:
        jelly_role = await guild.create_role(name='House Jellyfish', color=discord.Color(0xF1C40F))

    roles_to_add = [krill_role, manta_role, crab_role, jelly_role]
    for role in roles_to_add:
        if role not in guild.roles:
            await guild.create_role(name=role.name, color=role.color)

    # Code to assign the roles to users can be added here

  
#@client.event
#async def on_member_join(member):
  #  await dm_about_roles(member)

@client.event
async def on_message(message):
  
  if message.author == client.user:
    return

  
  msg = message.content
  reply = message.channel.send

  if msg.startswith("!help"):
    await reply("DM\'ed you")
    await message.author.send("\nHere are the commands everyone can use \n\n **!assignhouse** - *Sorts you into a house.* \n **!board** - *Shows you the current house leaderboard* \n **!krillpoints** - *Check the points of House Krill* \n **!mantapoints** - *Shows the points of House Manta* \n **!crabpoints** - *Shows the points of House Crab* \n **!jellypoints** - *Shows the points of House Jellyfish* \n **!hug *user*** - *Using this command you can hug someone* \n **!cook *user*** - *Using this command you can cook someone*\n **!yeet *user*** - *Using this command you can yeet someone :)* \n\nCOMMANDS FOR ROLE **GIVES POINTS**\n\n **!addkrill *points*** - *adds specified points to House Krill*\n **!addmanta *points*** - *adds specified points to House Manta*\n **!addcrab *points*** - *adds specified points to House Crab*\n **!addjelly *points*** - *adds specified points to House Jellyfish*\n **!setall *points*** - *sets points of all houses to specified points*")

  hello_kitty = ["HELLO MR CAT", "HELLO MR KITTY CAT", "HI MR CAT", "HII MR CAT", "HIII MR CAT", "HELLO MR KITTY CAT", "HELLO MR KITTY", "HELLOOO MR KITTY CAT", "HEY MR CAT", "HEYY MR CAT", "HEY MR KITTY CAT", "HEYYY MR CAT", "HEYYY MR KITTY CAT", "HOLA MR CAT", "HOLA MR KITTY CAT", "HELLO THERE MR CAT", "HELLO THERE MR KITTY CAT", "KONNICHIWA MR CAT", "KONNICHIWA MR KITTY CAT", "BONJOUR MR CAT", "BONJOUR MR KITTY CAT", "YO MR CAT", "YO MR KITTY CAT"]
  kitty_waves = ["Hello young one!", "Yo!!", "Hello! meow!", "Hi!!", "Hiiiiii!!!!", "Hiiii!!", "Hiii!!", "Hoiii!!", "Hola!", "Bonjour!!", "Henlooo!!", "Hiii!! :smirk_cat:"]
  if any(word in msg.upper() for word in hello_kitty):
  #if message.content.startswith('Hi Mr Cat'):
    await reply(random.choice(kitty_waves))


  morning_cat = ["good morning mr cat", "good morning mr kitty cat", "goodmorning mr cat", "goodmorning mr kitty cat", "goodmorningg mr cat", "goodmorninggg mr cat", "goodmorningg mr kitty cat", "goodmorninggg mr kitty cat", "morning mr cat", "morning mr kitty cat", "morningg mr cat", "morninggg mr cat"]
  kitty_morning = ["GOOD MORNING!!", "Good Morningg", "goodmorning", "Good Morninggg!!", "Hiiii!! Good Morning!!", "Good Morning Kiddo", "I don't sleep. But good morning.", "It's morning? Okie. Goodmorning!!!", "Morning Good!!", "Morning!", "morning", "Morninggg!!", "MORNING!!"]
  if any(word in msg.lower() for word in morning_cat):
    await reply(random.choice(kitty_morning))

  night_cat = ["good night mr cat", "good night mr kitty cat", "goodnight mr cat", "goodnight mr kitty cat", "goodnightt mr cat", "goodnighttt mr cat", "goodnightt mr kitty cat", "goodnighttt mr kitty cat", "night mr cat", "night mr kitty cat", "nightt mr cat", "nighttt mr cat"]
  kitty_night = ["GOOD NIGHT!!", "Good night! Sleep well", "goodnight", "Good Nightt!!", "Good Morning!! Sweet dreams!", "Good Night Kiddo", "I won't sleep. But still good night.","Sleep well! Sweet Dreams!", "It's night already? Okie. Goodnight!!!", "Sleep well kid!!", "Night!", "night", "Nigtt!!", "Nighttt!!"]
  if any(word in msg.lower() for word in night_cat):
    await reply(random.choice(kitty_night))

  affection = ["i love you mr cat", "i love u mr cat", "i luv you mr cat", "i luv u mr cat", "love you mr cat", "lov u mr cat", "luv you mr cat", "love u mr cat", "luv u mr cat", "me cat i love you", "mr cat i love u", "mr cat i luv u", "mr cat i luv you"]
  affection_reply1 = ["love you too ", "luv you too ", "luv u too ", "love you 2 "]
  affection_reply2 = ["chibi. ", "chibbi. ", "kiddo. ", "kid. ", "young one. ", "little one. ", "smol one. ", "smol chibi. "]
  affection_reply3 = ["hehe.", "ehehe.", ":kissing_cat:", ":smile_cat:", ":smiley_cat:", ":smirk_cat:"]

  if any(word in msg.lower() for word in affection):
    await reply(random.choice(affection_reply1) + random.choice(affection_reply2) + random.choice(affection_reply3))
  

  nomnom =["nom", "nomnom", "nomnomnom", "nom nom", "nom nom nom", "nomnomnomnom", "nom nom nom nom"]
  nomnom_chibi =["nomnomnom", "nom nom", "nomnom", "nomnom", "nom nom nom", "nom nom NOM", "nom :smirk_cat:", "nom", "nom nomnom", "nomnom nomnom", "*nomnomnom*", "**nomnomnom**", "***nomnomnom***"]
  if any(word in msg.lower() for word in nomnom):
    await reply(random.choice(nomnom_chibi))
  
  howareyou =["how are you mr cat", "how are you mr kitty cat", "how you doing mr cat", "how are you doing mr cat", "how are you doing mr kitty cat", "how are you mr kitty", "how have you been mr cat", "how have you been mr kitty cat", "how r u mr cat", "hru mr cat", "how are u mr cat"]
  iamfine =["I'm great. Thanks for asking.", "I'm fine. Thank you for asking.", "I'm doing well. Thanks.", "I am marvellous.", "I'm really good. Thanks for asking.", "I'm doing alright. Thanks for asking. :smiley_cat:", "I'm awesome! Thanks for asking.", "Great! Thank u for asking.", "Good! Thanks!"]
  howboutyou =["How are you?", "HBU?", "hbu?", "hbu", "How about you?", "How have you been?", "How have you been doing?", "How are you??!", "How are u?", "How are ya?"]
  if any(word in msg.lower() for word in howareyou):
    await reply(random.choice(iamfine))
    await reply(random.choice(howboutyou))

  barking = ["woof woof", "woof wooff", "bark bark"]
  barking_reply1 = ["Woof woof! ", "Pfft!! ", "Really? ", "Dogs?", "Hehe. ", "I am a Krill Cat. ", "Pfft!! WTF Meoww. ", "Cute! "]
  barking_reply2 = ["I was raised alongside krills. Mere dogs do not scare me", "You need to do better than that to scare me" , "Hahaha", "XD", "I come from the darkness. An adorable Woof cannot scare me.", "I've always found dogs interesting.", "I'll send you to Eden for a month when my contract with Muffin ends.", "I'll unalive you :D"]

  if any(word in msg.lower() for word in barking):
    await reply(random.choice(barking_reply1) + random.choice(barking_reply2))
  
    
  meeow = ["MEOW", "MEOWW", "MEOWWW", "MEEOWY", "MEOWY", "MEOWYY"]
  meeowy = ["meow!!", "Meoww!!", "meow!", "MEOW!!", ":smirk_cat:", ":smile_cat:", ":smiley_cat:", ":kissing_cat:", "Meow!! :smirk_cat:"]

  if any(word in msg.upper() for word in meeow):
    await reply(random.choice(meeowy))

  
  if msg.lower().startswith("!eat "):
    victim = msg.lower().split("!eat ",1)[1]
    await reply("nomnomnom. *eats* " + "*" + victim + "*")
  # elif msg.startswith("Eat "):
  #   victim = msg.split("Eat ",1)[1]
  #   await reply("nomnomnom. *eats* " + "*" + victim + "*")
  hug_me = ["hug me mr cat", "mr cat hug me", "i want a hug", "i need a hug"]
  if any(msg.lower().startswith(word) for word in hug_me):
    await reply("Awww. *hugs* " + message.author.mention)
  elif msg.lower().startswith("mr cat hug "):
    victim = msg.lower().split("mr cat hug ",1)[1]
    await reply("*HUGS* "  + victim.upper())
  
  if msg.lower().startswith("!hug "):
    victim = msg.lower().split("!hug ",1)[1]
    await reply(message.author.mention + " *hugs* "  + victim.capitalize())


  scared_cat = ["Nuuuuuuuuuu!! Not today!!!!", "Please no! Not today!", "Again?! Please no! :cry"]
  recipe1 = ["*marinates* ","*heats up oil* ", "*heats upoil to 3000 degrees Celcius*", "*heats up oil to 2999 degrees Celcius*", "*seasons with salt and pepper* ", "*prepares for deep frying*"]
  recipe2 = [" *with garnish*", " *with salad*", " *with wine*", " *along with dessert*", " *with mayonnaise*", " *with baked potatoes*", " *with bread*", " *with mashed potatoes*", " *with French fries*", " *with mushroom*", " *with meatballs*"]
  if msg.startswith("!cook " + client.user.mention) or msg.lower().startswith("!cook mr cat"):
    await reply(random.choice(scared_cat))
  elif msg.startswith("!cook ") or msg.startswith("!Cook ") or msg.startswith("!COOK "):
    victim = msg.lower().split("!cook ", 1)[1]
    await reply("*Takes* " + victim.capitalize())
    await reply(random.choice(recipe1))
    await reply("*fries* " + victim.capitalize())
    await reply("*serves* " + victim.capitalize() + random.choice(recipe2))
  
  if msg.startswith("!yeet "):
    victim = msg.split("!yeet ",1)[1]
    await reply("YEEEEEEEEEEEEEETTTTT. *yeets* " + "*" + victim.capitalize() + "*")
  # elif msg.upper().startswith("!YEET "):
  #   victim = msg.split("!Yeet ",1)[1]
  #   await reply("YEEEEEEEEEEEEETTTTTTT. *Yeets* " + "*" + victim.upper() + "*")
  # elif msg.startswith("YEET "):
  #   victim = msg.split("YEET ",1)[1]
  #   await reply("YEEEEEEEEEEETTTTTT. *YEETS* " + "*" + victim.upper() + "*")
    
  
  
    
  houuses = ["what are all the houses", "what are the colours of the houses", "what are the colours of all the houses","what are the house colours","what are the house names", "i wanna know more about the houses", "what are the colours of all the houses", "tell me more about the houses", "tell us about the houses", "tell us more about the houses"]
  houses_ans = "There are 4 houses \n\nThe **House Krill**. A house made after an ancient darkness. Their colour is **Red**. :red_square: \n\nThe **House Manta**. A house that was created after an ancient light. Their colour is **Green**. :green_square: \n\nThe **House Crab**. A house made after an ancient darkness. Their colour is **Blue**. :blue_square: \n\nThe **House Jellyfish**. A house made after an ancient light. Their colour is **Yellow**. :yellow_square:"
  if any(word in msg.lower() for word in houuses):
    await reply(houses_ans)

  
  grateful = ["THANK YOU MR KITTY CAT","THANK YOU MR CAT", "THANKS MR KITTY CAT", "THANKS MR CAT", "THANK U MR CAT"]
  pleased = ["No problem kiddo!! :smiley_cat:", "You\'re welcome child! :smile_cat:", "Anytime!! :smirk_cat:", ":heart_eyes_cat:"]

  #general = client.get_channel(917819568628580407)
  
  if any(word in msg.upper() for word in grateful):
    await reply(random.choice(pleased))

  if any(role.name == 'Gives Points' for role in message.author.roles) and msg.startswith("!addkrill"):
    points = int(msg.split("!addkrill ",1)[1])
    if "krill_points" in db.keys():
      k_point = int(db["krill_points"])
      k_point += points
      db["krill_points"] = str(k_point)
    else:
      db["krill_points"] = str(points)

    #await general.send("testing a new feature " + str(points))
    await reply(str(points) + " points awarded to House Krill")
    await reply(db["krill_points"])
  

  if msg.startswith("!krillpoints"):
    await reply("Current points of House Krill : " + db["krill_points"])

  if any(role.name == 'Gives Points' for role in message.author.roles) and msg.startswith("!addmanta"):
    points = int(msg.split("!addmanta ",1)[1])
    if "manta_points" in db.keys():
      point = int(db["manta_points"])
      point += points
      db["manta_points"] = str(point)
    else:
      db["manta_points"] = str(points)

    await reply(str(points) + " points awarded to House Manta")
    await reply("Current points of House Manta : " + db["manta_points"])
    
  if msg.startswith("!mantapoints"):
    await reply(db["manta_points"])
    

  if any(role.name == 'Gives Points' for role in message.author.roles) and msg.startswith("!addcrab"):
    points = int(msg.split("!addcrab ",1)[1])
    if "crab_points" in db.keys():
      point = int(db["crab_points"])
      point += points
      db["crab_points"] = str(point)
    else:
      db["crab_points"] = str(points)

    await reply(str(points) + " points awarded to House Crab")
    await reply("Current points of House Crab : " + db["crab_points"])
  
    
  if msg.startswith("!crabpoints"):
    await reply(db["crab_points"])


  if any(role.name == 'Gives Points' for role in message.author.roles) and msg.startswith("!addjelly"):
    points = int(msg.split("!addjelly ",1)[1])
    if "jelly_points" in db.keys():
      point = int(db["jelly_points"])
      point += points
      db["jelly_points"] = str(point)
    else:
      db["jelly_points"] = str(points)

    await reply(str(points) + " points awarded to House Jellyfish")
    await reply("Current points of House Jellyfish : " + db["jelly_points"])

  if msg.startswith("!jellypoints"):
    await reply(db["jelly_points"])

  if any(role.name == 'Gives Points' for role in message.author.roles) and (msg.startswith("!addkrill") or msg.startswith("!addmanta") or msg.startswith("!addcrab") or msg.startswith("!addjelly")):
    return
  elif any(role.name != 'Gives Points' for role in message.author.roles) and (msg.startswith("!addkrill") or msg.startswith("!addmanta") or msg.startswith("!addcrab") or msg.startswith("!addjelly")):
    await reply("You do not have the necessary permissions to add points.")
    
  if msg == '!board':
    point_krill = int(db["krill_points"])
    point_manta = int(db["manta_points"])
    point_crab = int(db["crab_points"])
    point_jelly = int(db["jelly_points"])
    house_names = ["Krill", "Manta", "Crab", "Jellyfish"]
    house_points = [point_krill, point_manta, point_crab, point_jelly]
    await reply("CURRENT LEADERBOARD")
    i = 1
    while i <= 4:
      await reply("House " + house_names[house_points.index(max(house_points))] + " : " + str(max(house_points)))
      house_names.remove(house_names[house_points.index(max(house_points))])
      house_points.remove(max(house_points))
      
      i += 1

  if any(role.name == 'Gives Points' for role in message.author.roles) and msg.startswith("!setall"):
    points = int(msg.split("!setall ",1)[1])
    db["krill_points"] = str(points)
    db["manta_points"] = str(points)
    db["crab_points"] = str(points)
    db["jelly_points"] = str(points)
    await reply("Points of all houses have been set to " + str(points))
    
  
  assign_krill = ["I smell the scent of a krill from this child. Your house shall now be **House Krill** :red_square:", "I sense the spirit of a krill from this child. You shall be in **House Krill** :red_square:", "A very familiar scent from this one. You shall now be in **House Krill** :red_square: kiddo", "Holy Sh-...this child smells just like a krill. I will be putting you in **House Krill** :red_square:", "I know this scent the most. You'll be in **House Krill** :red_square:", "It is a little difficult to decide on this one. You smell a bit like a Krill and a bit like a Crab. But mostly like a Krill. So kid you'll be in **House Krill** :red_square:", "Do you spend most your time in Golden Wasteland? You smell like a Krill. I'll put you in **House Krill** :red_square:", "I sense the spirit of a brave warrior from you kid. You'll be in **House Krill** :red_square:", "I smell the scent of a krill from this child. Your house shall now be **House Krill** :red_square:"]

  assign_crab = ["I sense mischief from you. I'll put you in **House Crab** :blue_square:", "I feel like you're a mischievous child. Your house shall be **House Crab** :blue_square:", "You definitely spend a lot of time with the crabs. It would only be fitting to put you into **House Crab** :blue_square:", "Looks like crabs attack you a lot. It would be funny if I put you into **House Crab** :blue_square: :smirk_cat:", "I smell the scent of a mischievous crab from you kid. I'll put you in **House Crab** :blue_square:", "You're definitely michievous. You'll be put in **House Crab** :blue_square:", "I sense the spirit of a mischievous child and an adventurer from you. But I think it's better to put you into **House Crab** :blue_square:", "It's difficult to decide the house for this one. But the scent of michief is strong with this one. I'll put you in **House Crab** :blue_square:", "You give off the scent of mischief. I will put you into **House Crab** :blue_square:"]

  assign_manta =["I sense the spirit of an adventurer from you. You should definitely be put in **House Manta** :green_square:", "I get the scent of a manta from you. I shall be putting you in **House Manta** :green_square:", "I get the smell of fresh air from you. I believe the house best for you shall be **House Manta** :green_square:", "You look like someone who loves adventures. I think **House Manta** :green_square: would be best for you", "I get the smell of clouds from you. You must love flying. The best house for you will be **House Manta** :green_square:", "Your light is bright, but not as bright as a Jellyfish. I also get the smell of clouds from you. I shall place you in **House Manta** :green_square:", "The scent of both a manta and a crab makes it difficult to decide. But I think **House Manta** :green_square: would be best for you kid.", "I smell the skies from this child. I shall put you into **House Manta** :green_square:"]

  assign_jellyfish =["You smell like the rain. I think it's best if I put you in **House Jellyfish** :yellow_square:", "I get the smell of Pertrichor from you. Your houses is going to be **House Jellyfish** :yellow_square:", "You smell just like when rain drops hit the light. I shall be putting you in **House Jellyfish** :yellow_square:", "The smell of fresh rain is strong with you. I'll put you in **House Jellyfish** :yellow_square:", "You smell like a Jellyfish. I shall put you in **House Jellyfish** :yellow_square:", "The smell of light and water. I will put this one in **House Jellyfish** :yellow_square:", "Your scent is similar to that of a Jellyfish. it's only natural I'll put you in **House Jellyfish** :yellow_square:", "Your light is quite bright. I think **House Jellyfish** :yellow_square: would be perfect for you.", "The smell of rain..... You'll be in **House Jellyfish** :yellow_square:"]
  
  if message.content.startswith("!assignhouse"):
    member = message.author

        # Get the role objects for the roles you want to check
    roles_to_check = ['House Krill', 'House Manta', 'House Crab', 'House Jellyfish']
    roles = [discord.utils.get(message.guild.roles, name=name) for name in roles_to_check]

    # Check if the member has any of the roles
    has_role = False
    for role in roles:
        if role in member.roles:
            has_role = True
            break

    # Send a message based on the result
    if has_role:
        await reply("You are already in a house. You cannot join another house.")
    else:
   
      if "choose_house_no" in db.keys():
        house_no = db["choose_house_no"]
        h_no = random.choice(house_no)
        house_no.remove(h_no)
        db["choose_house_no"] = house_no
        print("first if ", h_no)
        print("\n Houses in list : " + str(len(house_no)))
        if len(house_no) == 0:
          house_no = ["House Krill", "House Manta", "House Crab", "House Jellyfish"]
          db["choose_house_no"] = house_no
          print("second if ", h_no)
          print("\n Houses in list : " + str(len(house_no)))
      else:
        house_no = ["House Krill", "House Manta", "House Crab", "House Jellyfish"]
        db["choose_house_no"] = house_no
        print("else ")
    
      server = client.get_guild(message.channel.guild.id)
      roles = [discord.utils.get(server.roles, name=h_no)]
      member = await server.fetch_member(message.author.id)  
      try:
        await member.add_roles(*roles, reason="House assigned by Sorting Cat.")
        
      except Exception as e:
        print(e)
        await message.channel.send("Error assigning roles.")
     
      await reply(message.author.mention)  
      if h_no == "House Krill":
        await reply(random.choice(assign_krill))
        await reply(file= discord.File('Krill2.jpeg'))
        await message.author.send(file= discord.File('Krill_motto.jpg'))
      elif h_no == "House Crab":
        await reply(random.choice(assign_crab))
        await reply(file= discord.File('Crab1.jpg'))
        await message.author.send(file= discord.File('Crab_motto.jpg'))
      elif h_no == "House Manta":
        await reply(random.choice(assign_manta))
        await reply(file= discord.File('Manta1.jpg'))
        await message.author.send(file= discord.File('Manta_motto.jpg'))
      elif h_no == "House Jellyfish":
        await reply(random.choice(assign_jellyfish))
        await reply(file= discord.File('Jellyfish1.jpg'))
        await message.author.send(file= discord.File('Jellyfish_motto.jpg'))
      

keep_alive()
client.run(os.environ['token2'])
