def defang_ip(ip_address):
  ip_address = str(ip_address)
  placeholder = ""
  split_ip = ip_address.split(".")
  defang = "[.]"
  placeholder = defang.join(split_ip)
  return placeholder

ip_one = "1.2.192.8.0"
print(defang_ip(ip_one))

def split_word(word):
  splitting = word.split("!")
  spacing  = " -".join(splitting)
  return spacing

print(split_word("adios!amigo"))
  
