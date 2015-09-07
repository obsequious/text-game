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