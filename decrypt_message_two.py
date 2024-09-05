encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here

# initialize start and end indices
start_idx = 1
end_idx = len(encrypted_message) - 2

# split message into list of characters
message = [char for char in encrypted_message]

# swap characters
while start_idx < end_idx: 
    message[start_idx], message[end_idx] = message[end_idx], message[start_idx]
    start_idx += 2
    end_idx -= 2

decrypted_message = ''.join(message)

print(decrypted_message)