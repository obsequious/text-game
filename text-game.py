from sys import exit

def living_room():
	print """
You are sitting in your living room. You haven't slept much, 
so you're not really at 100 percent. And just when you think
you might have things calmed down, you hear your baby crying
in your bedroom. Your wife's in there, trying to get some sleep.
She's got some big thing tomorrow. Still, you look at the tv.
You look at the door that  used to take you to the outside world.
What do you do?
	"""
	
	choice = raw_input("> ")
	
	if "tv" in choice or "watch" in choice:
		print "Ah, SportsCenter."
#		tv()
	elif "door" in choice or "out" in choice:
		outside()
	elif "baby" in choice or "bedroom" in choice:
		print "Dad to the rescue!"
#		bedroom()
	else:
		print "Stop fucking around! Parenting is super important!"
		# then what? maybe just:
		# living_room()
		
def outside():
	print """
	You step outside. Breathing the autumn air almost makes up for
	the fact that you're a total deadbeat. So, what are you gonna
	do, Deadbeat Dad? Head for the bar? Or just take a stroll to
	"clear your head?"
	"""
	
	choice = raw_input("> ")
	
	if "walk" in choice or "head" in choice:
		bob()
	elif "bar" in choice:
		bar()
	else:
		outside()
		
def bob():
	print """
On your stroll you see your old friend Hobo Bob. You're not
entirely sure what place Bob enjoys in the urban ecology. You
think he might be homeless, although he's always good for a
chat. Lately he's been plying you with questionable parenting
advice. So, what about Bob?	
	"""
	
	choice = raw_input("> ")
	
	if "ask" in choice or "advice" in choice:
		bob_advice()
	else:
		bob_beatdown()
		
def bob_advice():
	print """	
"You know, I'm glad you asked." Bob gives you a sober look.
"You see, children are the greatest blessing we can ever be
given. But they're also the greatest curse."
	
Bob is giving you one of those looks, like someone who is
willing to divulge the world's greatest secret, if only you'd
ask.	
	"""
	
	choice = raw_input("> ")
	
	if "ask" in choice:
		print """		
"Well, it's a little know fact, but before the Malacore invasion,
humans lived forever, and had no need for offspring. Only through
the Curse of Malingerus Malacorus were we condemned to this endless
cycle of death and procreation.		
		"""
	else:
		bob_beatdown()
		
def bob_beatdown():
	print """	
Bob mumbles something about the need to break chains through
transcendental fisting. At least you think that's what he says. This 
must not be one of his better days. You know you need to shake him
off or you'll come back to the house somewhat worse for the wear.	
	"""
	
	bob_wounded = False
	
	while True:
		print "Bob's still following you. What do you do?"
		choice = raw_input("> ")
		if "punch" in choice or "kick" in choice:
			bob_wounded = True
			print '"Ouch," Bob says. "What the fuck!?"'
		elif bob_wounded and "money" in choice:
			print "Okay. I'll take the cash."
			break
		elif "money" in choice:
			print '"You know I can\'t be bought."'
		else:
			print '"I don\'t even know what the fuck that means, man."'
		
bob()