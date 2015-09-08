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


tv()