text = """
I am Hannan, a Computer Science student with a strong interest in AI, Machine Learning, and Data.
I enjoy learning by building real projects and turning what I learn into practical applications.
I am constantly improving my skills in Python, ML, PyTorch, SQL, and data technologies.
I like keeping my work organized through GitHub and sharing my progress along the way.
I am curious, consistent, and always looking for the next thing to learn and build.
My goal is to grow into a skilled AI/ML professional and create meaningful solutions with technology.
"""
chunks = text.strip().split("\n")
print(chunks)

for chunk in chunks:
    print("CHUNK")
    print(chunk)
    print()

# Multiple Text Chunking
text = """

I am Hannan, a Computer Science student with a strong interest in AI, Machine Learning, and Data.
I enjoy learning by building real projects and turning what I learn into practical applications.
I am constantly improving my skills in Python, ML, PyTorch, SQL, and data technologies.
I like keeping my work organized through GitHub and sharing my progress along the way.
I am curious, consistent, and always looking for the next thing to learn and build.
My goal is to grow into a skilled AI/ML professional and create meaningful solutions with technology.
"""
# Split text into multiple chunks
chunks = text.strip().split("\n\n")

print("MULTIPLE CHUNKS")
for chunk in chunks:
    print("CHUNK")
    print(chunk)
    print()

# Joining Chunks
joined_text = "\n\n".join(chunks)

print("JOINED TEXT")
print(joined_text)
