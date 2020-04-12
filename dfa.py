"""
Κώδικας που θα χρησιμοποιηθεί ως βάση για την 1η εργασία
των Μεταγλωττιστών (αναγνώριση κειμένου μέσω αυτομάτου DFA).

ΠΡΟΣΟΧΗ: Προσθήκες στον κώδικα επιτρέπονται μόνο
στα σημεία (Α), (Β) και (Γ) - διαβάστε τα σχόλια!
"""


transitions = {
		's0' : {'DIGIT' : 's1', 'DOT' : 's2'},
		's1' : {'DIGIT' : 's1', 'DOT' : 's3'},
		's2' : {'DIGIT' : 's3'},
	       	's3' : {'DIGIT' : 's3'}
     	      } 


accepts = { 
	    's3' : 'FLOAT_TOKEN'
     	  }


def get_char(text,pos):
	""" Returns char (or char category) at position `pos` of `text`,
	or None if out of bounds. """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	if c >= '0' and c <= '9':
		return 'DIGIT'
	if c == '.':
		return 'DOT'
	
	return c
	

# Δεν επιτρέπεται η παρέμβαση στον κώδικα από αυτό το σημείο και κάτω! 

def scan(text,transitions,accepts,state):
	""" Starting from inital `state`, scans `text` while transitions
	exist in `transitions` dict. After that, if on a state belonging to
	`accepts` dict, returns the corresponding token object, else None.
	"""
	
	# initial position on text
	pos = 0
	
	# memory object for last seen accepting state
	matched = None
	
	while True:
		
		c = get_char(text,pos)	# get next char (or char category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char			

			# remember if current state is accepting
			if state in accepts:
				matched = { 'token':  accepts[state],
					    'lexeme': text[:pos] }
			
		else:	# no transition found, return last match or None
			return matched
			

# testing inputs
for test in ['12.456','6789.','.66998','1234','.']:
	m = scan(test,transitions,accepts,'s0')
	print("Testing '{}'\nResult: {}\n".format(test,m))


