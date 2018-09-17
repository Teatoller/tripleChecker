#  unique_Element.py
def find_Unique_Element_inArray(input_array, num):
    ones_compliment = 0
    twos_compliment = 0

    for i in range(num):
        twos_compliment = twos_compliment | (ones_compliment & input_array[i])

        ones_compliment = ones_compliment ^ input_array[i]

        identical_bitwise_pack = ~(ones_compliment & twos_compliment)

        ones_compliment &= identical_bitwise_pack

        twos_compliment &= identical_bitwise_pack

    return ones_compliment


input_array = [5, 3, 4, 3, 5, 5, 3]
num = len(input_array)
print('The single exceptional element in the list is ',
      find_Unique_Element_inArray(input_array, num))
