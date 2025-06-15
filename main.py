from blog_fetcher import fetch_blog
from text_analyzer import extract_segments
from prompt_refiner import refine_prompts
from image_generator import generate_images
from safety_checker import is_safe

def main():
    url = "https://www.mynachiketa.com/post/speech-on-hanuman-jayanti-in-english?uniqueIdentifier=xQfEvo1749967733448"
    print("\nFetching blog...")
    blog_text = fetch_blog(url)
    # print(blog_text)

    print("\nExtracting visual segments...")
    segments = extract_segments(blog_text)
    print(segments)
    # segments = ['- Image of Kabir Das as a baby floating on the riverbank, being adopted by the weaver couple', "- Illustration of children reciting Kabir's dohas in a school program", '- Visual of people sharing food and clothes with the needy on Kabir Das Jayanti', '- Cover image of the special book "Discovering God" for children, featuring Hindu philosophy, knowledge of Gita and Upanishads, shlokas, and mantras']
    print("\nRefining prompts...")
    prompts = refine_prompts(segments)
    print(prompts)
    # prompts = ['Create an image of a cute baby floating on a river, smiling happily as a kind weaver couple reaches out to adopt him. The sun is shining brightly, and colorful flowers are blooming all around. The baby is wearing a tiny turban and a little smile on his face.', "Create a colorful picture of a group of smiling children standing on a stage, each holding a microphone and reciting Kabir's dohas. The background can show a school auditorium filled with happy audience members clapping and cheering. Add some bright lights and decorations to make it look like a fun and exciting school program.", 'Create an image of a group of happy people, both adults and children, smiling and sharing plates of food and piles of clothes with people in need. The sun is shining, and there are colorful flowers in the background. Everyone is happy and helping each other on Kabir Das Jayanti.', 'Create a colorful and cheerful image of a group of diverse children sitting in a circle, surrounded by blooming flowers and butterflies. In the center of the circle, place a magical book titled "Discovering God" with a bright, shining light emanating from its pages. Include symbols of Hinduism like lotus flowers, Om symbols, and a small statue of Lord Ganesha. The children are smiling and pointing at the book with excitement, showing their eagerness to learn about Hindu philosophy, Gita, Upanishads, shlokas, and mantras. The overall vibe of the image should be warm, inviting, and full of wonder.']


    print("\nFiltering and generating images...")
    safe_prompts = [p for p in prompts if is_safe(p)]
    paths = generate_images(safe_prompts)

    print("\nGenerated images saved:")
    for p in paths:
        print(p)

if __name__ == "__main__":
    main()
