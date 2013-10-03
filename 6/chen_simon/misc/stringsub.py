

orig="""
One day NAME was waling in the PLACE. 
NAME was tired when he came upon a THING.
"""

s="""
One day %(name)s was waling in the %(place)s. 
%(name)s was tired when he came upon a %(thing)s.
"""

#d={'name':'Tommy',
#   'place':'woods',
#   'thing':'Lepper-Khan'}

d={}
d['name']='Tommy', 'John'
d['place']='woods','tree'
d['thing']='Lepper-Khan', 'Simon'

t = {'name', 'place', 'thing'}
print s%{'name' : d['name'][0] , 'place' : d['place'][0], 'thing' : d['thing'][0] };
