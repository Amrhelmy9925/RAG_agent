from langchain.docstore.document import Document

# Create a list of guest dictionaries
guest_list = [
    {
        "name": "Dr. Nikola Tesla",
        "relation": "old friend from university days",
        "description": "Dr. Nikola Tesla is an old friend from your university days. He's recently patented a new wireless energy transmission system and would be delighted to discuss it with you. Just remember he's passionate about pigeons, so that might make for good small talk.",
        "email": "nikola.tesla@gmail.com"
    },
    {
        "name": "Lady Ada Lovelace",
        "relation": "mathematics mentor",
        "description": "Lady Ada Lovelace is a brilliant mathematician who has been working on computational algorithms. She's particularly excited to share her latest work on the analytical engine.",
        "email": "ada.lovelace@british.ac"
    },
    {
        "name": "Albert Einstein",
        "relation": "physics colleague",
        "description": "Dr. Einstein has recently published his work on special relativity. He enjoys playing violin and would appreciate discussing both music and physics.",
        "email": "a.einstein@physics.edu"
    }
]

# Create Document objects
docs = [
    Document(
        page_content="\n".join([
            f"Name: {guest['name']}",
            f"Relation: {guest['relation']}",
            f"Description: {guest['description']}",
            f"Email: {guest['email']}"      
        ]),
        metadata={"name": guest['name']}
    )
    for guest in guest_list
]