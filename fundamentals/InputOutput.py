# to get input from the user 
user_name = input("Enter you name: ")
user_age = input("Enter you age: ")

# so in the bottom code we want to get the input from the user about their skills, so we have to allow the user to enter multiple entries, but we can also use the following method also, but it is not effective and we will find out why - > 


# user_skills = input("Enter your skills: ")

# but first let's use other methods to let the user input which are better 
#  using a loop 


# skills = []
# num_skills  = int(input("How many skills do you have ? "))
# for i in range(num_skills):
#   skill = input("Enter skill #" + str(i+1) + ": ")
#   skills.append(skill)
# print("Your skills are: ", skill)

# education 


# domain_knowledge = []
# domain_k = int(input("how many domains of knowledge do you have ?"))
# for i in range(domain_k):
#   domains = input("Enter domain name #" + str(i+1)+ ": ")
#   domain_knowledge.append(domains)
# print("you have domain knowledge of : ", domain_knowledge)
# print(f"Hello {user_name} !, age:{user_age} , and you have skills in {domain_knowledge}")


# now we will use a while loop with a sentinel value 
# so this loop will ask the user continously for their likings and they can enter as many values they want as compared to earlier using for loop where we first decides the user skills number and the user could only enter those number of skills, but now the user can enter as many as he wants 

Likes = []
interests = input("Enter your interests (type 'done' to finish):")

while interests != "done":
  Likes.append(interests)
  interests  = input("Enter your interest (type 'done' to finish):")

print("your interests are: ", Likes)

# using a list comprehension , 
num_skills = int(input("how many skills do you have?"))
expertise = [input("Enter skills #" + str(i+1) + ":") for i in range(num_skills)]

print("your expertise is in: ", expertise)


# using the split method: - to allow the user to enter the skills all at once , then split() method will split the string into a list of individual skills. 

skills_string  = input("Enter your skills separated by commans: ")
powers = skills_string.split(",")

print("your powers are: ", powers)

