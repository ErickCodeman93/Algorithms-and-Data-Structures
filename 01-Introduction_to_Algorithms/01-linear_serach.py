# This algorithms only work when the numbers is sorted

def linear_serch( list, target ):
	"""
	Returns the index position of the target if found, else returns None
	"""

	# for item in list 
	for i in range( 0, len( list ) ): 
		if list[ i ] == target:
			return i
	
	return None

def verify( index ):
	if index is not None:
		print( "Target found at index: ", index )
	else:
		print( "Target not found in list" )


numbers = [ 1,2,3,4,5,6,7,8,9,10 ]

result = linear_serch( numbers, 12 )

verify( result )

result = linear_serch( numbers, 2 )

verify( result )