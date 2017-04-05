# HTML 
# Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

# Parsing 
# Parsing is the process of syntactic analysis of a string of symbols. It involves resolving a string into its component parts and describing their syntactic roles.

# HTMLParser 
# An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, text, comments, and other markup elements are encountered.

# Example (based on the original Python documentation):

# Code

# from HTMLParser import HTMLParser

# # create a subclass and override the handler methods
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print "Found a start tag  :", tag
#     def handle_endtag(self, tag):
#         print "Found an end tag   :", tag
#     def handle_startendtag(self, tag, attrs):
#         print "Found an empty tag :", tag

# # instantiate the parser and fed it some HTML
# parser = MyHTMLParser()
# parser.feed("<html><head><title>HTML Parser - I</title></head>"
#             +"<body><h1>HackerRank</h1><br /></body></html>")
# Output

# Found a start tag  : html
# Found a start tag  : head
# Found a start tag  : title
# Found an end tag   : title
# Found an end tag   : head
# Found a start tag  : body
# Found a start tag  : h1
# Found an end tag   : h1
# Found an empty tag : br
# Found an end tag   : body
# Found an end tag   : html


# .handle_starttag(tag, attrs)

# This method is called to handle the start tag of an element. (For example: <div class='marks'>) 
# The tag argument is the name of the tag converted to lowercase. 
# The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag's <> brackets. 


# .handle_endtag(tag)

# This method is called to handle the end tag of an element. (For example: </div>) 
# The tag argument is the name of the tag converted to lowercase. 


# .handle_startendtag(tag,attrs)

# This method is called to handle the empty tag of an element. (For example: <br />) 
# The tag argument is the name of the tag converted to lowercase. 
# The attrs argument is a list of (name, value) pairs containing the attributes found inside the tag's <> brackets.

# Task

# You are given an HTML code snippet of  lines. 
# Your task is to print start tags, end tags and empty tags separately.

# Format your results in the following way:

# Start : Tag1
# End   : Tag1
# Start : Tag2
# -> Attribute2[0] > Attribute_value2[0]
# -> Attribute2[1] > Attribute_value2[1]
# -> Attribute2[2] > Attribute_value2[2]
# Start : Tag3
# -> Attribute3[0] > None
# Empty : Tag4
# -> Attribute4[0] > Attribute_value4[0]
# End   : Tag3
# End   : Tag2
# Here, the -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value. 
# The > symbol acts as a separator of the attribute and the attribute value.

# If an HTML tag has no attribute then simply print the name of the tag. 
# If an attribute has no attribute value then simply print the name of the attribute value as None.

# Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->).Comments can be multiline as well.

# Input Format

# The first line contains integer , the number of lines in a HTML code snippet.
# The next  lines contain HTML code.

# Constraints

# Output Format

# Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the given snippet.

# Use proper formatting as explained in the problem statement.

# Sample Input

# 2
# <html><head><title>HTML Parser - I</title></head>
# <body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
# Sample Output

# Start : html
# Start : head
# Start : title
# End   : title
# End   : head
# Start : body
# -> data-modal-target > None
# -> class > 1
# Start : h1
# End   : h1
# Empty : br
# End   : body
# End   : html


import re
inps = ['<script type="text/javascript" src="js/cufon-yui.js"></script>',
'<!--<script type="text/javascript" src="js/TitilliumMaps.font.js"></script>--><h1>Business Solutions</h1><br />',
'<h2>Business Insurance</h2><script type="text/javascript">',
'    Cufon.replace(\'h1, h2\', { fontFamily: "TitilliumMaps26L", hover: true });',
'</script>']

# comment = False

# file = open('test.txt', 'r') 
for inp in inps: 
	# print line.rstrip()

# for inp in inps:
	# inp = '<html><head><title>HTML Parser - I</title></head>'
	# inp = '<body data-modal-target class=\'1\'><h1>HackerRank</h1><br /></body></html>'
	# inp = '<html><head><title>HTML Parser - I</title></head><body><h1>HackerRank</h1><br /></body></html>'
	# print 'COOOMMMENT', bool(re.search(r'<!--', inp))
	# print 'COOOMMMENT', bool(re.search(r'-->', inp))
	# print re.findall('(.*)(?=<!--)(?<=<!--)(.*)', inp)
	
	if comment:
		if '-->' in inp:
			pts = inp.split('-->')
			inp = pts[1]
			comment = False
		else:
			continue

	pts = inp.split('<!--')

	if len(pts) > 1:
		if '-->' in pts[1]:
			pts2 = pts[1].split('-->')
			inp = pts[0] + pts2[1]
		else:
			inp = pts[0]
			comment = True

	m = re.findall('<([^<>]+)>', inp)

	# print pts
	# print m
	for i in m:
		# print i
		if i.startswith('/'):
			m = re.search('[a-zA-Z0-9]+', i)
			print 'End   :', m.group(0)
		elif i.endswith('/'):
			# m = re.search('[a-zA-Z0-9]+', i)
			# print 'Empty :', m.group(0)
			m = re.findall('\S+', i)
			for result in m:
				if m.index(result) == 0:
					print 'Empty :', result
				else:
					parts = result.split('=')
					print parts
					if len(parts) == 1:
						value = None
					else:
						value = re.findall('[\'\"](.*?)[\'\"]', parts[1])
						if value:
							value = value[0]
						else:
							value = None
						# value = re.search('(?<=[\'\"])(.*)(?=[\'\"])', parts[1])
						# print value
						# value = value.group(1) 
					print '->', parts[0], '>', value
		else:
			m = re.findall('\S+', i)
			for result in m:
				if m.index(result) == 0:
					print 'Start :', result
				else:
					parts = result.split('=')
					if len(parts) == 1:
						value = None
					else:
						value = re.findall('[\'\"](.*?)[\'\"]', parts[1])
						if value:
							value = value[0]
						else:
							value = None
						# value = re.search('[^\'"]+', parts[1])
						# value = value.group(0) 
					print '->', parts[0], '>', value

