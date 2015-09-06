from sys import exit

def living_room():

	print "You are sitting in your living room."
	print "You haven't slept much, so you're not really at 100 percent."
	print "And just when you think you might have things calmed down,"
	print "you hear your baby crying in your bedroom."
	print "Your wife's in there, trying to get some sleep."
	print "She's got some big thing tomorrow."
	print "Still, you look at the tv."
	print "You look at the door that used to take you to the outside world."
	print "What do you do?"
	
	choice = raw_input("> ")
	
	if "tv" in choice or "watch" in choice:
		print "Ah, SportsCenter."
		tv()
	elif "door" in choice or "out" in choice:
		print "A perfect autumn evening almost makes you forget what a deadbeat you are."
		outside()
	elif "baby" in choice or "bedroom" in choice:
		print "Dad to the rescue!"
		bedroom()
	else:
		print "Stop fucking around! Parenting is super important!"
		

"""
def tv():

def outside():

def bedroom()"
"""
		
living_room()