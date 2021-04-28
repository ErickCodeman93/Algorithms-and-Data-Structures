def recursive_binary_search( list, target ):
	if len( list ) == 0:
		return False
	else:
		mindpoint = ( len( list ) ) // 2

		if list[ mindpoint ] == target:
			return True
		else:
			if list[ mindpoint ] < target:
				print( list[ mindpoint + 1 : ] )
				return recursive_binary_search( list[ mindpoint + 1 : ], target )
			else:
				print( list[ :mindpoint ] )
				return recursive_binary_search( list[ :mindpoint ], target )

def verify( result ):
	print( "Target found: ", result )

numbers = [ 1,2,3,4,5,6,7,8 ]

result = recursive_binary_search( numbers, 8 )
verify( result )

result = recursive_binary_search( numbers, 2 )
verify( result )