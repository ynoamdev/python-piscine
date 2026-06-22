from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """This function  load the image "animal.jpeg",
    print some information about it and display it after zooming.
    """
    try:
        img = ft_load("animal.jpeg")
        print(f"{img}")
        zoom = img[200:600, 400:800, 0:1]
        print(f"New shape after slicing: {zoom.shape}")
        print(f"{zoom}")
        plt.imshow(zoom, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
