import numpy as np
from PIL import Image

def generate_autostereogram(width, height, pattern_width=50):
    # Create a random pattern for the autostereogram
    pattern = np.random.randint(0, 256, size=(height, pattern_width), dtype=np.uint8)
    
    # Generate autostereogram by repeating the pattern horizontally
    autostereogram = np.tile(pattern, (1, int(width / pattern_width) + 1))[:, :width]
    
    return autostereogram

def save_image(image, filename):
    # Convert numpy array to PIL Image and save
    Image.fromarray(image).save(filename)

def main():
    # Specify dimensions for the stereogram
    width = 640
    height = 480
    
    # Generate autostereogram
    autostereogram = generate_autostereogram(width, height)
    
    # Save the generated autostereogram image
    save_image(autostereogram, "autostereogram.png")
    print("Autostereogram generated and saved as autostereogram.png")

if __name__ == "__main__":
    main()
