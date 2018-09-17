#  unique_Element.py
def find_Unique_Element_inArray(input_array, num_bits):
    ones_compliment = 0
    twos_compliment = 0

    for i in range(num_bits):

        twos_compliment = twos_compliment | (ones_compliment & input_array[i])

        """
        ones_compliment & input_array[i] copies bit to result if it exists
        in both operands. These are added to twos by the | Binary OR .
        Binary | copies bits if it exists in either operand
        twos_compliment = twos_compliment | ones_complimet & input_array[i]

        """

        ones_compliment = ones_compliment ^ input_array[i]

        """
        ones_compliment ^ input_array[i] copies bit to result if it is
        set in one operand but not both. These are added to ones_compliment
        ones_compliment = ones_compliment ^ input_array[i]

        """

        identical_bits_pack = ~(ones_compliment & twos_compliment)

        """
        The identical_bits are those that appear three times. They are
        to be segregated from the 'ones_compliment' and the twos_compliment
        ~(ones_compliment & twos_compliment). ~is unary and has the effect of
        flipping bits

        """

        ones_compliment = ones_compliment & identical_bits_pack

        """
        ones_compliment & identical_bits_pack copies bit to result if it exists
        in both operands.Thereby removing identical bits from ones_compliment

        """

        twos_compliment = twos_compliment & identical_bits_pack

        """
        twos_compliment & identical_bits_pack copies bit to result if it exists
        in both operands.Thereby removing identical bits from twos_compliment

        """

    return ones_compliment


input_array = [5, 3, 4, 3, 5, 5, 3]
num_bits = len(input_array)
print('The single exceptional element in the list is ',
      find_Unique_Element_inArray(input_array, num_bits))
