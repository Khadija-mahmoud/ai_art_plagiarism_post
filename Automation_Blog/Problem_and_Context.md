Porblem and Context of my Automation
Writing a blog can be a rewarding experience, especially when you're passionate about a topic. I recently embarked on a journey to explore a subject that has been generating significant buzz in recent years: plagiarism in AI-generated art. My blog journey was divided into four parts, each aimed at unraveling the intricate relationship between AI-generated art and its traditional counterparts.

As I delved into this intriguing topic, I began to notice a recurring issue that was both cumbersome and time-consuming: image resizing. Every time I uploaded an image to complement my blog posts, I found myself manually adjusting the image size to ensure it fit seamlessly within the content. This manual resizing process not only consumed valuable time but also hindered the fluidity of my blogging experience.

Determined to find a more efficient solution, I turned to technology for assistance. My first instinct was to leverage the power of code to create a tool that would allow me to easily adjust the size of every image I included in my blog. It was during this initial exploration that I encountered ChatGPT, a powerful AI language model capable of assisting with a wide range of tasks.

With ChatGPT at my disposal, I embarked on the journey of creating a code that would simplify the image resizing process. My goal was to develop a script that could automatically adjust the size of images while preserving their aspect ratio. This way, I could focus more on the content of my blog and less on the technicalities of image formatting.

I ventured into the world of programming, exploring various approaches to tackle this challenge. One of my initial attempts involved accessing the source code of the images themselves. I experimented with Python libraries and web scraping techniques to programmatically resize the images. While this approach had some success, it was far from ideal and required a significant amount of manual intervention.

Undeterred, I shifted my focus to a more direct and efficient solution. I realized that since my blog posts were primarily in Markdown format, I could modify the image tags directly within the Markdown files. This approach presented the advantage of maintaining a clean and organized structure for my blog.

My revised strategy involved creating a Python script that would parse my Markdown files, identify image tags, and adjust the image dimensions within those tags. The key challenge was to ensure that the aspect ratio of the images remained intact, preventing distortion or loss of image quality.

As I delved into coding this solution, I faced several iterations and refinements. Initially, I designed the script to generate a new Markdown file as the output, leaving the original Markdown untouched. However, I soon realized that this created unnecessary redundancy and complexity.

To streamline the process further, I modified the script to overwrite the existing Markdown files with the adjusted image tags. This change ensured that the input Markdown file was equivalent to the output Markdown file, eliminating the need for additional file management.

The script would identify image tags in the Markdown, calculate the adjusted dimensions based on the desired width, and update the tags accordingly. This way, I could simply run the script whenever I needed to resize images within my blog, saving both time and effort.

As I reflect on my journey, I am reminded of the power of technology and code to enhance the blogging experience. What began as a concern over image resizing evolved into a practical solution that not only simplified my blogging process but also allowed me to focus on the core message of my content.

In conclusion, my exploration of plagiarism in AI-generated art led me to discover a valuable lesson in problem-solving through code. The journey from manually adjusting image sizes to developing an automated solution highlighted the potential for technology to streamline creative endeavors. It reinforced the notion that with the right tools and a bit of coding, we can overcome challenges and make our blogging experiences more efficient and enjoyable.
