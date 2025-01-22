def ip_address(address):
  new_address = ""
  split_address = address.split(".")
  separator = "[.]"
  new_address = separator.join(split_address)
  return new_address
defangthis = "1.192.2.4.9"
print(ip_address(defangthis))



def placewall(words):
  new_structure = ""
  splitWord = words.split(".")
  line_wall = "|"
  new_structure = line_wall.join(splitWord)
  return new_structure

restrucutre_this = "M.a.r.t.i.a.n.M.a.n"
print(placewall(restrucutre_this))

def insert_slash(sentence):
  new_strucuture = ""
  splitWord = sentence.split(".")
  line_wall = "|"
  new_strucuture = line_wall.join(splitWord)
  return new_strucuture

remake_this = "hey.did.you.forget.this.today.?"
print(insert_slash(remake_this))
