from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """This function load the image "animal.jpeg", cut a square
        part from it and transpose it to produce an image.
    """
    try:
        img = ft_load("animal.jpeg")
        zoom = img[100:500, 400:800, 0:1]
        print(f"The shape of image is: ({zoom.shape})")
        print(f"{zoom}")
        transposed = np.zeros((400, 400), dtype=int)
        for i in range(400):
            for j in range(400):
                transposed[j, i] = zoom[i, j, 0]
        print(f"New shape after Transpose: {transposed.shape}")
        print(f"{transposed}")
        plt.imshow(transposed, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
