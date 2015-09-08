from sys import exit

def living_room():
	print """
You are sitting in your living room. You haven't slept much, 
so you're not really at 100 percent. And just when you think
you might have things calmed down, you hear your baby crying
in your bedroom. Your wife's in there, trying to get some sleep.
She's got some big thing tomorrow. Still, you look at the tv.
You look at the door that used to take you to the outside world.
	"""
	
	while True:
		print "What do you do?"
		choice = raw_input("> ")
		if "tv" in choice or "watch" in choice:
			tv()
		elif "door" in choice or "out" in choice:
			outside()
		elif "baby" in choice or "bedroom" in choice:
			bedroom()
		else:
			print "Stop fucking around! Parenting is super important!"
		
def outside():
	print """
You step outside. Breathing the autumn air almost makes up for
the fact that you're a total deadbeat. So, what are you gonna
do, Deadbeat Dad? Head for the bar? Or just take a walk to
"clear your head?"
	"""
	
	while True:		
		print "Where to?"
		choice = raw_input("> ")
		if "walk" in choice:
			bob()
		elif "bar" in choice:
			bar()
		else:
			print "You scratch your nuts in quiet contemplation."
		
def bob():
	print """
On your stroll you see your old friend Hobo Bob. You're not
entirely sure what place Bob enjoys in the urban ecology. You
think he might be homeless, although he's usually good for a
chat. Lately he's been plying you with questionable parenting
advice. "Hey Chief," he says. Bob likes to call you Chief.
	"""
	
	print "So, what about Bob?"
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
	
Bob gives you a conspiratorial smile. He may be willing to
divulge the world's greatest secret, if only you'd ask.	
	"""
	
	print "You gonna make Bob's dreams come true?"
	choice = raw_input("> ")
	
	if "ask" in choice or "yes" in choice:
		print """		
"Well, it's a little know fact, but before the Malacore invasion,
humans lived forever, and had no need for offspring. Only through
the Curse of Malingerus Malacorus were we condemned to this endless
cycle of death and procreation.		
		"""
		bob_beatdown()
	else:
		bob_beatdown()
		
def bob_beatdown():
	print """	
Bob then mumbles something about the need to break chains through
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
			print '"Okay. I\'ll take the cash," Bob says before scampering off.'
			print """
And karma, with Bob its intrepid enforcer, has given you a fine
gift today. Continuing down a path of deadbeatness will only
lead to awkward conversations and violence. You head home, ready
to embrace your paternal duties. Good job Dad!
			"""
			exit(0)
		elif "money" in choice:
			print '"You know I can\'t be bought."'
		else:
			print '"I don\'t even know what the fuck that means, man."'
			
def tv():
	print """
Your wife's got this for sure. You can flip around a little bit and
stay in earshot to make sure the baby doesn't get out of hand. Late
night tv is always fun.
	"""
	
	count = 0
	
	while True:
		print "So what's it gonna be?"
		choice = raw_input("> ")
		if "sports" in choice:
			print """
Not much on this late. You finally find a professional lacrosse
replay. Apparently there's professional lacrosse in the US; who
knew? After awhile, you start to get into it. You pick a side. You
become an expert, arguing with the refs and the announcers. Do you
know anything about lacrosse? Has ignorance ever stopped you before?

Then you see yourself, and you see yourself seeing yourself, and so
on. You're Kane and the mirrors reflect your emptiness back at you
ad infinitum. Clutched by a powerful sense of life's impermanence
and the need to fill so many holes, you rush back to your bedroom.
You grab on tight to your nursing wife, your perfect baby nestled
between you. You vow to become the father to this child you never had.
You succeed. Your daughter gives a stunning eulogy after you pass
at the ripe age of 83. Your last thought is of that lacrosse match
on tv.
			"""
			exit(0)
		elif "movie" in choice:
			print """
You find an interesting looking documentary about the French artist
Paul Gauguin. Gauguin was a good artist struggling to become great.
Eventually, he found the muse in Tahiti. He knew he'd do his best work
there, and that becoming great meant he'd have to leave his wife and
children.

You have so much in you. So many dreams. You know you'll keep chasing
those dreams, one foot in bad parenting and the other in a life of
quiet desperation. Better to be one great thing than many mediocre ones.
What do you need? Nothing. You walk out with the clothes on your back.
Your wife's way less of a fuckup than you. She'll do just fine.
			"""
			exit(0)
		else:
			if count == 0:
				print "You feel like that'd be a good choice right now. You're just wrong."
				count += 1
			elif count == 1:
				print "Nothing. How much do we pay for this shit again?"
				count += 1
			else:
				print """
After so much surfing with so little success, you become mesmerized
by an infomercial for the perfect home glassblowing setup. Of course.
This is what I've been waiting for. You've always knows you were meant
to work with your hands. You're above all this corporate bullshit.
You're meant to be a craftsman. You go online and order, well within
the fifteen minute window, ensuring you'll get a bonus flame retardant
suit for nothing more than the cost of shipping and handling.

You can't wait to tell your wife about this exciting new development.
"Look, I don't know how to tell you this," she says, "but I'm fucking
your best friend. We need to get a divorce."
				"""
				exit(0)



"""
functions needed:
tv()
bedroom()
bar()
"""