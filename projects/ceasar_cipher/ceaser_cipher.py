import art
print(art.logo)

def caesar(start_text, shift_amount, cipher_direction):
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  char_list = list(start_text)
  for char in char_list:
    if char in alphabet:
      c_index = char_list.index(char)
      a_index = alphabet.index(char)
      if cipher_direction == "encode":
        cipher_char =  alphabet[((a_index + shift_amount) % len(alphabet))]
      elif cipher_direction == "decode":
        cipher_char =  alphabet[((a_index + shift_amount * -1) % len(alphabet))]
      char_list[c_index] = cipher_char
  cipher_text = "".join(char_list)
  print(f"The {direction}d text is {cipher_text}")


continue_program = True

while continue_program:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  should_continue = input("\nWould you like to restart the cipher program?\n").lower()
  if should_continue == "yes":
    continue_program = True
  else:
    print("Goodbye")
    continue_program = False