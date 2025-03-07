import os
import random
import argparse
from PIL import Image, ImageDraw, ImageFilter


def generate_shapes_images(
    num_pictures,
    dimensions,
    output_dir,
    shape_size,
    distort_on,
):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Image dimensions
    width, height = dimensions

    # Generate images
    for i in range(num_pictures):
        # Create a blank RGB image
        img = Image.new(
            "RGB", (width, height), color=(255, 255, 255)
        )  # White background

        # Draw the image
        draw = ImageDraw.Draw(img)

        # Choose a random color
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Choose a random shape (star or square)
        shape = random.choice(["star", "square"])

        # Calculate the position for the shape (centered)
        x = (width - shape_size) // 2
        y = (height - shape_size) // 2

        # Draw the shape
        if shape == "star":
            # Define the points for a star
            star_points = [
                (x + shape_size // 2, y),  # Top point
                (x + shape_size * 0.6, y + shape_size * 0.4),  # Right inner point
                (x + shape_size, y + shape_size * 0.4),  # Right outer point
                (
                    x + shape_size * 0.7,
                    y + shape_size * 0.7,
                ),  # Bottom right inner point
                (x + shape_size * 0.8, y + shape_size),  # Bottom right outer point
                (x + shape_size // 2, y + shape_size * 0.8),  # Bottom point
                (x + shape_size * 0.2, y + shape_size),  # Bottom left outer point
                (x + shape_size * 0.3, y + shape_size * 0.7),  # Bottom left inner point
                (x, y + shape_size * 0.4),  # Left outer point
                (x + shape_size * 0.4, y + shape_size * 0.4),  # Left inner point
            ]
            draw.polygon(star_points, fill=color)
        elif shape == "square":
            # Draw a square
            draw.rectangle([x, y, x + shape_size, y + shape_size], fill=color)

        # Apply distortion if enabled
        if distort_on:
            img = img.filter(ImageFilter.GaussianBlur(radius=2))  # Example distortion

        # Save the image
        img_path = os.path.join(output_dir, f"image_{i+1}.png")
        img.save(img_path)
        print(f"Saved: {img_path}")

    print(
        f"All {num_pictures} images generated and saved successfully in '{output_dir}'!"
    )


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Generate images with different colors, shapes, and distortion."
    )
    parser.add_argument(
        "-n",
        "--num-pictures",
        type=int,
        default=10,
        help="Number of pictures to generate (default: 10).",
    )
    parser.add_argument(
        "-d",
        "--dimensions",
        type=int,
        nargs=2,
        default=[300, 300],
        help="Dimensions of the images (width height) (default: 300 300).",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=str,
        default="data/img",
        help="Output directory to save images (default: data/img).",
    )
    parser.add_argument(
        "-s",
        "--shape-size",
        type=int,
        default=100,
        help="Size of the shapes (default: 100).",
    )
    parser.add_argument(
        "--distort", action="store_true", help="Enable distortion in the images."
    )

    # Parse arguments
    args = parser.parse_args()

    # Call the function to generate images
    generate_shapes_images(
        args.num_pictures,
        args.dimensions,
        args.output_dir,
        args.shape_size,
        args.distort,
    )
