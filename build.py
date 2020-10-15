
def main():

    pages = [
        {   
            "filename": "content/about.html",
            "output": "docs/about.html",
            "title": "About Me",
        },
        {
            "filename": "content/contact.html",
            "output": "docs/contact.html",
            "title": "My Contact",
        },
        {
            "filename": "content/index.html",
            "output": "docs/index.html",
            "title": "My Home page",
        },
        {
            "filename": "content/portfolio.html",
            "output": "docs/portfolio.html",
            "title": "My Portfolio",
        },
        {
            "filename": "content/resume.html",
            "output": "docs/resume.html",
            "title": "My Resume",
        },

    ]

    blog_posts = [
        {
        "filename": "blog/1.html",
        "output": "docs/blog_post_1.html",
        "date": "September 3rd, 2018",
        "title": "My experience so far as a noob at Kickstart Coding",
        },
        {
        "filename": "blog/2.html",
        "output": "docs/blog_post_2.html",
        "date": "September 10th, 2018",
        "title": "So far I really like Ubuntu Linux",
        },
        {
        "filename": "blog/3.html",
        "output": "docs/blog_post_3.html",
        "date": "September 15th, 2018",
        "title": "My thoughts on Python so far",
        },
        
    ]
    

    for page in pages:
        #print('page:', page)

        # Read in the base template
        template = open("./templates/base.html").read()
        #print(template)

        # Read in the content of the index HTML page
        #print(page["filename"])
        index_content = open(page["filename"]).read()
        #print(index_content)

        # Use the string replace
        finished_index_page = template.replace("{{content}}", index_content).replace("{{title}}", page['title'])

        open(page["output"], "w+").write(finished_index_page)

        page_title = page['title']
        print(page_title)


    ############ blog posts section ##########################
    for blog in blog_posts:
        #print('blog:', blog)

        # Read in the blog_base template
        template = open("./templates/blog_base.html").read()
        #print(template)

        # Read in the content of the index HTML page
        #print(page["filename"])
        blog_index_content = open(blog["filename"]).read()
        #print(index_content)

        # Use the string replace
        finished_index_blog = template.replace("{{content}}", blog_index_content).replace("{{title}}", blog['title'])

        open(blog["output"], "w+").write(finished_index_blog)

        blog_title = blog['title']
        print(blog_title)

    ###### End of blog posts ############################        
if __name__ == "__main__":
    main()



