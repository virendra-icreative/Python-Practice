#Format()

#'<' - Left aligns the result (within the available space)
print("{0} was founded in {1:<15}!".format("GeeksforGeeks", 2009))
#'>' - Right aligns the result (within the available space)
print("{0} was founded in {1:>15}!".format("GeeksforGeeks", 2009))
#'^' - Center aligns the result (within the available space)
print("{0:*^20} was founded in {1:<15}!".format("GeeksforGeeks", 2009))
#'=' - Places the sign to the left most position
print("{0:*^20} was founded in {1:=15}!".format("GeeksforGeeks", 2009))
#'+' - Use a plus sign to indicate if the result is positive or negative
print('{:+},{:+}'.format(12345,-45678))
#'-' - Use a minus sign for negative values only
print('{:-},{:-}'.format(-12345,45678))
#' ' - Use a leading space for positive numbers
print('{: } asdf'.format(12345))
#',' - Use a comma as a thousand separator
print('{:,}'.format(123456789))
#'_' - Use a underscore as a thousand separator
print('{:_}'.format(123456789))
#'b' - Binary format
print('{:b}'.format(12))
#'c' - Converts the value into the corresponding unicode character
print('{:c}'.format(69))
#'d' - Decimal format
print('{:d}'.format(0b1100))
#'e' - Scientific format, with a lower case e
print('{:e}'.format(69123456789))
#'E' - Scientific format, with an upper case E
print('{:E}'.format(69123456789))
#'f' - Fix point number format
print('{:.3f}'.format(69.45))
#'F' - Fix point number format, upper case
print('{:.3F}'.format(69.45))
#'g' - General format
print('{:g}'.format(69.4500))
#'G' - General format (using a upper case E for scientific notations)
print('{:G}'.format(6.912346E+10))
#'o' - Octal format
print('{:o}'.format(69))
#'x' - Hex format, lower case
print('{:x}'.format(69))
#'X' - Hex format, upper case
print('{:X}'.format(69))
#'n' - Number format
print('{:n}'.format(69))
#'%' - Percentage format
print('{:.2%}'.format(69))