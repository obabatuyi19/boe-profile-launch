# Reads top.html
top_html = open('./templates/top.html').read()

# Reads index.html
middle_html = open('./content/index.html').read()


# Reads bottom.html
bottom_html = open('./templates/bottom.html').read()

# combine files
print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)


#write out
open('./docs/index.html', 'w+').write(combined_html)

###### end of index.html ###########

# Reads top.html
top_html = open('./templates/top.html').read()

# Reads index.html
middle_html = open('./content/about.html').read()


# Reads bottom.html
bottom_html = open('./templates/bottom.html').read()

# combine files
print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)


#write out
open('./docs/about.html', 'w+').write(combined_html)

##### end of about.html #########

# Reads top.html
top_html = open('./templates/top.html').read()

# Reads index.html
middle_html = open('./content/resume.html').read()


# Reads bottom.html
bottom_html = open('./templates/bottom.html').read()

# combine files
print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)


#write out
open('./docs/resume.html', 'w+').write(combined_html)

##### end of resume.html #####

# Reads top.html
top_html = open('./templates/top.html').read()

# Reads index.html
middle_html = open('./content/portfolio.html').read()


# Reads bottom.html
bottom_html = open('./templates/bottom.html').read()

# combine files
print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)


#write out
open('./docs/portfolio.html', 'w+').write(combined_html)

##### end of portfolio.html ######

# Reads top.html
top_html = open('./templates/top.html').read()

# Reads index.html
middle_html = open('./content/contact.html').read()


# Reads bottom.html
bottom_html = open('./templates/bottom.html').read()

# combine files
print('combining HTML')
combined_html = top_html + middle_html + bottom_html
print(combined_html)


#write out
open('./docs/contact.html', 'w+').write(combined_html)

