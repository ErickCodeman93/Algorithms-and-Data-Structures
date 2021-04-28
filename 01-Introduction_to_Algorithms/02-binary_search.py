# This algorithms only work when the numbers is sorted

def binary_search( list, target ):
	first = 0
	last = len( list ) - 1

	while first <= last:
		mindpoint = ( first + last ) // 2
		# print( mindpoint )

		if list[ mindpoint ] == target:
			return mindpoint
		elif list[ mindpoint ] < target:
			first = mindpoint + 1
		else:
			last = mindpoint - 1

	return None

def verify( index ):
	if index is not None:
		print( "Target found at index: ", index )
	else:
		print( "Target not found in list" )


numbers = [ 1,2,3,4,5,6,7,8,9,10 ]

result = binary_search( numbers, 12 )

verify( result )

result = binary_search( numbers, 6 )

verify( result )